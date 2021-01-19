numbers = [1, 2, 3, 5, 8, 10, 12, 13, 14, 15, 17, 19, 21, 23, 24, 25, 26]
# Findout all the sequence from the given list and its count.
position = 0
for position in range(0, len(numbers)):
    sequence_list = []
    ele1 = numbers[position]
    next_exp_num = ele1 + 1
    ref_position = position
    while True:
        if next_exp_num == numbers[ref_position + 1]:
            sequence_list.append(numbers[ref_position])
            next_exp_num = next_exp_num + 1
            ref_position += 1

        else:
            sequence_list.append(numbers[ref_position])
            print("Sequence is ", sequence_list)
            break

