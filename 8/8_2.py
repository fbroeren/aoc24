from copy import deepcopy
import numpy as np
from itertools import combinations

def dist(x1, x2):
    return np.linalg.norm(x2 - x1)

def check_dist(p1, p2, x):
    d1 = dist(p1, x)
    d2 = dist(p2, x)
    if (d2 * 2 == d1) or (d1 * 2 == d2):
        return True
    else:
        return False
    
def check_within_map(pos, map):
    return np.all(pos >= 0) and np.all(pos < len(map))

def main() -> None:
    with open('input') as f:
        lines = [list(x.strip()) for x in f.readlines()]
        map = np.array(lines)
    result_map = deepcopy(map)
    antenna_types = list(set(map[np.where(map != '.')]))
    print(antenna_types)
    for type in antenna_types:
        print(type)
        locations = np.argwhere(map == type)
        for pos1, pos2 in list(combinations(locations, 2)):
            dx = pos2 - pos1
            # get the lowest step in line with both nodes
            dx = dx // np.gcd(dx[0], dx[1], dtype=int)
            
            antinode1 = pos2 + dx
            while check_within_map(antinode1, map):
                result_map[antinode1[0], antinode1[1]] = '#'
                antinode1 += dx
                
            antinode2 = pos1 - dx
            while check_within_map(antinode2, map):
                result_map[antinode2[0], antinode2[1]] = '#'
                antinode2 -= dx
            
    print(result_map)
    # The code above does not include the antinodes located at the antenna's.
    # That is why we add these points to the count below.
    print(np.sum(result_map != '.', axis=(0, 1)))

    
if __name__ == "__main__":
    main()