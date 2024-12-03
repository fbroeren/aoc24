import re

result = 0
with open('input') as f:
    for line in f.readlines():
        search = 'mul\(\d{1,3},\d{1,3}\)'
        muls = re.findall(search, line)
        for mul in muls:
            nrs = [int(x) for x in mul[4:-1].split(',')]
            result += nrs[0] * nrs[1]
print(result)
