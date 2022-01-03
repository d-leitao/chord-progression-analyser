import chord_parsing as cp

prog_str = 'Fmaj7/C - C'

progression = cp.parse_progression_str(prog_str)
print(progression)