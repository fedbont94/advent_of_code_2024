import numpy as np


def read_file():
    # with open("data/day5_test.txt", "r") as f:
    with open("data/day5_1.txt", "r") as f:
        all_lines = [line.strip() for line in f]
        file_1 = []
        file_2 = []
        for line in all_lines:
            if "|" in line:
                num1, num2 = line.split("|")
                file_1.append([int(num1), int(num2)])
            if "," in line:
                nums = line.split(",")
                file_2.append([int(num) for num in nums])
        return np.array(file_1), file_2


def check_line(file_1, line):
    for i in range(len(line)):
        if i == 0:
            continue
        numb = line[i]
        prev_numbs = line[:i]
        mask = numb == file_1[:, 0]
        matching = file_1[mask]
        prev_mustNOT = matching[:, 1]
        isTrue = np.all([prev_numb != prev_mustNOT for prev_numb in prev_numbs])
        if not isTrue:
            return 0

    return line[int(len(line) / 2)]


def part1():
    file_1, file_2 = read_file()
    counter = 0
    for line in file_2:
        line = np.array(line)
        counter += check_line(file_1, line)
    print(counter)


def order_line(file_1, line):
    for i in range(len(line)):
        if i == 0:
            continue
        numb = line[i]
        prev_numbs = line[:i]
        mask = numb == file_1[:, 0]
        matching = file_1[mask]
        prev_mustNOT = matching[:, 1]
        bool_list = np.array([prev_numb != prev_mustNOT for prev_numb in prev_numbs])
        isTrue = np.all(bool_list)
        if not isTrue:
            # find the index of the first False
            index = np.where(bool_list == False)[0][0]
            # pop the number from the line
            numberToDelete = line[i]
            line = np.delete(line, i)
            # move the number from i to index
            line = np.insert(line, index, numberToDelete)
            return line, False
    return line, True


def check_line_part2(file_1, line):
    if check_line(file_1, line) != 0:
        return 0
    isGood = False
    while not isGood:
        line, isGood = order_line(file_1, line)
    return line[int(len(line) / 2)]


def part2():

    file_1, file_2 = read_file()
    counter = 0
    for line in file_2:
        line = np.array(line)
        counter += check_line_part2(file_1, line)
    print(counter)


if __name__ == "__main__":
    part1()
    part2()
