# playing-craps.py
"""Roll TWO six-sided dice six thousand times."""

import random

# face frequency counters
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0
frequency7 = 0
frequency8 = 0
frequency9 = 0
frequency10 = 0
frequency11 = 0
frequency12 = 0

trials = 6_000_000

# simulate rolls
for roll in range(trials):
    face = random.randrange(1, 7) + random.randrange(1, 7)
    
    # increment appropriate face counter
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 1
    elif face == 7:
        frequency7 += 1
    elif face == 8:
        frequency8 += 1
    elif face == 9:
        frequency9 += 1
    elif face == 10:
        frequency10 += 1
    elif face == 11:
        frequency11 += 1
    elif face == 12:
        frequency12 += 1
        
print(f'Face{"Frequency":>13}')
print(f'Face{1:4>}{frequency1:>13}')
print(f'Face{2:4>}{frequency2:>13}')
print(f'Face{3:4>}{frequency3:>13}')
print(f'Face{4:4>}{frequency4:>13}')
print(f'Face{5:4>}{frequency5:>13}')
print(f'Face{6:4>}{frequency6:>13}')
print(f'Face{7:4>}{frequency7:>13}')
print(f'Face{8:4>}{frequency8:>13}')
print(f'Face{9:4>}{frequency9:>13}')
print(f'Face{10:4>}{frequency10:>13}')
print(f'Face{11:4>}{frequency11:>13}')
print(f'Face{12:4>}{frequency12:>13}')

craps = frequency2 + frequency3 + frequency12
win = frequency7 + frequency11
print('Craps:', craps/trials)
print('Wins:', win/trials)

