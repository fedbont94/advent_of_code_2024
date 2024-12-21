import numpy as np


def read_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    matrix = [list(line.strip()) for line in lines]
    matrix = np.array(matrix, dtype=str)
    return matrix


def find_area_perimeter(matrix, letter):
    area = np.sum(matrix == letter)
    perimeter = area * 4
    for pos in np.argwhere(matrix == letter):
        neighbors, _ = find_neighbors(matrix, letter, pos)
        perimeter -= neighbors
    return area, perimeter


def find_neighbors(matrix, letter, pos):
    neighbors = 0
    pos_n = []
    if pos[0] + 1 < matrix.shape[0]:
        if matrix[pos[0] + 1, pos[1]] == letter:
            neighbors += 1
            pos_n.append((pos[0] + 1, pos[1]))
    if pos[0] - 1 >= 0:
        if matrix[pos[0] - 1, pos[1]] == letter:
            neighbors += 1
            pos_n.append((pos[0] - 1, pos[1]))
    if pos[1] + 1 < matrix.shape[1]:
        if matrix[pos[0], pos[1] + 1] == letter:
            neighbors += 1
            pos_n.append((pos[0], pos[1] + 1))
    if pos[1] - 1 >= 0:
        if matrix[pos[0], pos[1] - 1] == letter:
            neighbors += 1
            pos_n.append((pos[0], pos[1] - 1))
    return neighbors, pos_n


def find_a_block(matrix, letter, pos):
    block = []
    block.append(pos)
    all_pos = []
    all_pos.append(pos)
    old_len = 0
    while len(all_pos) != old_len:
        old_len = len(all_pos)
        for all_p in all_pos:
            neighbors, pos_n = find_neighbors(matrix, letter, all_p)
            for p in pos_n:
                if p not in all_pos:
                    all_pos.append(p)
    return all_pos


def part1(matrix):
    result = 0
    allLetters = np.unique(matrix)
    for letter in allLetters:
        blocks = []
        find_all_pos = np.where(matrix == letter)
        for p1, p2 in zip(find_all_pos[0], find_all_pos[1]):
            in_block = False
            for block in blocks:
                if (p1, p2) in block:
                    in_block = True
            if in_block:
                continue

            block = find_a_block(matrix, letter, (p1, p2))
            blocks.append(block)

        for block in blocks:
            matrix_block = np.full(matrix.shape, ".")
            for pos in block:
                matrix_block[pos] = matrix[pos]

            area, perimeter = find_area_perimeter(matrix_block, letter)
            result += area * perimeter
    print(result)
    return


def part2():
    return


if __name__ == "__main__":
    # file_path = "data/day12_test.txt"
    file_path = "data/day12.txt"
    matrix = read_input(file_path)
    part1(matrix)
