# file: pairs.py
# https://bohdan-lesiv.github.io/omnomnom/python-01.html


# this was very tricky
def filter_pairs(numbers, sum_filter = 10): 
    pairs = []
    numbers_list = []
    for string in numbers:
        numbers_list.append(int(string))
    while numbers_list:
        num = numbers_list.pop()
        diff = sum_filter - num
        if diff in numbers_list:
            pairs.append((diff, num))      
    return pairs


def print_pairs(pairs):
    for pair in pairs:
        print(pair[0],"+",pair[1])


# main block
if __name__ == '__main__':
    import sys
    print_pairs(filter_pairs(sys.argv[1:]))