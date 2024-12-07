from operator import add, mul
from itertools import combinations_with_replacement, permutations, product
from multiprocessing import Pool

def concat(i, j):
    # We only need to add one extra operator to the list
    return i * (10 ** len(str(j))) + j

def check(result, components):
    result = int(result)
    operators = [add, mul, concat]
    operator_combinations = product(operators, repeat=len(components) - 1)
    for p in operator_combinations:
            temp_result = components[0]
            for op, comp in zip(p, components[1:]):
                temp_result = op(temp_result, comp)
            if temp_result == result:
                return True
    else:
        return False
    
def test_line(line: str):
    result, rest = line.split(':')
    components = [int(x) for x in rest.split()]
    if check(result, components):
        return int(result)
    else:
        return 0

def main():
    mp_pool = Pool(4)
    with open('input') as f:
        lines = f.readlines()
        out = mp_pool.map(test_line, lines)
        print(sum(out))

if __name__ == "__main__":
    main()