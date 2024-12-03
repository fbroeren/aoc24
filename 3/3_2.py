import re

result = 0
do = True
with open('input') as f:
    for line in f.readlines():
        # Split on valid muls, dos and don'ts. Remove all invalid input
        search = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
        muls = re.findall(search, line)
        # Go through all of the list, toggling the "do" variable and acting accordingly
        for mul in muls:
            if mul == "do()":
                do = True
            elif mul == "don't()":
                do = False
            elif do:
                nrs = [int(x) for x in mul[4:-1].split(',')]
                result += nrs[0] * nrs[1]
print(result)
