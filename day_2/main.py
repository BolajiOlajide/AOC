# https://adventofcode.com/2020/day/2

def part1(data):
    count = 0

    for [_range, _character, text] in data:
        [lowerBound, upperBound] = list(map(int, _range.split('-')))
        character = _character[0]

        if (text.count(character) >= lowerBound) and (text.count(character) <= upperBound):
            count += 1

    return count


def part2(data):
    count = 0

    for [_range, _character, text] in data:
        [lowerBound, upperBound] = list(map(int, _range.split('-')))
        character = _character[0]

        first_index_correct = text[lowerBound - 1] == character
        second_index_correct = text[upperBound - 1] == character

        if first_index_correct != second_index_correct:
            count += 1

    return count


def fetch_data_from_source():
    with open('day_2/data.txt', 'r') as file:
        return list(map(lambda x: x.rstrip().split(' '), file))

if __name__ == '__main__':
    data = fetch_data_from_source()

    print('Part One: ', part1(data))
    print('Part Two: ', part2(data))