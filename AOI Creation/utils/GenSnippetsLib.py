import json
import os
import re

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.formatters.bbcode import BBCodeFormatter
from pygments.lexers.jvm import JavaLexer
from pygments.lexers.python import Python3Lexer
from pygments.styles import get_style_by_name

def parse_bbcode_list(bbcode, logging):
    """parse code letter by letter, removing metadata characters but assigning them to the parsed letter dictionary"""
    result = []
    pattern = "\[[^\[\]]*?\]"
    idx = 0
    base_color = (0, 0, 0, 255)
    color = base_color
    bold = False
    italic = False
    aoi_default = "None"
    aoi_name = [aoi_default]
    if logging:
        print('bbcode', len(bbcode), bbcode)
    while idx < len(bbcode):
        data = re.search(pattern, bbcode[idx:])
        meta = False

        if data is not None and data.start(0) == 0:
            value = data.group(0).strip("[").strip("]")
            if logging:
                print('value', value)
            if "/AOI" in value:
                meta = True
                aoi_name.pop()
                if logging:
                    print(f"after deletion {aoi_name}")
            elif "AOI" in value:
                meta = True
                aoi_name.append(value[4:])
                if logging:
                    print(f"after insertion {aoi_name}")

            if "/aoi" in value:
                meta = True
                aoi_name.pop()
                if logging:
                    print(f"after deletion {aoi_name}")
            elif "aoi" in value:
                meta = True
                aoi_name.append(value[4:])
                if logging:
                    print(f"after insertion {aoi_name}")
            if "/color" in value:
                meta = True
                color = base_color
            elif "color" in value:
                meta = True
                color = tuple(int(value[i: i + 2], 16) for i in (7, 9, 11))
                color = (color[0], color[1], color[2], 255)

            # if "/b" in value:
            #     meta = True
            #     bold = False
            # elif "b" in value:
            #     meta = True
            #     bold = True
            # if "/i" in value:
            #     meta = True
            #     italic = False
            # elif "i" in value:
            #     meta = True
            #     italic = True

            if meta == True:
                idx += data.end(0)

        if meta==False:
            result.append({"letter": bbcode[idx], "color": color, "bold": bold, "italic": italic, "AOI": [value for value in aoi_name]})
            idx += 1
    if len(aoi_name) != 1:
        raise Exception("AOI not closed - " + aoi_name[-1])
    return result


def set_font(data, regular, bold, italic, bolditalic):
    """determine font with given font formatting for each letter in the parsed dataset"""
    new_result = []
    for entry in data:
        if entry["bold"] == True and entry["italic"] == True:
            entry["font"] = bolditalic
        elif entry["bold"] == True:
            entry["font"] = bold
        elif entry["italic"] == True:
            entry["font"] = italic
        else:
            entry["font"] = regular
        new_result.append(entry)

    return new_result


def create_background(width, height, color):
    """creats image template with given background color"""
    r = np.full([height, width], color[0], np.uint8)
    g = np.full([height, width], color[1], np.uint8)
    b = np.full([height, width], color[2], np.uint8)
    a = np.full([height, width], color[3], np.uint8)
    background = np.dstack((r, g, b, a))
    return background


