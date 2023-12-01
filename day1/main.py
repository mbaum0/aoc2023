calibration_file = "./day1/calibration.txt"


def part1(lines):
    valid_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    line_nums = []
    sum = 0
    for i, line in enumerate(lines):
        line_nums.append([])
        for char in line:
            if char in valid_nums:
                line_nums[i].append(char)

        if len(line_nums[i]) == 1:
            line_nums[i] = line_nums[i]*2

        if len(line_nums[i]) > 0:
            sum += int("".join([line_nums[i][0], line_nums[i][-1]]))

    return sum


def part2(lines):
    str_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    newlines = []
    for i, line in enumerate(lines):
        line_indicies = {}
        for num in str_nums:
            index = line.find(num)
            while index != -1:
                line_indicies[index] = num
                index = line.find(num, index+1)
        newline = line

        cnt = 0
        for idx, num in sorted(line_indicies.items()):
            newline = newline[:idx+cnt] + str(str_nums.index(num)+1) + newline[idx+cnt:]
            cnt += 1
        
        newlines.append(newline)

    return part1(newlines)



with open(calibration_file, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    print(part1(lines))
    print(part2(lines))
