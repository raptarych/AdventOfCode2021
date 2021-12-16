input_file = open('input.txt', mode='r')

data = [bin(int(my_hexdata.strip(), 16))[2:].zfill(len(my_hexdata.strip()) * 4) for my_hexdata in input_file.readlines()]
print(data)


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
            print('\t' * recursion_level, "version", version)
            print('\t' * recursion_level, "type_id", type_id)
        else:
            if type_id == 4:
                b_num = binary_num[0:5]
                binary_num = binary_num[5:]

                print('\t' * recursion_level, "literal", int(b_num[1:], 2))
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
    return (binary_num, version_sum)


for d in data:
    print(part1(d))
