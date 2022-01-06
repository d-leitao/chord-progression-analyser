import utils


def predict_major_key(prog_chord_hashes):
    """
    Predict relative major of the progression's key.
    Returns key's root in integer notation.
    Predicts key with most relies on percentage of notes contained in each possible key.

    """
    
    chords_notes_list = [chord_hash_to_notes(ch) for ch in prog_chord_hashes]
    all_notes = [n for chord_notes in chords_notes_list for n in chord_notes]

    n_notes = len(all_notes)
    major_key_intervals = [0, 2, 4, 5, 7, 9, 11]
    key_scores = dict()
    for possible_root in range(0, 11+1):
        possible_key_notes = [possible_root + i for i in major_key_intervals]
        n_notes_in_key = len([note for note in all_notes if note in possible_key_notes])
        key_scores[possible_root] = n_notes_in_key / n_notes

    best_keys = [k for k, v in key_scores if v == max(key_scores.values())]

    if len(best_keys) == 1:
        best_key = best_keys[0]
    else:
        if prog_chord_hashes[0][1] in best_keys:
            best_key = prog_chord_hashes[0][1]  # root of the first chord
        elif prog_chord_hashes[-1][1] in best_keys:
            best_key = prog_chord_hashes[-1][1]  # root of the last chord
        else:
            best_key = best_keys[0]  # unprincipled
    
    return best_key


def chord_hash_to_notes(chord_hash):
    """
    Transform chord_hash to list of notes (absolutes in integer notation).
    Refer to parse_chord_str()'s docstring for the format of chord_hash.
    """
    tone_to_interval_mappings = {
        'third': {'sus2': 2, 'minor': 3, 'sus4': 5, 'major': 7},
        'fifth': {'dim': 6, 'perfect': 7, 'aug': 8},
        'seventh': {'minor': 10, 'major': 11}
    }
    bass, root, chord_description = chord_hash
    other_notes = [
        utils.standardize(root + tone_to_interval_mappings[d])
        for d in chord_description
        if d is not None
    ]
    notes_list = [bass, root, *other_notes]
    
    return notes_list