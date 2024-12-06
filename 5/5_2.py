rules = []
updates = []

def isSorted(l):
    ''' Check if all items are increasing '''
    return all(l[i] <= l[i+1] for i in range(len(l) - 1))

def checkSorted(line, rules):
    prev = []
    for n in line:
        for r in rules:
            if r[1] == n:
                if (r[0] in line) and (r[0] not in prev):
                    return False
        prev.append(n)
    return True

def sort(line, rules):
    for a, b in rules:
        if (a in line) and (b in line):
            ia = line.index(a)
            ib = line.index(b)
            if ib < ia:
                line[ib], line[ia] = line[ia], line[ib]
    return line

def middle(line):
    return line[int(len(line) / 2)]

with open('input') as f:
    check = False
    for line in f:
        if not line.strip():
            check = True
        elif not check:
            rules.append([int(x) for x in line.strip().split('|')])
        else:
            updates.append([int(x) for x in line.strip().split(',')])

middle_numbers = []
sorted_numbers = []
for u in updates:
    if checkSorted(u, rules):
        middle_numbers.append(middle(u))
    else:
        while not checkSorted(u, rules):
            u = sort(u, rules)
        sorted_numbers.append(middle(u))

print(f'sum: {sum(sorted_numbers)}')
