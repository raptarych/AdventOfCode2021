import math

input_file = open('input.txt', mode='r')

data = [eval(i) for i in input_file.readlines()]
print(data)


def is_regular(n):
    return isinstance(n, int)


def is_pair(n):
    return isinstance(n, list) and len(n) == 2 and all(map(is_regular, n))


def array_to_tree(n, depth=0):
    if is_regular(n):
        return (depth, n)
    result = []
    for i in n:
        subtree = array_to_tree(i, depth+1)
        if isinstance(subtree, list):
            result = [*result, *subtree]
        else:
            result = [*result, subtree]
    return result


def explode_if_needed(tree):
    replacement = {}
    deletion = []
    for i in range(1, len(tree)):
        (depth1, n1) = tree[i-1]
        (depth2, n2) = tree[i]
        if depth1 != depth2 or depth1 < 4:
            continue

        (depth_left, n_left, depth_right, n_right) = (None, None, None, None)
        if i - 2 >= 0:
            (depth_left, n_left) = tree[i-2]
        if i+1 < len(tree):
            (depth_right, n_right) = tree[i+1]
        if depth_left:
            replacement[i - 2] = (depth_left, n_left + n1)
        if depth_right:
            replacement[i + 1] = (depth_right, n_right + n2)
        replacement[i] = (depth1 - 1, 0)
        deletion.append(i-1)

        break

    if not replacement:
        return False

    for i in replacement:
        tree[i] = replacement[i]

    for i in deletion:
        del tree[i]

    return True


def split_if_needed(tree):
    replacement = {}
    addition = []
    for i in range(0, len(tree)):
        (depth, n) = tree[i]
        if n >= 10:
            replacement[(depth, n)] = (depth + 1, math.ceil(n / 2))
            addition = (depth + 1, int(n / 2))
            break
    if not replacement:
        return False
    for i in replacement:
        idx = tree.index(i)
        tree[idx] = replacement[i]
        tree.insert(idx, addition)
    return True


numbers = []
for i in range(len(data)):
    x = array_to_tree(data[i])
    #print("Input ", x)
    if not numbers:
        numbers = [*[(d-1, n) for d, n in x]]
    else:
        numbers = [*[(d+1, n) for d, n in numbers], *x]

    while True:
        if explode_if_needed(numbers):
            continue
        if split_if_needed(numbers):
            continue
        break

result = [i[1] for i in numbers]

while len(result) > 1:
    reduced_result = [result[i] * 3 + result[i+1] * 2 for i in range(0, len(result), 2)]
    result = reduced_result


print(result)