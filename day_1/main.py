# Question: https://adventofcode.com/2020/day/1
import itertools


def part1(data):
    for a, b in itertools.product(data, repeat=2):
        if a + b == 2020:
            return a * b

    return 0


def part2(data):
    for a, b, c in itertools.product(data, repeat=3):
        if a + b + c == 2020:
            return a * b * c

    return 0


def fetch_data_from_source():
    with open('day_1/data.txt', 'r') as file:
        return list(map(int, file))


if __name__ == '__main__':
    data = fetch_data_from_source()

    print('Part One: ', part1(data))
    print('Part Two: ', part2(data))