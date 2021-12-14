from collections import Counter
input_lines = [x.rstrip('\n') for x in open('input.txt', mode='r').readlines()]

polymer_init = input_lines[0]
rules_raw = [x.split(' -> ') for x in input_lines[2:]]
rules = {r[0]: r[1] for r in rules_raw}


# 1: naive method
def part1(polymer, steps=14):
    print("part1")

    def generate_next_polymer():
        for i in range(len(polymer) - 1):
            if i == 0:
                yield polymer[0]

            pair = polymer[i: i + 2]
            yield rules[pair]
            yield pair[1]

    for i in range(steps):
        next_polymer = generate_next_polymer()
        polymer = ''.join(list(next_polymer))

    c = Counter(polymer)
    print(max(c.values()) - min(c.values()))


# 2: recursive method
def part2(polymer_input, steps=40):
    print("part2")
    cache = {}

    def calc_polymer_counts(polymer, steps_left):
        if (polymer, steps_left) in cache:
            return cache[(polymer, steps_left)]

        if steps_left == 0:
            cache[(polymer, steps_left)] = Counter(polymer[1:])
            return cache[(polymer, steps_left)]

        if len(polymer) == 2:
            return calc_polymer_counts(polymer[0] + rules[polymer] + polymer[1], steps_left - 1)

        moving_window_2 = [polymer[i:i + 2] for i in range(0, len(polymer) - 1)]
        counts = [*map(lambda x: calc_polymer_counts(x, steps_left), moving_window_2)]
        iteration_result = {}
        for c in counts:
            for k, v in c.items():
                iteration_result[k] = (iteration_result[k] if k in iteration_result else 0) + v

        cache[(polymer, steps_left)] = iteration_result
        return iteration_result

    result = calc_polymer_counts(polymer_input, steps)
    result[polymer_input[0]] = (result[polymer_input[0]] if polymer_input[0] in result else 0) + 1
    print(max(result.values()) - min(result.values()))


part1(polymer_init)
part2(polymer_init)
