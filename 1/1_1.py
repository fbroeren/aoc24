l1 = []
l2 = []

with open('input_1') as f:
    for line in f.readlines():
        n1, n2 = line.split()
        l1.append(int(n1))
        l2.append(int(n2))
l1.sort()
l2.sort()
distances = [abs(n1 - n2) for n1, n2 in zip(l1, l2)]
print(l1)
print(l2)
print(distances)
print(sum(distances))
