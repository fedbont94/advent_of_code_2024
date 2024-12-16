import numpy as np


def read_input(file_path):
    with open(file_path, "r") as f:
        lines = []
        lines = [list(line.strip()) for line in f.readlines()]
    return np.array(lines, dtype=str)


def part1(matrix):
    cursor = np.where(matrix == "^")
    while cursor[0] > 0:
        if matrix[cursor[0] - 1, cursor[1]] != "#":
            matrix[cursor] = "X"
            matrix[cursor[0] - 1, cursor[1]] = "^"
        if matrix[cursor[0] - 1, cursor[1]] == "#":
            matrix = np.rot90(matrix)
        cursor = np.where(matrix == "^")
    else:
        matrix[cursor] = "X"
    # Count the number of X
    num_X = np.count_nonzero(matrix == "X")
    print(num_X)

    return


def check_if_is_a_loop(matrix):
    cursor = np.where(matrix == "^")
    counter_steps = 0
    maxSteps = matrix.shape[0] * matrix.shape[1]
    while cursor[0] > 0:
        if matrix[cursor[0] - 1, cursor[1]] == "#":
            matrix = np.rot90(matrix)
        if matrix[cursor[0] - 1, cursor[1]] != "#":
            if matrix[cursor[0] - 1, cursor[1]] == "X":
                counter_steps += 1
            else:
                counter_steps = 0

            matrix[cursor] = "X"
            matrix[cursor[0] - 1, cursor[1]] = "^"
        cursor = np.where(matrix == "^")
        if counter_steps > maxSteps:
            return True

    return False


def check_if_is_a_loop2(matrix):
    cursor = np.where(matrix == "^")
    cursor = np.array([cursor[0][0], cursor[1][0]])
    directions = np.array(
        [[-1, 0], [0, 1], [1, 0], [0, -1]]  # Up  # Right  # Down  # Left
    )
    directionString = ["^", ">", "v", "<"]
    counter = 0
    indexDir = 0
    maxSteps = matrix.shape[0] * matrix.shape[1]
    while (
        (cursor[0] > 0)
        and (cursor[1] > 0)
        and (cursor[0] < matrix.shape[0] - 1)
        and (cursor[1] < matrix.shape[1] - 1)
    ):
        next_position = cursor + directions[indexDir]
        next_position = tuple(next_position)
        if matrix[next_position] != "#":
            if directionString[indexDir] in list(matrix[tuple(cursor)]):
                counter += 1
            matrix[tuple(cursor)] = directionString[indexDir]
            cursor = next_position
        if matrix[next_position] == "#":
            indexDir += 1
            indexDir = indexDir % 4
        if counter > maxSteps:
            return True
    else:
        matrix[cursor] = "X"
    return False


def part2(matrix):
    matrix_copy = matrix.copy()
    counter = 0
    cursor = np.where(matrix == "^")
    while cursor[0] > 0:
        if matrix[cursor[0] - 1, cursor[1]] == "#":
            matrix = np.rot90(matrix)
        cursor = np.where(matrix == "^")
        if matrix[cursor[0] - 1, cursor[1]] != "#":
            matrix_copy = matrix.copy()
            if matrix[cursor[0] - 1, cursor[1]] != "X":
                matrix_copy[cursor[0] - 1, cursor[1]] = "#"
                isLoop = check_if_is_a_loop2(matrix_copy)
                if isLoop:
                    counter += 1
            matrix[cursor] = "X"
            matrix[cursor[0] - 1, cursor[1]] = "^"
        num_X = np.count_nonzero(matrix == "X")
        if num_X % 10 == 0:
            print(num_X)
    else:
        matrix[cursor] = "X"
    print("Final result:", counter)
    return


if __name__ == "__main__":
    # matrix = read_input("data/day6_test.txt")
    matrix = read_input("data/day6_1.txt")
    # part1(matrix)
    part2(matrix)

# 1846 too large
