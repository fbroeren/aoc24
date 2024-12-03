import numpy as np

safe = 0
with open('input') as f:
    for report in f.readlines():
        levels = report.split()
        levels = [int(x) for x in levels]
        print(levels)
        diff = np.diff(levels)
        print(diff)
        if np.all(abs(diff) > 0) and np.all(abs(diff) <= 3) and (np.all(diff < 0) or np.all(diff > 0)):
            print('SAFE')
            safe += 1
        else:
            print('Unsafe')
            
print(safe)