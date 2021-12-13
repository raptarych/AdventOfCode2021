input_file = open('input.txt', mode='r').readlines()
points = []
max_x,max_y = 0,0


def print_points():
    print('')
    for y in range(6):
        for x in range(40):
            if (x,y) in points:
                print("#", end='')
            else:
                print('.', end='')
        print('')
    print('')


for line in input_file:
    if line[0] == 'f':
        fold_data = line[11:].split('=')
        if fold_data[0] == 'y':
            fold = int(fold_data[1])
            points = [(p[0], min(p[1], fold*2 - p[1])) for p in points]
        elif fold_data[0] == 'x':
            fold = int(fold_data[1])
            points = [(min(p[0], fold*2 - p[0]), p[1]) for p in points]
    elif '0' <= line[0] <= '9':
        p = [*map(int, line.split(','))]
        max_x = max(max_x, p[0])
        max_y = max(max_y, p[1])
        points.append((p[0],p[1]))

print(len(set(points)))
print(max_x, "x", max_y)
print_points()