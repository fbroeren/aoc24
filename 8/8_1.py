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
            print(pos1, pos2)
            dx = pos2 - pos1
            antinode1 = pos2 + dx
            antinode2 = pos1 - dx
            print(antinode1, antinode2)
            for an in [antinode1, antinode2]:
                if np.all(an >=0) and np.all(an < len(map)):
                    result_map[an[0], an[1]] = '#'
    print(result_map)
    print(np.sum(result_map == '#', axis=(0, 1)))

    
if __name__ == "__main__":
    main()