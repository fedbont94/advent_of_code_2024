import numpy as np
import re


def part1(full_text):
    full_text = full_text.replace("mul ", "")
    full_text = full_text.replace("mul ( ", "")
    starting_index = [m.start() for m in re.finditer(r"mul\(", full_text)]

    all_mul = []
    for i in starting_index:
        ending_index = re.search(r"\)", full_text[i:]).end() + i
        all_mul.append(full_text[i:ending_index])

    final_result = 0
    for item in all_mul:
        item = item.replace("mul(", "")
        item = item.replace(")", "")
        try:
            num1, num2 = item.split(",")
        except:
            continue
        try:
            num1 = int(num1)
            num2 = int(num2)
        except:
            continue
        final_result += num1 * num2
    print(final_result)


def part2(full_text):
    full_text = full_text.replace("mul ", "")
    full_text = full_text.replace("mul ( ", "")
    donts = [m.start() for m in re.finditer(r"don't", full_text)]
    strings_to_remove = []
    for dont in donts:
        mulPos = full_text.find("do()", dont)
        partial_text = full_text[dont:mulPos]
        strings_to_remove.append(partial_text)
    for partial_text in strings_to_remove:
        full_text = full_text.replace(partial_text, "")
    part1(full_text)


if __name__ == "__main__":
    with open("data/day3_1.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    full_text = "".join(lines)
    part1(full_text)
    part2(full_text)
