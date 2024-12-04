import numpy as np

# Read in the file input as a numpy array
with open('input') as f:
    lines = f.readlines()
    lines = [list(x.strip()) for x in lines]
    puzzle = np.array(lines)
    
n = len(puzzle)
N = 0
# scan over every 3x3 block
for i in range(n-2):
    for j in range(n-2):
        block = puzzle[i:i+3, j:j+3]
        # Not quite happy about this check, but it works
        if block[1,1] == 'A':
            if (block[0, 0] == 'M' and block[2, 2] == 'S') or (block[2, 2] == 'M' and block[0, 0] == 'S'):
                if (block[0, 2] == 'M' and block[2, 0] == 'S') or (block[2, 0] == 'M' and block[0, 2] == 'S'):
                    N += 1
print(N)