from collections import defaultdict
from queue import PriorityQueue

game_map = [x.rstrip('\n') for x in open('input.txt', mode='r').readlines()]
game_map = [[int(j) for j in i] for i in game_map]


def print_map(start, visited, game_map):
    print('\n')
    for y in range(len(game_map)):
        for x in range(len(game_map[0])):
            c = '.'
            if (x, y) == start:
                c = 'x'
            elif (x, y) in visited:
                c = '#'
            print(c, sep='', end='')
        print('')


def search(game_map):
    start = (0, 0)
    end = (len(game_map[0])-1, len(game_map)-1)

    paths = PriorityQueue()
    paths.put((0, [start]))
    cache = defaultdict(int)
    results = []
    complexity = 0
    while paths:
        complexity+=1
        (l, path) = paths.get()
        (x, y) = path[-1]

        neighbours = [(x+dx, y+dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]
        neighbours = [(x, y) for x, y in neighbours if 0 <= x < len(game_map) and 0 <= y < len(game_map) and (x, y) not in path]
        for n in neighbours:
            new_l = l + game_map[n[1]][n[0]]
            if n not in cache or cache[n] > new_l:
                cache[n] = new_l
                if n == end:
                    results.append(new_l)
                    #print_map(n, path, game_map)
                    print(new_l, "complexity", complexity)
                    return
                new_path = path.copy()
                new_path.append(n)
                paths.put((new_l, new_path))


def part1():
    search(game_map)


def part2():
    new_data = []
    max_y = len(game_map)
    max_x = len(game_map[0])
    for y in range(len(game_map) * 5):
        row = []
        for x in range(len(game_map[0]) * 5):
            c = game_map[y % max_y][x % max_x] + int(y / max_y) + int(x / max_x)
            c = (c - 1) % 9 + 1
            row.append(c)
        new_data.append(row)
    search(new_data)


part1()
# works, but pretty slow tho :(
part2()