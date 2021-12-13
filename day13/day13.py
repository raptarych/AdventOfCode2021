input_file = open('input.txt', mode='r').readlines()


def execute(part):
    points = set()
    for line in input_file:
        if '0' <= line[0] <= '9':
            p = map(int, line.split(','))
            points.add((next(p), next(p)))
        elif line[0:4] == 'fold':
            fold_data = line[11:].split('=')
            fold = int(fold_data[1])
            if fold_data[0] == 'y':
                points = {(p[0], min(p[1], fold * 2 - p[1])) for p in points}
            elif fold_data[0] == 'x':
                points = {(min(p[0], fold * 2 - p[0]), p[1]) for p in points}
            if part == 1:
                break

    if part == 1:
        print(len(points))
    if part == 2:
        for y in range(6):
            for x in range(40):
                print("#" if (x, y) in points else ' ', end='')
            print('')


execute(part=1)
execute(part=2)
