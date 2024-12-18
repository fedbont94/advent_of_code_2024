# import chache
from functools import cache


def read_input(file):
    with open(file) as f:
        return f.read().strip()


def apply_rule(line):
    new_line = []
    for elem in line:
        if elem == "0":
            new_line.append("1")
        elif len(elem) % 2 == 0:
            lengthHalf = len(elem) // 2
            el1 = elem[:lengthHalf]
            el2 = int(elem[lengthHalf:])
            new_line.append(el1)
            new_line.append(str(el2))
        else:
            elem = int(elem)
            elem *= 2024
            new_line.append(str(elem))
    return new_line


@cache
def part1(line):
    for i in range(25):
        line = apply_rule(line)
    # print(len(line))
    return line


def part2(line):
    counter = 0
    for idx, elem1 in enumerate(line):
        new_line1 = [elem1]
        new_line1 = part1(new_line1)
        for elem2 in new_line1:
            new_line2 = [elem2]
            new_line2 = part1(new_line2)
            for elem3 in new_line2:
                new_line3 = [elem3]
                new_line3 = part1(new_line3)
                counter += len(new_line3)
        if idx % 10 == 0:
            print(idx)
    print(counter)
    return


if __name__ == "__main__":
    # file = "data/day11_test.txt"
    file = "data/day11.txt"

    line = read_input(file)
    line = line.split(" ")
    # part1(line)
    part2(line)
