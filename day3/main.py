filename = "input.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]


def is_symbol(char):
    if char.isnumeric() or char == ".":
        return False
    return True


def is_part_number(last_line, line, next_line, start_index, end_index):
    start_index = start_index - 1
    end_index = end_index + 1

    if is_symbol(line[start_index]):
        return True

    if is_symbol(line[end_index]):
        return True

    for k in range(start_index, end_index+1):
        if is_symbol(last_line[k]) or is_symbol(next_line[k]):
            return True
    return False


size = len(lines[0])

lines.insert(0, "."*size)
lines.append("."*size)

size += 2


def part_one():
    total = 0
    # I'm appending dots at the start and end of each line AND a line in the beginning and at the end of the test case, so I don't have to worry about bounds
    for index in range(1, len(lines)-1):
        last_line = "."+lines[index-1]+"."
        line = "."+lines[index]+"."
        next_line = "."+lines[index+1]+"."

        i = 0
        while i < size:
            number_str = ""

            if line[i].isnumeric():
                start_index = i
                while line[i].isnumeric():
                    number_str += line[i]
                    i += 1
                end_index = i-1
                if is_part_number(last_line, line, next_line, start_index, end_index):
                    total += int(number_str)
            else:
                i += 1
    print("part1 total:", total)


def get_number_backward(line, index):
    i = index
    while line[i].isnumeric():
        i -= 1
    return int(line[i+1:index+1])


def get_number_forward(line, index):
    i = index
    while line[i].isnumeric():
        i += 1
    return int(line[index:i])


def get_number_both_dir(line, index):
    start = index
    while line[start].isnumeric():
        start -= 1

    end = index
    while line[end].isnumeric():
        end += 1

    return int(line[start+1:end])


def get_numbers_other_lines(adjacent_part_numbers, line,  start_index, end_index, index):
    if line[index].isnumeric():
        adjacent_part_numbers.append(get_number_both_dir(line, index))
    else:
        if line[start_index].isnumeric():
            adjacent_part_numbers.append(
                get_number_backward(line, start_index))

        if line[end_index].isnumeric():
            adjacent_part_numbers.append(
                get_number_forward(line, end_index))


def gear_ratio(last_line, line, next_line, index):
    start_index = index - 1
    end_index = index + 1

    adjacent_part_numbers = []

    if line[start_index].isnumeric():
        adjacent_part_numbers.append(get_number_backward(line, start_index))

    if line[end_index].isnumeric():
        adjacent_part_numbers.append(get_number_forward(line, end_index))

    get_numbers_other_lines(adjacent_part_numbers,
                            last_line, start_index, end_index, index)

    get_numbers_other_lines(adjacent_part_numbers,
                            next_line, start_index, end_index, index)

    if len(adjacent_part_numbers) != 2:
        return 0
    return adjacent_part_numbers[0] * adjacent_part_numbers[1]


def part_two():
    total = 0
    for line_index in range(1, len(lines)-1):
        last_line = "."+lines[line_index-1]+"."
        line = "."+lines[line_index]+"."
        next_line = "."+lines[line_index+1]+"."

        for index in range(1, size-1):
            if line[index] == "*":
                total += gear_ratio(last_line, line, next_line, index)
    print("part2 total:", total)


part_one()
part_two()
