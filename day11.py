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


def part1(line):
    for i in range(25):
        line = apply_rule(line)
    # print(len(line))
    return line


def part2(line):
    counter = 0
    counter1 = 0
    counter2 = 0
    counter1_dict = {}
    counter2_dict = {}
    counter3_dict = {}
    for idx, elem1 in enumerate(line):
        if elem1 in counter1_dict:
            counter1 = counter1_dict[elem1]
        else:
            counter1 = 0
            new_line1 = [elem1]
            new_line1 = part1(new_line1)
            for elem2 in new_line1:
                if elem2 in counter2_dict:
                    counter2 = counter2_dict[elem2]
                else:
                    counter2 = 0
                    new_line2 = [elem2]
                    new_line2 = part1(new_line2)
                    for elem3 in new_line2:
                        if elem3 in counter3_dict:
                            counter3 = counter3_dict[elem3]
                        else:
                            new_line3 = [elem3]
                            new_line3 = part1(new_line3)
                            counter3 = len(new_line3)
                            counter3_dict[elem3] = counter3
                        counter2 += counter3
                    counter2_dict[elem2] = counter2
                counter1 += counter2
            counter1_dict[elem1] = counter1
        counter += counter1
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
