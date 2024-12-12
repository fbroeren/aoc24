from icecream import ic
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

def main() -> None:
    start = time.time()
    stones = read_input('input')
    ic(stones)
    for i in range(75):
        new_stones = []
        for stone in stones:
            new_stones.extend(apply_rules(stone))
        stones = new_stones
    end = time.time()
    ic(len(stones))
    ic(end - start)
if __name__ == "__main__":
    main()