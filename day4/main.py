filename = "input.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]


def part_one():
    total = 0
    for line in lines:
        numbers = line.split(":")[1]
        numbers = numbers.split("|")

        winning_numbers = numbers[0].split()
        my_numbers = numbers[1].split()

        quantity = len(winning_numbers) + len(my_numbers)
        collection = set(winning_numbers)
        collection = collection.union(set(my_numbers))
        num_of_winning_numbers = quantity - len(collection)
        if num_of_winning_numbers > 0:
            total += 2**(num_of_winning_numbers-1)
    print("part1 total:", total)


def add_to_queue(queue, num_of_winning_numbers, current_quantity):
    initial_queue_len = len(queue)
    i = 0
    while i < num_of_winning_numbers:
        if i < initial_queue_len:
            queue[i] += current_quantity
        else:
            queue.append(current_quantity)
        i += 1
    return queue


def part_two():
    queue = []
    total = 0
    for line in lines:
        current_quantity = 1
        if len(queue) != 0:
            current_quantity += queue.pop(0)

        total += current_quantity

        game = line.split(":")[0]
        game_number = game.split()[1]

        numbers = line.split(":")[1]
        numbers = numbers.split("|")

        winning_numbers = numbers[0].split()
        my_numbers = numbers[1].split()

        quantity = len(winning_numbers) + len(my_numbers)
        collection = set(winning_numbers)
        collection = collection.union(set(my_numbers))
        num_of_winning_numbers = quantity - len(collection)

        queue = add_to_queue(queue, num_of_winning_numbers, current_quantity)
    print("part2 total:", total)


part_one()
part_two()
