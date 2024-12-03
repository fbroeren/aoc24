import numpy as np

def test_safe(levels):
    diff = np.diff(levels)
    if np.all(abs(diff) > 0) and np.all(abs(diff) <= 3) and (np.all(diff < 0) or np.all(diff > 0)):
        return True
    else:
        return False


safe = 0
with open('input') as f:
    for report in f.readlines():
        levels = report.split()
        levels = [int(x) for x in levels]
        print(levels)
        if test_safe(levels):
            print('SAFE')
            safe += 1
        else:
            for i in range(len(levels)):
                new_levels = levels[:i]
                new_levels.extend(levels[i+1:])
                if test_safe(new_levels):
                    print('SAFEish')
                    safe += 1
                    break
            else:
                print('unsafe')

            
print(safe)