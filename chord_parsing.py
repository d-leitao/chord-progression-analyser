from copy import deepcopy


def parse_progression_str(
    progession_str: str,
    sep: str = ' - ',
    chord_type_matches: list = None) -> list:
    '''
    Transform string containing chord progression into list of chord hashes.
    Uses chord_parsing.parse_chord_str() for each chord.

    Args:
        progression_str (str): string containing the chord progression
        sep (str): separator between chords
        chord_type_matches (list): refer to chord_parsing.parse_chord_str()'s docstring
    Returns:
        list: list of chord_hash tuples (refer to chord_parsing.parse_chord_str()'s docstring)
    '''
    prog_input_list = progession_str.split(sep)
    chord_hash_list = [parse_chord_str(c) for c in prog_input_list]

    return chord_hash_list


def parse_chord_str(
        chord_str: str,
        chord_type_matches: list = None) -> tuple:
    '''
    Transform string containing chord into chord hash.
    Chord hash format: (bass, root, chord_type)

    Args:
        chord_str (str): string containing a chord
        chord_type_matches (list): list of tuples mapping pattern to chord_type
            pattern (str): commonly used musical notation excluding bass and root indications
            chord_type (tuple): (third, fifth, seventh)
                third (str): one of {sus2, minor, sus4, major, None}
                fifth (str): one of {dim, perfect, aug, None}
                seventh (str): one of {minor, major, None}
    Returns:
        tuple: chord_hash tuple containing bass, root and chord_type
            bass (int): integer notation (C-B -> 0-11)
            root (int): integer notation (C-B -> 0-11)
            chord_type (tuple): (third, fifth, seventh)
                third (str): one of {sus2, minor, sus4, major, None}
                fifth (str): one of {dim, perfect, aug, None}
                seventh (str): one of {minor, major, None}
    '''
    if chord_type_matches is None:
        # format: (third, fifth, seventh)
        # ignoring extensions beyond the seventh
        chord_type_matches = [
            ('sus2', ('sus2', 'perfect', None)),
            ('sus4', ('sus4', 'perfect', None)),
            ('dim7', ('minor', 'dim', 'minor')),
            ('dim', ('minor', 'dim', None)),
            ('aug7', ('major', 'aug', 'minor')),
            ('aug', ('major', 'aug', None)),
            ('maj7', ('major', 'perfect', 'major')),
            ('m7', ('minor', 'perfect', 'minor')),
            ('mM7', ('minor',  'perfect', 'major')),
            ('7', ('major', 'perfect', 'minor')),
            ('5', (None, 'perfect', None))
            ('m', ('minor', 'perfect', None)),
            ('', ('major', 'perfect', None))
        ]

    unprocessed = deepcopy(chord_str)  # copy

    # ROOT
    if len(unprocessed) == 1:  # white key major chords
        root_str = unprocessed[0]
        unprocessed = unprocessed[1:]
    else:
        if unprocessed[1] in ['b', '#']:
            root_str = unprocessed[0:2]
            unprocessed = unprocessed[2:]
        else:
            root_str = unprocessed[0]
            unprocessed = unprocessed[1:]

    # BASS
    if '/' in unprocessed:  # bass different from root
        unprocessed_split = unprocessed.split('/')
        bass_str = unprocessed_split[1] # bass
        unprocessed = unprocessed_split[0] # rest

    else:  # bass same as root
        bass_str = root_str

    # by now, the root has been parsed out from unprocessed
    # CHORD
    # if no patterns are identified, default to major
    chord_type = ('major', 'perfect', None)
    for patt, c_type in chord_type_matches:
        if patt in unprocessed:
            chord_type = c_type

    # convert note letters to integer notation
    bass = letterToInt(bass_str)
    root = letterToInt(root_str)

    return (bass, root, chord_type)


def letterToInt(letter_note: str) -> int:
    '''Map note letter to integer notation (C-B -> 0-11).'''
    mapping = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4,
            'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9,
            'A#': 10, 'Bb': 10, 'B': 11}
    int_note = standardize(mapping[letter_note])
    return int_note


def intToLetter(int_note: int) -> str:
    '''Map integer notation to note letter (0-11 -> C-B).'''
    mapping = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#',
            7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}
    letter_note = standardize(mapping[int_note])
    return letter_note


def standardize(unstd_int_note: int) -> int:
    '''Standardize values outside of integer notation range (0-11).'''
    int_note = unstd_int_note
    while int_note < 0:
        int_note += 12
    int_note = int_note % 12
    return int_note
