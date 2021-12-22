# f = open("input3.txt", "r")


# def get_data():
#     f = open("input3.txt", "r")
#     data = f.read().splitlines()
#     return data


# data = get_data()
# count = [0] * len(data[0])

# # for d in data:
# #     for i, v in enumerate(d):
# #         if v == '1':
# #             count[i] += 1


# # gamma = epsilon = 0
# # for i in range(len(data[0])):
# #     gamma <<= 1
# #     epsilon <<= 1
# #     print(bin(gamma))
# #     print(bin(epsilon))
# #     if count[i] > len(data)//2:
# #         gamma += 1
# #     else:
# #         epsilon += 1
# # print(gamma)
# # print(epsilon)

# # print(gamma * epsilon)


# def solution2(l, n_bit):
#     o2_l = l.copy()
#     co2_l = l.copy()

#     for i in range(n_bit):
#         o2_bit = sum((_l >> (n_bit - i)) & 1 for _l in o2_l) >= len(o2_l) / 2
#         o2_l = [_l for _l in o2_l if (_l >> (n_bit - i)) & 1 == o2_bit] or o2_l

#     for i in range(n_bit):
#         co2_bit = sum((_l >> (n_bit - i)) & 1 for _l in co2_l) < len(co2_l) / 2
#         co2_l = [_l for _l in co2_l if (
#             _l >> (n_bit - i)) & 1 == co2_bit] or co2_l

#     return o2_l[0] * co2_l[0]


# data = [int(x, 2) for x in f]
# n_bit = max(bit.bit_length() for bit in data)
# print(solution2(data, n_bit))


"""Advent of Code 2021 Day 3 - Binary Diagnostic"""


def convert_to_columns(binary_values):
    """Takes list of strings and returns one with rows and columns swapped."""
    column_conversion = []
    for row_num in range(len(binary_values[0])):
        column_conversion.append('')
        for col_num in range(len(binary_values)):
            column_conversion[-1] += binary_values[col_num][row_num]

    return column_conversion


with open('input3.txt', 'r') as aoc_input:
    input_lines = [line.strip() for line in aoc_input.readlines()]

binary_columns = convert_to_columns(input_lines)
gamma = ''
for column in binary_columns:
    if column.count('0') > len(column) / 2:
        gamma += '0'
    else:
        gamma += '1'

epsilon = ''.join(map(lambda bit: '1' if bit == '0' else '0', gamma))

# Answer One
print("Submarine power consumption:", int(gamma, 2) * int(epsilon, 2))

oxy_binaries = input_lines.copy()
oxy_columns = binary_columns.copy()
oxy_criteria = ''
i = 0
while len(oxy_binaries) > 1:
    if oxy_columns[i].count('1') >= len(oxy_columns[i]) / 2:
        oxy_criteria += '1'
    else:
        oxy_criteria += '0'

    oxy_binaries = list(filter(
        lambda binary: binary.startswith(oxy_criteria), oxy_binaries
    )
    )
    oxy_columns = convert_to_columns(oxy_binaries)

    i += 1

co2_binary = input_lines.copy()
co2_columns = binary_columns.copy()
co2_criteria = ''
i = 0
while len(co2_binary) > 1:
    if co2_columns[i].count('1') >= len(co2_columns[i]) / 2:
        co2_criteria += '0'
    else:
        co2_criteria += '1'

    co2_binary = list(filter(
        lambda binary: binary.startswith(co2_criteria), co2_binary
    )
    )
    co2_columns = convert_to_columns(co2_binary)

    i += 1

# Answer Two
print("Submarine life support rating:",
      int(oxy_binaries[0], 2) * int(co2_binary[0], 2))
