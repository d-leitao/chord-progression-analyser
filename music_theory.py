import utils


def predict_major_key(prog_chord_hashes):

    chords_notes_list = [chord_hash_to_notes(ch) for ch in prog_chord_hashes]
    
    raise NotImplementedError


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