def create_image(source_json, font_path="\\fonts\\ttf\\", lexer=Python3Lexer, logging=False):
    """creates image from code snippet with syntax highlighting and AOIs with the information stored in data, such as background color, width, height, spacing, font... """
    data = {}
    with open(source_json) as f:
        data = json.load(f)

    code = ""
    for line in data["source-code"]:
        code += line + "\n"

    background_color = (data["background-color"][0],
                        data["background-color"][1],
                        data["background-color"][2])
    width_margin = data["width-margin"]
    height_margin = data["height-margin"]
    spacing = data["spacing"]

    regular = ImageFont.truetype(
        os.getcwd() + font_path + data["font-normal"], data["font-size"], encoding="unic")
    bold = ImageFont.truetype(
        os.getcwd() + font_path + data["font-bold"], data["font-size"], encoding="unic")
    italic = ImageFont.truetype(
        os.getcwd() + font_path + data["font-italic"], data["font-size"], encoding="unic")
    bolditalic = ImageFont.truetype(os.getcwd(
    ) + font_path + data["font-bold-italic"], data["font-size"], encoding="unic")

    if logging:
        print(f"code init {code}")
    code_aois = parse_bbcode_list(code, logging)
    actual_code = "".join([l["letter"] for l in code_aois])
    if logging:
        print(f"code after bbcode for AOIs{actual_code}")
    
    code_styled = highlight(actual_code,
                            lexer(), 
                            BBCodeFormatter(
                                 line_numbers=False, 
                                #  style=get_style_by_name(data["style"] if "style" in data else "vs"))
                                style = get_style_by_name("no"))
        )
    code_styled = parse_bbcode_list(code_styled, logging)
    actual_code2 = "".join([l["letter"] for l in code_styled])
    if logging:
        print(f"code after bbcode for highlights:\n{actual_code2}")
    if len(code_aois) != len(code_styled):
        print('ERROR')
        print(f'code does not match:\n"{actual_code}"\n"{actual_code2}"')
        print(f'difference in length:\n"{len(actual_code)}"\n"{len(actual_code2)}"')
        # raise Exception()
    code = []
    for idx, c in enumerate(code_styled):
        # if logging:
        #     print('styled', c)
        #     print('AOI', code_aois[idx])
        code.append({"letter": c["letter"], "color": c["color"], "bold": c["bold"], "italic": c["italic"], "AOI": code_aois[idx]["AOI"]})
    if logging:
        print(f"code after highlight {code}")

    code = set_font(code, regular, bold, italic, bolditalic)
    # if logging:
    #     print(f"code after set_font {code}")

    source_code = []
    tmp_source_code = ""
    for tmp_data in code:
        if tmp_data["letter"] == "\n":
            source_code.append(tmp_source_code)
            tmp_source_code = ""
        else:
            tmp_source_code += tmp_data["letter"]

    img = Image.new("RGBA", (1, 1), color="white")
    draw = ImageDraw.Draw(img)
    max_length = max([draw.textsize(txt, regular)[0] for txt in source_code]) + 2 * width_margin
    max_height = (
            sum([draw.textsize("placeholder", regular)[1] + spacing for txt in data["source-code"]]) + 2 * height_margin
    )

    img = Image.new("RGBA", (max_length, max_height), color=background_color)
    draw = ImageDraw.Draw(img)

    width_current = width_margin
    height_current = height_margin
    result = []
    for letter in code:
        if letter["letter"] == "\n":
            width_current = width_margin
            height_current = height_current + draw.textsize("placeholder", regular)[1] + spacing
            letter["BoundingBox"] = (0, 0, 0, 0)
        else:
            letter["BoundingBox"] = draw.textbbox(
                (width_current, height_current), letter["letter"], font=letter["font"]
            )
            draw.text((width_current, height_current), letter["letter"], letter["color"], font=letter["font"])
            width_current += draw.textsize(letter["letter"], regular)[0]

        result.append(letter)
    return img, result

AOI_PADDING=5
AOI_NAME_COLOR_MAPPING ={
    "method_signature":"#980000", #red
            "method_identifier":"#00ff00" ,#green
            "method_argument_declaration":"#0000ff" ,#blue
            "method_call":"#cc4125", #light red
            "method_call_identifier":"#8cff8c" ,#light green
            "method_arguments":"#8c8cff", #light blue
            "for":"#ff00ef", #bright pink
            "if":"#ff0000", #red
            "else_if":"#ffa000", #bright orange
            "else":"#f1c232", #light yellow
            "while":"#00ffff" ,#bright cyan
            "for_body":"#d000ac", #dark pink
            "if_body":"#990000" ,#dark red
            "else_if_body":"#d46500", #dark orange
            "else_body":"#c4b800", #dark yellow
            "while_body":"#134f5c" ,#dark cyan
            "arithmetic_expression":"#ffa07a" ,#light salmon
            "return":"#63c5ff" ,#light blue
            "declaration":"#b500ff" ,#violet
            "varassign":"#4a86e8", #dark dim blue
            "if_head":"#ea9999", #light red
            "else_if_head":"#f6b26b", #light orange
            "else_head":"#fff000", #bright yellow
            "for_head":"#ff92f8", #light pink
            "while_head":"#76a5af" ,#light turquoise
            "class_declaration":"#555555", #dark grey
            "type":"#ff0000", #red
            "return_type":"#76a5af",
            "function": "#00ff00"
}


def match_aoi_name_color(aoi_name):
    """ determine aoi color based on name"""
    if aoi_name in AOI_NAME_COLOR_MAPPING:
        return AOI_NAME_COLOR_MAPPING[aoi_name]
    return "#000000"# black

