import itertools



def check_combinations(numberList, combiantions, result):
    for combination in combiantions:
        tempResult = 0
        for i, number in enumerate(numberList):
            if i == 0:
                tempResult = number
            else:
                if combination[i-1] == "+":
                    tempResult += number
                if combination[i-1] == "*":
                    tempResult *= number
                if combination[i-1] == "||":
                    tempResult = int(str(tempResult) + str(number))

        if tempResult == result:
            return True
    return False






def part1_and_2(file, operations):
    with open(file) as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    resutls = []
    numbers = []
    for line in lines:
        result,  number = line.split(":")
        resutls.append(result)
        numbers.append(number)
    
    sumOfTrue = 0
    for result, number in zip(resutls, numbers):
        result = int(result)
        numberList = [int(x) for x in number.split(" ") if x.isdigit()]
        repeat = len(numberList) - 1
        combiantions = list(itertools.product(operations, repeat=repeat))   
        isTrue = check_combinations(numberList, combiantions, result)
        if isTrue:
            sumOfTrue += result
    print(sumOfTrue)

    return

if __name__ == '__main__':
    # file = "data/day7_test.txt"
    file = "data/day7_1.txt"
    # operations = ["+", "*"]
    operations = ["+", "*", "||"]
    
    part1_and_2(file, operations)