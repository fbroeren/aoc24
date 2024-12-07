import time
import numpy as np

def average(list):
    return sum(list) / len(list)

def print_map(map):
    for line in map:
        print(line)
        
def move_guard(guard, map):
    i, j, dir = guard
    match dir:
        case 0:  # up
            new_pos = [i-1, j]
            look_at = (range(0, i), j)
        case 1:  # right
            new_pos = [i, j+1]
            look_at = (i, range(j, len(map[0])))
        case 2:  # down
            new_pos = [i+1, j]
            look_at = (range(i, len(map)), j)
        case 3:  # left
            new_pos = [i, j-1]
            look_at = (i, range(j)) 
    if sum(map[look_at] == '#') == 0:
        map[look_at] = 'x'
        return guard, map, False
    elif map[new_pos[0], new_pos[1]] == '#':
        guard[2] = (guard[2] + 1) % 4 
        guard, map, status = move_guard(guard, map)
    else:
        map[new_pos[0], new_pos[1]] = 'x'
        guard = [*new_pos, dir]
    return guard, map, True 

def count_x(map):
    return np.sum(map == 'x', axis=(0,1))

with open('input') as f:
    map = [list(l.strip()) for l in f.readlines()]
    for i, line in enumerate(map):
        if '^' in line:
            j = line.index('^')
            guard = [i, j, 0]
            line[j] = 'x'
            break
    map= np.array(map)

history = guard
result = move_guard(guard, map)
times = []
while result[-1]:
    start_time = time.time()
    guard, map, status = result
    if guard in history:
        break
    history.append(guard)
    result = move_guard(guard, map)
    end_time = time.time()
    times.append(end_time - start_time)
print(map)
print(count_x(map))
print(f'Total time: {sum(times):.3g}, {average(times):.3g} per iteration')