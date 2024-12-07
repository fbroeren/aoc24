from operator import add, mul
from itertools import combinations_with_replacement, permutations, product
from multiprocessing import Pool

def check(result, components):
    result = int(result)
    operators = [add, mul]
    operator_combinations = product(operators, repeat=len(components) - 1)
#   The line above replaces the lines below, yielding an incredible efficiency boost
#     for c in combinations_with_replacement(operators, len(components) - 1):
#         perms = set(permutations(c))
#         for p in perms:
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
    with open('test_input') as f:
        lines = f.readlines()
        out = mp_pool.map(test_line, lines)
        print(sum(out))

if __name__ == "__main__":
    main()