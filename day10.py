import numpy as np


def read_input(file_path):
    with open(file_path, "r") as file:
        return np.array([list(line.strip()) for line in file]).astype(int)


def find_prev_number(matrix, numb, pos):
    next_pos = []
    if pos[0] + 1 < matrix.shape[0]:
        if matrix[pos[0] + 1, pos[1]] == numb - 1:
            next_pos.append((pos[0] + 1, pos[1]))
    if pos[0] - 1 >= 0:
        if matrix[pos[0] - 1, pos[1]] == numb - 1:
            next_pos.append((pos[0] - 1, pos[1]))
    if pos[1] + 1 < matrix.shape[1]:
        if matrix[pos[0], pos[1] + 1] == numb - 1:
            next_pos.append((pos[0], pos[1] + 1))
    if pos[1] - 1 >= 0:
        if matrix[pos[0], pos[1] - 1] == numb - 1:
            next_pos.append((pos[0], pos[1] - 1))
    return next_pos


def part1(matrix):

    find0 = np.where(matrix == 0)
    zerosCount = {key: [] for key in (zip(find0[0], find0[1]))}
    find9 = np.where(matrix == 9)
    for ninePos in zip(find9[0], find9[1]):
        next_pos_8 = find_prev_number(matrix, 9, ninePos)
        for eightPos in next_pos_8:
            next_pos_7 = find_prev_number(matrix, 8, eightPos)
            for sevenPos in next_pos_7:
                next_pos_6 = find_prev_number(matrix, 7, sevenPos)
                for sixPos in next_pos_6:
                    next_pos_5 = find_prev_number(matrix, 6, sixPos)
                    for fivePos in next_pos_5:
                        next_pos_4 = find_prev_number(matrix, 5, fivePos)
                        for fourPos in next_pos_4:
                            next_pos_3 = find_prev_number(matrix, 4, fourPos)
                            for threePos in next_pos_3:
                                next_pos_2 = find_prev_number(matrix, 3, threePos)
                                for twoPos in next_pos_2:
                                    next_pos_1 = find_prev_number(matrix, 2, twoPos)
                                    for onePos in next_pos_1:
                                        next_pos_0 = find_prev_number(matrix, 1, onePos)
                                        for zeroPos in next_pos_0:
                                            if ninePos not in zerosCount[zeroPos]:
                                                zerosCount[zeroPos].append(ninePos)

    values = zerosCount.values()
    totalCount = sum([len(val) for val in values])
    print(totalCount)
    return


def part2(matrix):

    find0 = np.where(matrix == 0)
    zerosCount = {key: [] for key in (zip(find0[0], find0[1]))}
    find9 = np.where(matrix == 9)
    for ninePos in zip(find9[0], find9[1]):
        next_pos_8 = find_prev_number(matrix, 9, ninePos)
        for eightPos in next_pos_8:
            next_pos_7 = find_prev_number(matrix, 8, eightPos)
            for sevenPos in next_pos_7:
                next_pos_6 = find_prev_number(matrix, 7, sevenPos)
                for sixPos in next_pos_6:
                    next_pos_5 = find_prev_number(matrix, 6, sixPos)
                    for fivePos in next_pos_5:
                        next_pos_4 = find_prev_number(matrix, 5, fivePos)
                        for fourPos in next_pos_4:
                            next_pos_3 = find_prev_number(matrix, 4, fourPos)
                            for threePos in next_pos_3:
                                next_pos_2 = find_prev_number(matrix, 3, threePos)
                                for twoPos in next_pos_2:
                                    next_pos_1 = find_prev_number(matrix, 2, twoPos)
                                    for onePos in next_pos_1:
                                        next_pos_0 = find_prev_number(matrix, 1, onePos)
                                        for zeroPos in next_pos_0:
                                            zerosCount[zeroPos].append(ninePos)

    values = zerosCount.values()
    totalCount = sum([len(val) for val in values])
    print(totalCount)
    return


if __name__ == "__main__":
    # file_path = "data/day10_test.txt"
    file_path = "data/day10.txt"
    matrix = read_input(file_path)
    # part1((matrix))
    part2((matrix))
