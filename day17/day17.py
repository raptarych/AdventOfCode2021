def vizualize(values, max_y, x_range, y_range, idx, idy):
    print("Initial", idx, idy)
    print("Max Y", max_y)
    for y in range(max_y, y_range[0] - 1, -1):
        for x in range(0, x_range[1] + 1):
            if x == 0 and y == 0:
                c = 'S'
            elif (x, y) in values:
                c = '#'
            elif x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
                c = 'T'
            else:
                c = '.'
            print(c, sep='', end='')
        print('')


input_file = open('input.txt', mode='r')

line = input_file.read().strip()[13:]
(x_data, y_data) = line.split(', ')
x_range = [int(i) for i in x_data[2:].split('..')]
y_range = [int(i) for i in y_data[2:].split('..')]
print(x_range, y_range)


def simulate(idx, idy, x_range, y_range):
    values = [(0, 0)]
    max_y = y_range[1]
    dx, dy = idx, idy
    while True:
        (xi, yi) = (values[-1][0] + dx, values[-1][1] + dy)
        values.append((xi, yi))
        if yi > max_y:
            max_y = yi
        dx = dx - 1 if dx > 0 else 0
        dy = dy - 1
        if x_range[0] <= xi and yi <= y_range[1] or yi <= y_range[0]:
            break

    (x, y) = values[-1]
    if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
        #vizualize(values, max_y, x_range, y_range, idx, idy)
        return max_y
    return None


def part2():
    hits = set()
    max_y = 0
    for dy in range(-y_range[0], y_range[0]-1, -1):
        for dx in range(0, x_range[1]+1):
            max_hit_y = simulate(dx, dy, x_range, y_range)
            if max_hit_y is not None:
                if not max_y:
                    max_y = max_hit_y
                    print("part 1", max_y)
                hits.add((dx, dy))
    print("part 2", len(hits))


part2()
