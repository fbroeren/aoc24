l1 = []
l2 = []

with open('input_1') as f:
    for line in f.readlines():
        n1, n2 = line.split()
        l1.append(int(n1))
        l2.append(int(n2))

similarity = 0
for n in l1:
    similarity += n * sum([x == n for x in l2])
    
print(similarity)