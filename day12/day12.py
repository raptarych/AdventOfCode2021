input_file = open('input.txt', mode='r')
cave_system = [i.split('-') for i in input_file.read().splitlines()]
cave_map = {j: [] for i in cave_system for j in i}
for road in cave_system:
    cave_map[road[0]].append(road[1])
    cave_map[road[1]].append(road[0])


def execute(part):
    paths = [['start']]
    answer = []

    def better_validate_path(path, new_value):
        if new_value == 'end' or new_value[0].lower() != new_value[0]:
            return True
        path_set = {i for i in path if i[0].lower() == i[0] and i != 'start'}
        if new_value not in path_set:
            return True
        if part == 1:
            if new_value in path_set:
                return False
        elif part == 2:
            counts = [path.count(i) for i in path_set]
            if 2 in counts:
                return False

        return True
    processed_paths = 0
    while len(paths) > 0:
        processed_paths += 1
        path = paths.pop()
        last_cave = path[len(path) - 1]
        next_paths = cave_map[last_cave]
        for next_cave in next_paths:
            if next_cave == 'start':
                continue

            is_valid = better_validate_path(path, next_cave)
            if not is_valid:
                continue
            new_path = path.copy()
            new_path.append(next_cave)

            if is_valid:
                if next_cave == 'end':
                    answer.append(new_path)
                else:
                    paths.append(new_path)

        #print(paths)
    print("Part", part, len(answer))
    print("Processed paths", processed_paths)


execute(part=1)
execute(part=2)
