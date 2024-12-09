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

def condense_filesystem(fs):
    # a bit slow, but it works
    while None in fs:
        fs[fs.index(None)] = fs.pop()
    return fs

def checksum(fs):
    sum = 0
    for pos, id in enumerate(fs):
        sum += pos * id
    return sum

def main() -> None:
    disk_map = read_line('test_input')
    print(disk_map)
    fs = create_filesystem(disk_map)
    print(fs)
    condense_filesystem(fs)
    print(fs)
    print('fast version: ', read_condensed_fs(disk_map))
    print(checksum(fs))
    
if __name__ == "__main__":
    main()