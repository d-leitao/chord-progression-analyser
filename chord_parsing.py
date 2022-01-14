from copy import deepcopy

import utils


def parse_progression_str(
    progression_str: str,
    chord_type_matches: list = None,
    sep: str = '-') -> list:
    """
    Transform string containing chord progression into list of chord hashes.
    Uses chord_parsing.parse_chord_str() for each chord.

    Args:
        progression_str (str): string containing the chord progression
        sep (str): separator between chords
        chord_type_matches (list): refer to chord_parsing.parse_chord_str()'s docstring
    Returns:
        list: list of chord_hash tuples (refer to chord_parsing.parse_chord_str()'s docstring)
    """
    prog_input_list = progression_str.split(sep)
    prog_chord_hashes = [parse_chord_str(c, chord_type_matches) for c in prog_input_list]

    return prog_chord_hashes


def parse_chord_str(
        chord_str: str,
        chord_description_mappings: list = None) -> tuple:
    """
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
            bass (int): integer notation (C-B -> 0-11, refer to utils.letterToInt())
            root (int): integer notation (C-B -> 0-11, refer to utils.letterToInt())
            chord_type (tuple): (third, fifth, seventh)
                third (str): one of {sus2, minor, sus4, major, None}
                fifth (str): one of {dim, perfect, aug, None}
                seventh (str): one of {minor, major, None}
    """
    if chord_description_mappings is None:
        # format: (third, fifth, seventh)
        # ignoring extensions beyond the seventh
        chord_description_mappings = [
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
            ('5', (None, 'perfect', None)),
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
    for patt, c_tone_descr in chord_description_mappings:
        if patt in unprocessed:
            chord_type = c_tone_descr

    # convert note letters to integer notation
    bass = utils.letterToInt(bass_str)
    root = utils.letterToInt(root_str)

    chord_hash = (bass, root, chord_type) 

    return chord_hash

