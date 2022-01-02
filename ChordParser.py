from copy import deepcopy


class ChordParser:

    def __init__(self):
        pass

    @classmethod    
    def decompose_chord_str(cls, chord_str):

        unprocessed = deepcopy(chord_str)  # copy

        # ROOT
        if len(unprocessed) == 1:  # white key major chords
            map_root = unprocessed[0]
            unprocessed = unprocessed[1:]
        else:
            if unprocessed[1] in ['b', '#']:
                map_root = unprocessed[0:2]
                unprocessed = unprocessed[2:]

        # BASS
        if '/' in unprocessed:  # bass different from root
            unprocessed_split = unprocessed.split('/')
            map_bass = unprocessed_split[1] # bass
            unprocessed = unprocessed_split[0] # rest

        else:  # bass same as root
            map_bass = map_root

        # by now, the root has been parsed out from unprocessed
        # THIRD AND FIFTH
        map_third = 'major'  # the default
        map_fifth = 'perfect'  # the default
        map_seventh = 'None'
        extensions = unprocessed

        if len(unprocessed) == 0:
            map_third = 'major'
            extensions = ''

        elif unprocessed[0:3] == 'dim':
            map_third = 'minor'
            map_fifth = 'flat'
            extensions = unprocessed[3:]

        elif unprocessed[0:3] in ['maj', 'add']:
            map_third = 'major'
            extensions = unprocessed

        elif unprocessed[0:3] in ['m7M', 'mM7', 'm7+']: # all are used
            map_third = 'minor'
            map_seventh = 'major'
            extensions = unprocessed[3:]

        elif unprocessed[0:2] == 'm7':
            map_third = 'minor'
            map_seventh = 'minor'
            extensions = unprocessed[2:]

        elif unprocessed[0:2] in ['7M', 'M7', '7+']: #all are used
            map_seventh = 'major'
            extensions = unprocessed[2:]
        
        elif unprocessed[0] == 'm':
            map_third = 'minor'
            extensions = unprocessed[1:]

        elif unprocessed[0] == '9':
            map_seventh = 'minor'
        
        elif unprocessed[0] == '7':
            map_seventh = 'minor'
            extensions = unprocessed[1:]

        elif unprocessed[0] == '5':
            map_third = 'None'
            extensions = unprocessed[1:]

        elif unprocessed[0] == '4':
            map_third = 'sus4'
            extensions = unprocessed[1:]

        #capturing an augmented chord
        if extensions[0:4] == '(5+)':
            map_fifth = 'sharp'
            extensions = extensions[4:]

        map_chord = {'chord': chord, 'root': map_root, 'third': map_third, 
                    'fifth': map_fifth, 'seventh': map_seventh,
                    'bass': map_bass, 'extensions': extensions}

        return map_chord


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