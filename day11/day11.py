def make_step(octopuses):
    step_zeros = 0
    zeros = []
    for y in range(len(octopuses)):
        for x in range(len(octopuses)):
            octopuses[y][x] = (octopuses[y][x] + 1) % 10;
            if octopuses[y][x] == 0:
                zeros.append((x, y))
                step_zeros += 1

    while len(zeros) > 0:
        new_zeros = []
        for (x, y) in zeros:
            neighbours_indices = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
            neighbours = [(x+dx, y+dy) for dx,dy in neighbours_indices
                          if 0 <= x+dx < len(octopuses[0])
                          and 0 <= y+dy < len(octopuses[0])
                          and octopuses[y+dy][x+dx] != 0]
            for n in neighbours:
                (dx, dy) = n
                octopuses[dy][dx] = (octopuses[dy][dx] + 1) % 10
                if octopuses[dy][dx] == 0:
                    new_zeros.append((dx, dy))
                    step_zeros += 1
        zeros = new_zeros
    return octopuses
