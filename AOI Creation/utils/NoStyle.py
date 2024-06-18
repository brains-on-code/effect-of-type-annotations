from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

class NoStyle(Style):
    default_style = ""
    styles = {
        Comment:                'noitalic',
        Keyword:                'nobold',
        Name:                   '',
        Name.Function:          '',
        Name.Class:             'nobold',
        String:                 'bg:#eee #111'
    }
    
# .venv/lib/python3.11/site-packages/pygments/styles/no.py
# create this file there, then you can import it