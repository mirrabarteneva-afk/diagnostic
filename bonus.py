def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as name:
            name = [x.rstrip() for x in name]
            print(name)
            return len(name)
    except FileNotFoundError:
        return -1

print(count_lines("data.txt"))
print(count_lines("nope.txt"))