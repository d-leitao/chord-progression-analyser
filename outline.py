# representations

string = 'Fmaj7/C'
reading = {
    'bass': 'C',
    'tonic': 'F',
    'third': 'major',
    'fifth': 'perfect',
    'seventh': 'maj7'
}
absolute = {
    'bass': 0,
    'tonic': 5,
    'third': }
relative = [2, [0, 4, 7, 11]]

# backend functions

class Chord:
    pass

class Progression:
    pass

def str_to_chord():
    '''
    Transforms chord in string format into Chord object
    (e.g. 'Fmaj7/C' -> Chord())
    '''

def str_to_progression():
    '''
    Transforms progression in string format into Progression object
    (e.g. 'C - Fmaj7/C' -> Progression())
    '''

# UI functions

def insert_progression():
    pass