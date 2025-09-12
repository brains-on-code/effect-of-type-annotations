import pprint

import numpy

# TODO: describe and document what this file exactly does
import config


def participant_fixation_saccades(participant_df):
    # post-computations: fixation/saccade counts, fix/sac per minute
    print('--> found fixations: ', len(participant_df['fixations']))
    print('--> found saccades: ', len(participant_df['saccades']))

    fixations_per_second = len(participant_df['fixations']) / (participant_df['experiment_runtime'] / 1000)
    saccades_per_second = len(participant_df['saccades']) / (participant_df['experiment_runtime'] / 1000)

    print('--> roughly fixations/sec: ', round(fixations_per_second, 2))
    print('--> roughly saccades/sec: ', round(saccades_per_second, 2))

    # fixation length in time, average saccade distance
    fixation_length: float = numpy.mean([fixation['TimeLength'] for fixation in participant_df['fixations']])
    saccade_distance: float = numpy.mean([saccade['Distance'] for saccade in participant_df['saccades']])

    print('--> roughly fixation length in msec: ', round(fixation_length, 2))
    print('--> roughly saccade distance in pixel: ', round(saccade_distance, 2))

    participant_df['results']['FixationsPerSecond'] = fixations_per_second
    participant_df['results']['FixationLength'] = fixation_length
    participant_df['results']['SaccadesPerSecond'] = saccades_per_second
    participant_df['results']['SaccadeDistance'] = saccade_distance

    return participant_df


def participant_fixation_saccades_task(participant_df):
    # get all unique snippets
    try:
        snippets = participant_df['gaze_data'][config.KEYWORD_SNIPPET].unique()
    except Exception as e:
        pprint.pprint(participant_df['gaze_data'])
        raise e

    # todo maybe move this into preprocessing
    for snippet in snippets:
        # collect fixation/saccade data for each snippet
        fixations = []
        saccades = []

        for fixation in participant_df['fixations']:
            if snippet == fixation[config.KEYWORD_SNIPPET]:
                fixations.append(fixation)

        for saccade in participant_df['saccades']:
            if snippet == saccade[config.KEYWORD_SNIPPET]:
                saccades.append(saccade)

        # todo change done by Nils
        task_time = participant_df['gaze_data'].loc[participant_df['gaze_data'][config.KEYWORD_SNIPPET] == snippet, ['ExperimentTime']].iloc[[0, -1]].diff().iat[-1, 0]
        # task_time = participant_df['gaze_data'].loc[participant_df['gaze_data'][config.KEYWORD_SNIPPET] == snippet, ['ExperimentTime']].iloc[[0, -1]].diff().iloc[-1][0]

        # compute for each snippet: fixations/saccades per second and length/distance
        fixations_per_second = len(fixations) / (task_time / 1000)
        saccades_per_second = len(saccades) / (task_time / 1000)

        fixation_length: float = numpy.mean([fixation['TimeLength'] for fixation in fixations])
        saccade_distance: float = numpy.mean([saccade['Distance'] for saccade in saccades])

        # store results
        participant_df['results']['ByNoTA'][snippet] = {}
        participant_df['results']['ByNoTA'][snippet]['FixationsPerSecond'] = fixations_per_second
        participant_df['results']['ByNoTA'][snippet]['FixationLength'] = fixation_length
        participant_df['results']['ByNoTA'][snippet]['SaccadesPerSecond'] = saccades_per_second
        participant_df['results']['ByNoTA'][snippet]['SaccadeDistance'] = saccade_distance

    return participant_df


def participant_fixation_saccades_TA(participant_df):
    def calculate_and_store_results(participant_df, condition, fixations, saccades, task_time):
        # compute for each condition: fixations/saccades per second and length/distance
        fixations_per_second = len(fixations) / (task_time / 1000)
        saccades_per_second = len(saccades) / (task_time / 1000)
        fixation_length: float = numpy.mean([fixation['TimeLength'] for fixation in fixations])
        saccade_distance: float = numpy.mean([saccade['Distance'] for saccade in saccades])

        # store results
        if not 'ByTA' in participant_df['results']:
            participant_df['results']['ByTA'] = {}

        participant_df['results']['ByTA'][condition] = {}
        participant_df['results']['ByTA'][condition]['FixationsPerSecond'] = fixations_per_second
        participant_df['results']['ByTA'][condition]['FixationLength'] = fixation_length
        participant_df['results']['ByTA'][condition]['SaccadesPerSecond'] = saccades_per_second
        participant_df['results']['ByTA'][condition]['SaccadeDistance'] = saccade_distance

        return participant_df

    # get all unique snippets
    snippets = participant_df['gaze_data'][config.KEYWORD_SNIPPET].unique()

    # collect fixation/saccade data for each condition (non/scrambled)
    fixations = []
    fixations_TA = []
    saccades = []
    saccades_TA = []
    task_time = 0
    task_time_TA = 0

    # print(f'PARTICIPANT_DF:\n{participant_df["fixations"]}')

    # todo maybe move this into preprocessing
    for snippet in snippets:

        for fixation in participant_df['fixations']:
            if snippet == fixation[config.KEYWORD_SNIPPET]:
                if snippet[-1] == 'T':
                    fixations_TA.append(fixation)
                else:
                    fixations.append(fixation)
        
        for saccade in participant_df['saccades']:
            if snippet == saccade[config.KEYWORD_SNIPPET]:
                if snippet[-1] == 'T':
                    saccades_TA.append(saccade)
                else:
                    saccades.append(saccade)

        # todo Nils also changed this line
        snippet_time = participant_df['gaze_data'].loc[participant_df['gaze_data'][config.KEYWORD_SNIPPET] == snippet, ['ExperimentTime']].iloc[[0, -1]].diff().iat[-1, 0]

        if snippet[-1] == 'T':
            task_time_TA += snippet_time
        else:
            task_time += snippet_time

    participant_df = calculate_and_store_results(participant_df, 'normal', fixations, saccades, task_time)
    participant_df = calculate_and_store_results(participant_df, 'withTA', fixations_TA, saccades_TA, task_time_TA)

    return participant_df




