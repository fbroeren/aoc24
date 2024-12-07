from copy import deepcopy
import numpy as np
from time import time

def print_map(map):
    for line in map:
        print(line)
        
def move_guard(guard, map):
    # Would it be possible to immediately walk to the closest obstacle?
    i, j, dir = guard
    match dir:
        case 0:  # up
            new_pos = [i-1, j]
        case 1:  # right
            new_pos = [i, j+1]
        case 2:  # down
            new_pos = [i+1, j]
        case 3:  # left
            new_pos = [i, j-1]
    if (new_pos[0] > len(map[0])-1) or (new_pos[1] > len(map)-1) or (new_pos[0] < 0) or (new_pos[1] < 0):
        return False
    elif map[new_pos[0]][new_pos[1]] == '#':
        guard[2] = (guard[2] + 1) % 4 
        guard, map = move_guard(guard, map)
    else:
        map[new_pos[0]][new_pos[1]] = 'x'
        guard = [*new_pos, dir]
    return guard, map

def count_x(map):
    return sum([line.count('x') for line in map])

def patrol(guard, map):
    guard = deepcopy(guard)
    map = deepcopy(map)

    history = guard
    result = move_guard(guard, map)
    while result:
        guard, map = result
        if guard in history:
            return None
        history.append(guard)
        result = move_guard(guard, map)

    return guard, map 

def find_loop(guard, map):
    guard = deepcopy(guard)
    map = deepcopy(map)

    history = [guard]
    result = move_guard(guard, map)
    
    while result:
        guard, map = result
        if guard in history:
            return True
        if len(history) > len(map)**2:
            print('Long path')  # Not quite sure why I need this check. Hangs without
            return True
        history.append(guard)
        result = move_guard(guard, map)
    return False

with open('input') as f:
    map = [list(l.strip()) for l in f.readlines()]
    for i, line in enumerate(map):
        if '^' in line:
            j = line.index('^')
            guard = [i, j, 0]
            line[j] = 'x'
            break
    map = np.array(map)
        
_, patrol_map = patrol(guard, map)
print(patrol_map)

start_time = time()
count = 0
guard_start = deepcopy(guard)
# Tried to optimize a little, but it could definitely be faster
for i, j in zip(*np.where(patrol_map == 'x')):
    print(i, j)
    if not (i == guard_start[0] and j == guard_start[1]):
        new_map = deepcopy(map)
        new_map[i][j] = '#'
        if find_loop(guard, new_map):
            count += 1
end_time = time()
print(f'duration: {end_time - start_time:.5g}s')
print(count)

# Whoof, 370 seconds