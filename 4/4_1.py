import numpy as np

# The puzzle is always square

def find_in_line(line):
    n = 0
    for i in range(len(line) - 3):
        chars = line[i:i+4]
        if np.array_equal(np.array(['X', 'M', 'A', 'S']), chars):
            n += 1
        elif np.array_equal(np.array(['S', 'A', 'M', 'X']), chars):
            n += 1
    return n

def make_diagonal(puzzle):
    diag_1 = []
    n = len(puzzle)
    for i in range(3, n):
        diag_1.append([puzzle[i-j, j] for j in range(i + 1)])
    #     for j in range(i + 1):
    #         print(puzzle[i-j, j], end='')
    #     print('')
    for i in range(n-2, 2, -1):
        diag_1.append([puzzle[n - 1 - j, n - 1 - (i - j)] for j in range(i + 1)])
    #     for j in range(i + 1):
    #         print(puzzle[n-1-(j), n-1-(i-j)], end='')
    #     print('')
    return diag_1

def make_diagonal2(puzzle):
    diag_1 = []
    n = len(puzzle)
    for i in range(3, n):
        diag_1.append([puzzle[n-1-(i-j), j] for j in range(i + 1)])
    #     for j in range(i + 1):
    #         print(puzzle[i-j, j], end='')
    #     print('')
    for i in range(n-2, 2, -1):
        diag_1.append([puzzle[(n-1)-(n - 1 - j), n - 1 - (i - j)] for j in range(i + 1)])
    #     for j in range(i + 1):
    #         print(puzzle[n-1-(j), n-1-(i-j)], end='')
    #     print('')
    return diag_1

def find_horizontal(puzzle):
    return sum([find_in_line(line) for line in puzzle])

def find_vertical(puzzle) :
    return sum([find_in_line(line) for line in puzzle.T])

# Read in the file input as a numpy array
with open('input') as f:
    lines = f.readlines()
    lines = [list(x.strip()) for x in lines]
    puzzle = np.array(lines)
    
N = 0
N += find_horizontal(puzzle)
N += find_vertical(puzzle)
N += find_horizontal(make_diagonal(puzzle))
N += find_horizontal(make_diagonal2(puzzle))
print(N)