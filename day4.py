import numpy as np
import re


def count_xmas(list_):
    xmas = "XMAS"
    counter = 0
    for i in list_:
        freq = i.count(xmas)
        counter += freq
        freq = i.count(xmas[::-1])
        counter += freq
    return counter


def find_diagonal(matrix):

    matrix = np.array([list(i) for i in matrix])
    a = matrix.shape[0]
    list_ = [np.diag(matrix, k=i).tolist() for i in range(-a + 1, a)]
    list_ = ["".join(i) for i in list_]
    count1 = count_xmas(list_)
    list_ = [np.diag(np.fliplr(matrix), k=i).tolist() for i in range(-a + 1, a)]
    list_ = ["".join(i) for i in list_]
    count2 = count_xmas(list_)
    return count1 + count2


def find_vertical(matrix):
    matrix = np.array(matrix)
    a = matrix.shape[0]
    list_ = [matrix[i].tolist() for i in range(a)]
    return count_xmas(list_)


def find_horizontal(matrix):
    matrix = np.array(matrix)
    a = matrix.shape[0]
    all_letters = len(matrix[0])
    vertical_lines = []
    for j in range(all_letters):
        vertical_line = ""
        for i in range(a):
            vertical_line += matrix[i][j]
        vertical_lines.append(vertical_line)
    list_ = vertical_lines
    return count_xmas(list_)


def part1():
    full_text = np.loadtxt("data/day4_1.txt", dtype=str)
    matrix = full_text
    counter = find_diagonal(matrix) + find_vertical(matrix) + find_horizontal(matrix)
    print(counter)


def count_cros(matrix):
    vertival = matrix.shape[0]
    horizontal = len(matrix[0])
    counter = 0
    for v in range(vertival - 2):
        for h in range(horizontal - 2):
            letter1 = "M" == matrix[v][h]
            letter2 = "S" == matrix[v][h + 2]
            letter3 = "A" == matrix[v + 1][h + 1]
            letter4 = "M" == matrix[v + 2][h]
            letter5 = "S" == matrix[v + 2][h + 2]
            if letter1 and letter2 and letter3 and letter4 and letter5:
                counter += 1
                # print(matrix[v][h], ".", matrix[v][h + 2])
                # print(".", matrix[v + 1][h + 1], ".")
                # print(matrix[v + 2][h], ".", matrix[v + 2][h + 2])
                # # exit()
    return counter


def part2():
    full_text = np.loadtxt("data/day4_1.txt", dtype=str)
    matrix = full_text
    matrix = np.array([list(i) for i in matrix])
    count1 = count_cros(matrix)
    count2 = count_cros(np.fliplr(matrix))
    count3 = count_cros(np.rot90(matrix))
    count4 = count_cros(np.rot90(np.flipud(matrix)))
    print(count1 + count2 + count3 + count4)


if __name__ == "__main__":
    # part1()
    part2()
