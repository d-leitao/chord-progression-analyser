from copy import deepcopy


class ChordParser:

    def __init__(
            self, 
            chord_type_matches: list=None):
        if chord_type_matches is None:
            self.chord_type_matches = [  # (third, fifth, seventh)
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
                ('m', ('minor', 'perfect', None)),
                ('', ('major', 'perfect', None))  
            ]
        else:
            self.chord_type_matches = chord_type_matches
    
    def decompose_chord_str(self, chord_str):

        unprocessed = deepcopy(chord_str)  # copy

        # ROOT
        if len(unprocessed) == 1:  # white key major chords
            root = unprocessed[0]
            unprocessed = unprocessed[1:]
        else:
            if unprocessed[1] in ['b', '#']:
                root = unprocessed[0:2]
                unprocessed = unprocessed[2:]

        # BASS
        if '/' in unprocessed:  # bass different from root
            unprocessed_split = unprocessed.split('/')
            bass = unprocessed_split[1] # bass
            unprocessed = unprocessed_split[0] # rest

        else:  # bass same as root
            bass = root

        # by now, the root has been parsed out from unprocessed
        # CHORD
        # if no patterns are identified, default to major
        chord_type = ('major', 'perfect', None)
        for pattern, chord_hash in self.chord_type_matches:
            if pattern in unprocessed:
                chord_type = chord_hash

        return (bass, root, chord_type)


    # auxiliary (static) methods

    @staticmethod
    def standardize(integer): #fix numbers outside of 0-11
        while integer < 0:
                integer += 12
        
        return integer % 12

    @staticmethod
    def letterToNumber(letter):
        mapping = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4,
                'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9,
                'A#': 10, 'Bb': 10, 'B': 11}
        return mapping[letter]

    @staticmethod
    def numberToLetter(number):
        mapping = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#',
                7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}
        return mapping[number]