def generate_AOI_boxes(image, aoi_list, max_size):
    """adds boxes for aois into image"""
    width, height = image.size
    aoi_clustered = []
    current_left = []
    current_top = []
    current_right = []
    current_bottom = []
    current_aoi = []
    color = []
    for letter in aoi_list:
        # Close AOI
        if letter['letter'] in " \t\n":
            continue
        if len(letter["AOI"]) == 1:
            for idx in range(len(current_aoi)):
                aoi_clustered.append((len(aoi_clustered), current_aoi[idx], current_left[idx], current_top[idx], current_right[idx], current_bottom[idx], color[idx]))

            current_aoi = []
            color = []
            current_left = []
            current_top = []
            current_right = []
            current_bottom = []
            continue
        # There is no AOI set
        if len(current_aoi) == 0:
            current_aoi = []
            color = []
            current_left = []
            current_top = []
            current_right = []
            current_bottom = []
            for idx in range(1, len(letter["AOI"])):
                current_aoi.append(letter["AOI"][idx])
                current_left.append(letter["BoundingBox"][0])
                current_top.append(letter["BoundingBox"][1])
                current_right.append(letter["BoundingBox"][2])
                current_bottom.append(letter["BoundingBox"][3])
                color.append(letter["color"])
            continue

        for idx in reversed(range(len(current_aoi))):
            if current_aoi[idx] in letter["AOI"]:
                current_left[idx] = min(current_left[idx], letter["BoundingBox"][0])
                current_top[idx] = min(current_top[idx], letter["BoundingBox"][1])
                current_right[idx] = max(current_right[idx], letter["BoundingBox"][2])
                current_bottom[idx] = max(current_bottom[idx], letter["BoundingBox"][3])
                # remove the AOI from the letter
                letter["AOI"].remove(current_aoi[idx])
            else:
                aoi_clustered.append((len(aoi_clustered), current_aoi[idx], current_left[idx], current_top[idx], current_right[idx], current_bottom[idx], color[idx]))
                del current_aoi[idx]
                del current_left[idx]
                del current_top[idx]
                del current_right[idx]
                del current_bottom[idx]
                del color[idx]

        for idx in range(1, len(letter["AOI"])):
            current_aoi.append(letter["AOI"][idx])
            current_left.append(letter["BoundingBox"][0])
            current_top.append(letter["BoundingBox"][1])
            current_right.append(letter["BoundingBox"][2])
            current_bottom.append(letter["BoundingBox"][3])
            color.append(letter["color"])

    for idx in range(len(current_aoi)):
        aoi_clustered.append((len(aoi_clustered), current_aoi[idx], current_left[idx], current_top[idx], current_right[idx], current_bottom[idx], color[idx]))

    return_aoi = []

    for aoi in aoi_clustered:
        outline_color = match_aoi_name_color(aoi[1])
        image_draw = ImageDraw.Draw(image)
        # print(f"{aoi[1]} width: {aoi[4]-aoi[2]}, height: {aoi[5]-aoi[3]}")
        # image_draw.rectangle([aoi[2]-AOI_PADDING, 
        #                       aoi[3]-AOI_PADDING-(aoi[4]-aoi[2])/75, #add padding to height depending on the aois width
        #                       aoi[4]+AOI_PADDING, 
        #                       aoi[5]+AOI_PADDING+(aoi[4]-aoi[2])/75],  #add padding to height depending on the aois width
        #                       outline=outline_color, fill=None, width=2)
        # print(f"{aoi[1]} width: {aoi[4]-aoi[2]} width_move: {max_size[0] // 2 - width // 2}, height: {aoi[5]-aoi[3]}, height_move: {max_size[1] // 2 - height // 2}")
        x0 = aoi[2]-AOI_PADDING + width // 2 - max_size[0] // 2
        y0 = aoi[3]-AOI_PADDING-(aoi[4]-aoi[2])/75 + height // 2 - max_size[1] // 2 # add padding to height depending on the aois width
        x1 = aoi[4]+AOI_PADDING + width // 2 - max_size[0] // 2
        y1 = aoi[5]+AOI_PADDING+(aoi[4]-aoi[2])/75 + height // 2 - max_size[1] // 2 # add padding to height depending on the aois width
        image_draw.rectangle([x0, y0, x1, y1],
                              outline=outline_color, fill=None, width=2)
        return_aoi.append((aoi[1], x0, y0, x1, y1, outline_color))

    return return_aoi