def read_line(filename):
    with open(filename) as f:
        result = f.readline()
    return result

def create_filesystem(disk_map):
    fs = []
    for n, i in enumerate(range(0, len(disk_map), 2)):
        print(n, disk_map[i])
        fs.extend([n]*int(disk_map[i]))
        if (i+1) < len(disk_map):
            fs.extend([None]*int(disk_map[i+1]))
    return fs

def clean_end(fs):
    while fs[-1] is None:
        fs.pop()

def condense_filesystem(fs):
    # it works! However, it seems like starting directly from the map could be more efficient
    look_at = max([x for x in fs if x])
    while look_at > 0:
        print(f"we will look at {look_at}, there are {fs.count(look_at)} instances")
        count = fs.count(look_at)
        start_ind = fs.index(look_at)
        for i, f in enumerate(fs[:start_ind]):
            if f is None:
                j = i + 1
                n = 1
                while fs[j] is None:
                    j += 1
                    n += 1
                if n >= count:
                    print(i, i+n)
                    for _ in range(count):
                        fs[fs.index(look_at)] = None
                    fs[i:i+count] = [look_at]*count
                    break
        clean_end(fs)
        look_at -= 1
    return fs

def checksum(fs):
    sum = 0
    for pos, id in enumerate(fs):
        if id:
            sum += pos * id
    return sum

def main() -> None:
    disk_map = read_line('input')
    print(disk_map)
    fs = create_filesystem(disk_map)
    print(fs)
    print(checksum(fs))
    condense_filesystem(fs)
    print(fs)
    print(checksum(fs))
    
if __name__ == "__main__":
    main()