import numpy as np


def read_input(file_path):
    with open(file_path, "r") as f:
        lines = []
        lines = [list(line.strip()) for line in f.readlines()]
    return np.array(lines, dtype=str)


def part1(matrix):
    # print(matrix)
    # max_range = len(matrix)
    cursor = np.where(matrix == "^")
    while cursor[0] > 0:
        if matrix[cursor[0] - 1, cursor[1]] != "#":
            matrix[cursor] = "X"
            matrix[cursor[0] - 1, cursor[1]] = "^"
        if matrix[cursor[0] - 1, cursor[1]] == "#":
            matrix = np.rot90(matrix)
            # input()
        # max_range = len(matrix)
        cursor = np.where(matrix == "^")
        # print(matrix)
    else:
        matrix[cursor] = "X"
    # Count the number of X
    num_X = np.count_nonzero(matrix == "X")
    print(num_X)

    return


def part2(matrix):
    return


if __name__ == "__main__":
    matrix = read_input("data/day6_test.txt")
    # matrix = read_input("data/day6_1.txt")
    part1(matrix)
    part2(matrix)
