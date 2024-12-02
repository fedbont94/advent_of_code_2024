import numpy as np


def check_array(array):
    isSafe = False

    orderingCheck = np.sum(array[:-1] < array[1:])
    if orderingCheck == len(array) - 1:
        isSafe = True

    orderingCheck = np.sum(array[:-1] > array[1:])
    if orderingCheck == len(array) - 1:
        isSafe = True

    if not isSafe:
        return False

    differenceCheck = np.abs(array[:-1] - array[1:])
    if np.sum(differenceCheck > 3) != 0:
        isSafe = False

    return isSafe


def part1():
    with open("data/day2_1.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    counter = 0
    for line in lines:
        digits_list = line.split()
        digits_list = [int(d) for d in digits_list]
        digits_array = np.array(digits_list)
        isSafe = check_array(digits_array)
        if isSafe:
            counter += 1
    print("Counter 1:", counter)
    return


def part2():
    with open("data/day2_1.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    counter = 0
    for line in lines:
        digits_list = line.split()
        digits_list = [int(d) for d in digits_list]
        digits_array = np.array(digits_list)
        isSafe = check_array(digits_array)
        if isSafe:
            counter += 1
        else:
            for i in range(len(digits_array)):
                isSafe = check_array(np.delete(digits_array, i))
                if isSafe:
                    counter += 1
                    break

    print("Counter 2:", counter)

    return


if __name__ == "__main__":
    part1()
    part2()
