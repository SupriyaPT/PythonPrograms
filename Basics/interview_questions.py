a = "1"
b = 2
print(int(a) + b)


#dictionary comprehension - Filter the dictionary by removing all items with a value of greater than 1.
d = {"a": 1, "b": 2, "c": 3}
d_nw = {k:d[k] for k in d.keys() if d[k] > 1}


def word_count(file_path):

    with open(file_path, 'r') as f:
        all_data = f.readlines()

    total_word_count = 0
    for line in all_data:
        word_count_per_row = 0
        line = line.replace(",", " ")
        split_line = line.split()
        word_count_per_row += len(split_line)
        total_word_count += word_count_per_row
        print("word count: ", word_count_per_row)

    print("Total word count ", total_word_count)


word_count('words1.txt')

#