# count total by taking first and last digit and concatenating them before adding to total
def count_total(lines):
    total = 0
    for line in lines:
        for index in range(len(line)):
            if line[index].isdigit():
                first = line[index]
                break

        for index in range(len(line)-1, -1, -1):
            if line[index].isdigit():
                last = line[index]
                break

        current = str(first) + str(last)
        total += int(current)
    return total


def part_one():
    # read file
    filename = "input.txt"
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    total = count_total(lines)
    print("part1 total:", total)


def part_two():
    # read file
    filename = "input.txt"
    with open(filename) as file:
        filestring = file.read()

    # translation dictonary
    # each translation has the numeric symbol and the first and last letter of each word, so it don't lose numbers like in the following case
    # oneight should be 18, not 11 (1 ight)
    trans = {"one": "o1e",
             "two": "t2o",
             "three": "t3e",
             "four": "f4r",
             "five": "f5e",
             "six": "s6x",
             "seven": "s7n",
             "eight": "e8t",
             "nine": "n9e",
             }

    # prepare the input to count by translating written numbers to their numeric form
    for key, value in trans.items():
        filestring = filestring.replace(key, value)

    total = count_total(filestring.split("\n"))
    print("part2 total:", total)


part_one()

part_two()
