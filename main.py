import csv
import pandas as pd

import chord_parsing as cp
import music_theory as mt


def main():
    """
    Function for Chord Progression Analyser's main app.
    """
    FILEPATH = 'data/progressions.csv'
    records = pd.read_csv(FILEPATH, sep=',')

    main_input = main_menu()
    if main_input == 1:
        analyse_new_progression(records)
    elif main_input == 2:
        pass

    records.to_csv(FILEPATH, sep=', ', quoting=csv.QUOTE_ALL, quotechar='"')


def main_menu():
    """
    Main menu displayer & input manager.
    """
    options = {
        1: 'Analyse new progression',
        2: 'Analyse old progression'}
    
    for k, v in options:
        print(f'{k} - {v}')

    main_input = input('> ')

    if main_input not in options.keys():
        raise ValueError(f'Valid options: {", ".join(list(options.keys()))}')

    return main_input


def analyse_new_progression(records: pd.DataFrame):

    sep = '-'
    print(f'Insert progression (sep="{sep}"):')
    progression_input = input('> ')
    progression_chord_hashes = cp.parse_progression_str(
        progression_str=progression_input,
        sep=sep)

    major_key = mt.predict_major_key(progression_chord_hashes)
    raise NotImplementedError


if __name__ == '__main__':
    main()