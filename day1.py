import numpy as np


def part1():
    file_one = np.loadtxt("data/day1_1.txt")

    data1 = file_one[:, 0]
    data2 = file_one[:, 1]

    # Set both arrays in growing order
    data1 = np.sort(data1)
    data2 = np.sort(data2)

    difference = data1 - data2
    difference = np.abs(difference)

    total = np.sum(difference)

    print("The total is: ", total)


def part2():
    file_one = np.loadtxt("data/day1_1.txt")
    data1 = file_one[:, 0]
    data2 = file_one[:, 1]

    # For each element in data1, see how ofter is in data2
    total_similarity_score = 0
    for d in data1:
        score = np.sum(data2 == d)
        total_similarity_score += score * d

    print("The total similarity score is: ", total_similarity_score)


if __name__ == "__main__":
    part1()
    part2()
