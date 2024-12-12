from icecream import ic
from multiprocessing import Pool
import time

def read_input(filename):
    with open(filename) as f:
        line = f.readline()
        stones = [int(x) for x in line.split()]
    return stones

def apply_rules(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        l = len(str(stone))
        return [int(str(stone)[:l//2]), int(str(stone)[l//2:])]
    else:
        return [stone * 2024]
    
def flatten(xss):
    return [x for xs in xss for x in xs]

def main() -> None:
    start = time.time()
    stones = read_input('input')
    ic(stones)
    for i in range(75):
        mp_pool = Pool(processes=4)
        out = mp_pool.map(apply_rules, stones)
        new_stones = flatten(out)
        stones = new_stones
    end = time.time()
    ic(len(stones))
    ic(end - start)

if __name__ == "__main__":
    main()