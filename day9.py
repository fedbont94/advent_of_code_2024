import numpy as np


def replaceDots(string):
    reversedString = string[::-1]
    # reversedString = list(reversedString)
    number = None
    for i in range(len(reversedString)):
        number = reversedString[i]
        break
    if number is None:
        return string

    for i in range(len(string)):
        if string[i] == -1:
            string = list(string)
            string[i] = number
            # string = "".join(string[:-1])
            return string[:-1]


def part1(line):
    finalString = np.array([], dtype=int)

    length = len(line)
    totID = np.arange((length + 1) // 2)
    for i in range(length):
        if i % 2 != 0:
            continue
        iD = totID[i // 2]
        files = int(line[i])
        if i + 1 == length:
            freeSpace = 0
        else:
            freeSpace = int(line[i + 1])
        idList = np.array(([iD] * files), dtype=int)
        finalString = np.append(finalString, idList)
        if freeSpace != 0:
            finalString = np.append(finalString, np.zeros(freeSpace, dtype=int) - 1)
    finalStringLen = len(finalString)
    for i in range(finalStringLen):
        finalString = replaceDots(finalString)
        if (-1) not in list(finalString):
            break

    # finalString = finalString.ljust(finalStringLen, ".")
    # print(finalString)
    finalString = np.array(finalString, dtype=int)
    fullID = np.arange(len(finalString))
    mult = np.multiply(fullID, finalString)
    sum = np.sum(mult)
    print(sum)

    return


def part2(line):
    finalString = np.array([], dtype=int)

    length = len(line)
    totID = np.arange((length + 1) // 2)
    for i in range(length):
        if i % 2 != 0:
            continue
        iD = totID[i // 2]
        files = int(line[i])
        if i + 1 == length:
            freeSpace = 0
        else:
            freeSpace = int(line[i + 1])
        idList = np.array(([iD] * files), dtype=int)
        finalString = np.append(finalString, idList)
        if freeSpace != 0:
            finalString = np.append(finalString, np.zeros(freeSpace, dtype=int) - 1)

    return


if __name__ == "__main__":
    name = "data/day9_1.txt"
    # name = "data/day9_test.txt"
    with open(name) as f:
        file = f.read()

    part1(file)
    part2(file)
