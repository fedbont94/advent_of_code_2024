import numpy as np


def findPos(x1, y1, x2, y2):
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    if x1 >= x2:
        pos1x = x1 + x_diff
        pos2x = x2 - x_diff
    else:
        pos1x = x1 - x_diff
        pos2x = x2 + x_diff
    if y1 >= y2:
        pos1y = y1 + y_diff
        pos2y = y2 - y_diff
    else:
        pos1y = y1 - y_diff
        pos2y = y2 + y_diff

    return (pos1x, pos1y), (pos2x, pos2y)


def findMultiplePos(x1, y1, x2, y2):
    x_diff = abs(x2 - x1)
    y_diff = abs(y2 - y1)
    positions = [(x1, y1), (x2, y2)]
    for i in range(1, 50):
        if x_diff * i > 50 or y_diff * i > 50:
            break
        if x1 >= x2:
            pos1x = x1 + i * x_diff
            pos2x = x2 - i * x_diff
        else:
            pos1x = x1 - i * x_diff
            pos2x = x2 + i * x_diff
        if y1 >= y2:
            pos1y = y1 + i * y_diff
            pos2y = y2 - i * y_diff
        else:
            pos1y = y1 - i * y_diff
            pos2y = y2 + i * y_diff
        positions.append((pos1x, pos1y))
        positions.append((pos2x, pos2y))

    return positions


def part1(matrix):
    allAntennas = np.unique(matrix)
    allAntennas = allAntennas[allAntennas != "."]
    allPos = []
    for antenna in allAntennas:
        x_array, y_array = np.where(matrix == antenna)
        for i in range(len(x_array) - 1):
            for j in range(i + 1, len(x_array)):
                x1, y1 = x_array[i], y_array[i]
                x2, y2 = x_array[j], y_array[j]
                pos1, pos2 = findPos(x1, y1, x2, y2)
                # Check if pos1 and pos2 are within the matrix
                if (
                    pos1[0] >= 0
                    and pos1[0] < matrix.shape[0]
                    and pos1[1] >= 0
                    and pos1[1] < matrix.shape[1]
                ):
                    allPos.append(pos1)
                if (
                    pos2[0] >= 0
                    and pos2[0] < matrix.shape[0]
                    and pos2[1] >= 0
                    and pos2[1] < matrix.shape[1]
                ):
                    allPos.append(pos2)
    allPos = np.unique(allPos, axis=0)
    print(len(allPos))
    return


def part2(matrix):
    allAntennas = np.unique(matrix)
    allAntennas = allAntennas[allAntennas != "."]
    allPos = []
    for antenna in allAntennas:
        x_array, y_array = np.where(matrix == antenna)
        for i in range(len(x_array) - 1):
            for j in range(i + 1, len(x_array)):
                x1, y1 = x_array[i], y_array[i]
                x2, y2 = x_array[j], y_array[j]
                positions = findMultiplePos(x1, y1, x2, y2)
                # Check if pos1 and pos2 are within the matrix
                for pos in positions:
                    if (
                        pos[0] >= 0
                        and pos[0] < matrix.shape[0]
                        and pos[1] >= 0
                        and pos[1] < matrix.shape[1]
                    ):
                        allPos.append(pos)
    allPos = np.unique(allPos, axis=0)
    # for pos in allPos:
    #     matrix[pos[0], pos[1]] = "#"
    # matrix2 = np.array(["".join(line) for line in matrix])
    # for l in matrix2:
    #     print(l)
    print(len(allPos))
    return


if __name__ == "__main__":

    file = "data/day8_1.txt"
    # file = "data/day8_test.txt"
    matrix = np.loadtxt(file, dtype=str)
    matrix = np.array([list(line) for line in matrix])

    # part1(matrix)
    part2(matrix)
