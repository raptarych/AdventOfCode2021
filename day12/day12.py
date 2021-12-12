from collections import Counter

input_file = open('input.txt', mode='r')
cave_map = [i.split('-') for i in input_file.read().splitlines()]


def part1():
    paths = [['start']]
    answer = []

    while len(paths) > 0:
        path = paths.pop()
        last_cave = path[len(path) - 1]
        next_paths = [i for i in cave_map if last_cave in i]
        for road in next_paths:
            next_cave = [i for i in road if i != last_cave][0]
            if next_cave == 'start':
                continue
            new_path = path.copy();
            new_path.append(next_cave)

            is_valid = True
            small_caves = Counter([i for i in new_path if i != 'start' and i != 'end' and i.lower() == i])
            if any([v > 1 for k, v in small_caves.items()]):
                is_valid = False

            if is_valid:
                if next_cave == 'end':
                    answer.append(new_path)
                else:
                    paths.append(new_path)

    print("Part1", len(answer))


def part2():
    paths = [['start']]
    answer = []

    def validate_path(path):
        small_caves = Counter([i for i in path if i != 'start' and i != 'end' and i.lower() == i])

        if any([v > 2 for k, v in small_caves.items()]):
            return False
        else:
            small_caves = Counter([v for _, v in small_caves.items()])
            if small_caves[2] > 1:
                return False
        return True

    while len(paths) > 0:
        path = paths.pop()
        last_cave = path[len(path) - 1]
        next_paths = [i for i in cave_map if last_cave in i]
        for road in next_paths:
            next_cave = [i for i in road if i != last_cave][0]
            if next_cave == 'start':
                continue
            new_path = path.copy();
            new_path.append(next_cave)

            is_valid = validate_path(new_path)

            if is_valid:
                if next_cave == 'end':
                    answer.append(new_path)
                else:
                    paths.append(new_path)

            #print(paths)
    print("Part2", len(answer))


part1()
part2()
