import itertools
from collections import Counter, defaultdict

import numpy

input_file = open('input.txt', mode='r')

data = []
scanner = set()
while True:
    line = input_file.readline()
    if not line:
        break
    line = line.strip()
    if line[:3] == '---':
        if len(scanner) > 1:
            data.append(scanner)
        scanner = set()
    elif line:
        (x, y, z) = map(int, line.split(','))
        scanner.add((x, y, z))

if len(scanner) > 1:
    data.append(scanner)


def get_beacon(s1, s2, permutation):
    min_diff = (0, 0, 0)
    min_unique_values = {(x, y, z) for x, y, z in numpy.concatenate((s1, s2))}
    for r1 in s1:
        for r2 in s2:
            diff = (r2 - r1)
            diff_matrix = numpy.tile(diff, (len(s2), 1))
            moved_s2 = s2 - diff_matrix
            unique_values = {(x, y, z) for x, y, z in numpy.concatenate((s1, moved_s2))}
            # duplicates_counter = Counter([(x, y, z) for x, y, z in numpy.concatenate((s1, moved_s2))])
            # duplicates = [k for k, v in duplicates_counter.items() if v > 1]
            if len(unique_values) < len(min_unique_values):
                min_unique_values = unique_values
                min_diff = diff
    # print("for", permutation, "result", len(min_unique_values), "with diff", min_diff)
    return min_unique_values, min_diff


def sort_r(r):
    return r[numpy.argsort(r[:, 0])]


def swap(r, a1, a2, a3):
    r2 = r
    r2 = numpy.rot90(r2, axes=(1, 0))
    r3 = numpy.array([
        r2[abs(a1) - 1] * (-1 if a1 < 0 else 1),
        r2[abs(a2) - 1] * (-1 if a2 < 0 else 1),
        r2[abs(a3) - 1] * (-1 if a3 < 0 else 1),
    ])
    r2 = numpy.rot90(r3, axes=(0, 1))
    return r2


permutations_set = [*itertools.permutations([1, 2, 3, -1, -2, -3], 3)]
permutations_set = {i for i in permutations_set if len(set(map(abs, i))) == 3}


def get_fingerprint(s1):
    # s1 = sorted(list(s1), key=lambda a: abs(a[0]) + abs(a[1]) + abs(a[2]))
    combinations = itertools.combinations(s1, 2)
    result = {int(numpy.linalg.norm(x2 - x1) * 1000): [x1, x2] for x1, x2 in combinations}
    return result


def set_to_array(s):
    return numpy.array([numpy.array(i) for i in s])


def part1(data):
    solved = defaultdict()
    solved[0] = data[0]
    while True:
        unsolved = [i for i in range(len(data)) if i not in solved.keys()]
        if not unsolved:
            break
        for s1 in list(solved.keys()):
            for s2 in unsolved:
                if s1 == s2 or s2 in solved.keys():
                    continue

                prev_fingerprint = get_fingerprint(set_to_array(solved[s1]))

                # get fingerprint
                current_fingerprint = get_fingerprint(set_to_array(data[s2]))
                keys_intersection = set(current_fingerprint.keys()).intersection(prev_fingerprint.keys())

                if not keys_intersection:
                    continue


                # figure out previous pos to current pos of the same beacon
                current_to_prev_mapping = defaultdict(set)
                for key in keys_intersection:
                    keys = [(x, y, z) for x, y, z in current_fingerprint[key]]
                    values = {(x, y, z) for x, y, z in prev_fingerprint[key]}
                    for k in keys:
                        if current_to_prev_mapping[k]:
                            current_to_prev_mapping[k].intersection_update(values)
                        else:
                            current_to_prev_mapping[k] = values
                current_to_prev_mapping = {k: next(iter(v)) for k, v in current_to_prev_mapping.items() if v and len(v) == 1}
                #print('detected', len(current_to_prev_mapping), "intersections")
                if len(current_to_prev_mapping) < 12:
                    continue
                print("scanners", s1, "and", s2)
                # figure out transformation
                transformation, move = None, None
                current_items = numpy.array([numpy.array(i) for i in current_to_prev_mapping.keys()])
                prev_items = numpy.array([numpy.array(i) for i in current_to_prev_mapping.values()])
                for p in permutations_set:
                    rotated = swap(current_items, p[0], p[1], p[2])
                    diff = prev_items[0] - rotated[0]
                    diff_matrix = numpy.tile(diff, (len(current_to_prev_mapping), 1))
                    if numpy.array_equal(prev_items - diff_matrix, rotated):
                        transformation = p
                        move = diff
                        break
                print(transformation, move)
                print(s2, "solved with", len(current_to_prev_mapping), "intersections")
                solved[s2] = (transformation, move)

                # apply transformation to beacons from current scanner
                new_beacons_relative = data[s2]
                new_beacons_r = [swap([numpy.array([x, y, z])], *transformation)[0] + move for x, y, z in new_beacons_relative]
                new_beacons = [(x, y, z) for x, y, z in new_beacons_r]
                solved[s2] = new_beacons
                break
    print(len({i for s in solved.values() for i in s}))

part1(data)
