import numpy as np
from icecream import ic

def read_map(filename):
    with open(filename) as f:
        map = [[int(x) for x in list(line.strip())] for line in f.readlines()]
    return np.array(map)

def print_map(map):
    for line in map:
        print(' '.join([str(x) for x in line]))
            
def find_trailheads(map):
    return np.array(np.where(map == 0)).T

def adjacent(map, pos):
    result = []
    i, j = pos
    if i > 0:
        result.append((i-1, j))
    if j >=0:
        result.append((i, j-1))
    if i < len(map[0]) - 1:
        result.append((i+1, j))
    if j < len(map) - 1:
        result.append((i, j+1))
    return [tuple(x) for x in result if np.all(map[x[0], x[1]] == map[i, j] + 1)]

def BFS(map, start):
    visited = np.full_like(map, False)
    queue = []
    
    queue.append(start)
    visited[start[0], start[1]] = True
    
    while queue:
        s = queue.pop(0)
        
        for i in adjacent(map, s):
            if not visited[i[0], i[1]]:
                queue.append(i)
                visited[i[0], i[1]] = True
    return(visited)

def DFSUtil(map, v, visited):
    visited.append(v)
    ic(v, map[v[0], v[1]])
    
    for n in adjacent(map, v):
        DFSUtil(map, n, visited)
    

def DFS(map, start):
    visited = []
    DFSUtil(map, start, visited)
    return visited


def trailhead_score(map, th):
    return np.sum(map * BFS(map, th) == 9, axis=(0, 1))
    
def main() -> None:
    map = read_map('input')
    trailheads = find_trailheads(map)
    scores = []
    for th in trailheads:
        visited = DFS(map, th)
        visited_numbers = [map[v[0], v[1]] for v in visited]
        scores.append(sum([x == 9 for x in visited_numbers]))
    ic(scores)
    ic(sum(scores))
        


if __name__ == "__main__":
    main()