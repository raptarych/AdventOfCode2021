import numpy

input_file = open('input.txt', mode='r')

hexadecimals = [bin(int(i.strip(), 16))[2:].zfill(len(i.strip()) * 4)
                # can read multiple lines (good for testing different cases at once)
                for i in input_file.readlines()]

operators = [
    sum,
    numpy.prod,
    min,
    max,
    lambda x: x,
    lambda x: 1 if x[0] > x[1] else 0,
    lambda x: 1 if x[0] < x[1] else 0,
    lambda x: 1 if x[0] == x[1] else 0
]


def part1(binary_num, version=None, type_id=None, expected_packets=1, recursion_level=0):
    version_sum = 0
    while expected_packets and len(binary_num) > 0:
        if version is None:
            version = int(binary_num[0:3], 2)
            version_sum += version
            binary_num = binary_num[3:]
        elif type_id is None:
            type_id = int(binary_num[0:3], 2)
            binary_num = binary_num[3:]
        else:
            if type_id == 4:
                b_num = binary_num[0:5]
                binary_num = binary_num[5:]

                if b_num[0] == '0':
                    expected_packets -= 1
                    version = None
                    type_id = None
                    continue
            else:
                i = binary_num[0]
                binary_num = binary_num[1:]
                if i == '0':
                    subpacket_l = binary_num[:15]
                    binary_num = binary_num[15:]
                    subpacket = binary_num[:int(subpacket_l, 2)]
                    (_, subpacket_versions) = part1(subpacket, recursion_level=recursion_level + 1,
                                                    expected_packets=99999999)
                    binary_num = binary_num[int(subpacket_l, 2):]
                elif i == '1':
                    subpacket_l = int(binary_num[:11], 2)
                    binary_num = binary_num[11:]
                    (binary_num, subpacket_versions) = part1(binary_num, expected_packets=subpacket_l,
                                                             recursion_level=recursion_level + 1)
                version_sum += subpacket_versions
                version = None
                type_id = None
                expected_packets -= 1
    return binary_num, version_sum


def part2(binary_num, version=None, type_id=None, recursion_level=0):
    package_results = []
    package_literal_b = ''
    while len(binary_num) > 0:
        if version is None:
            version = int(binary_num[0:3], 2)
            binary_num = binary_num[3:]
            continue
        if type_id is None:
            type_id = int(binary_num[0:3], 2)
            binary_num = binary_num[3:]
            print('\n', '\t' * recursion_level, "version", version)
            print('\t' * recursion_level, "type_id", type_id)
            continue

        if type_id == 4:
            b_num = binary_num[0:5]
            binary_num = binary_num[5:]

            package_literal_b += b_num[1:]
            if b_num[0] == '1':
                continue
            if b_num[0] == '0':
                print('\t' * recursion_level, "literal", int(package_literal_b, 2))
                return binary_num, int(package_literal_b, 2)
        else:
            i = binary_num[0]
            binary_num = binary_num[1:]
            if i == '0':
                subpacket_l = binary_num[:15]
                binary_num = binary_num[15:]
                subpacket = binary_num[:int(subpacket_l, 2)]
                binary_num = binary_num[int(subpacket_l, 2):]
                while subpacket:
                    (subpacket, result) = part2(subpacket, recursion_level=recursion_level + 1)
                    package_results.append(result)
            elif i == '1':
                subpacket_l = int(binary_num[:11], 2)
                binary_num = binary_num[11:]
                for it in range(subpacket_l):
                    binary_num, result = part2(binary_num, recursion_level=recursion_level + 1)
                    package_results.append(result)
            return binary_num, operators[type_id](package_results)


for v in hexadecimals:
    answer = [part1(v), part2(v)]
    print("part 1:", answer[0][1])
    print("part 2:", answer[1][1])
