def filter_pairs(numbers, sum_filter=10):
    numbers_list = list(map(int, numbers))
    pairs = []
    while numbers_list:
        num = numbers_list.pop()
        diff = sum_filter - num
        if diff in numbers_list:
            pairs.append((diff, num))
    if not pairs:
        print("There are no numbers in the list that are equal to %s" % sum_filter)
    return pairs


def print_pairs(pairs):
    for a, b in pairs:
        print(str(a) + " + " + str(b))


if __name__ == '__main__':
    import sys

    print_pairs(filter_pairs(sys.argv[1:]))
