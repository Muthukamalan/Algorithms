# Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.


def solution1(array: list[int]) -> int:
    array_length = len(array)

    for i in range(array_length):
        pair = False
        for j in range(array_length):
            if array[i] == array[j]:
                pair = True

        if not pair:
            return array[i]

    return -1


def solution2(array: list[int]) -> int:
    lookup = dict()  # element:: frequency

    for i in array:
        if i in lookup.get(i, 0):
            lookup[i] = 1  # init frequency
        else:
            lookup[i] += 1  # update frequency

    for ele, freq in lookup.items():
        if freq < 2:
            return ele
    else:
        return -1


def solution3(array: list[int]) -> int:
    odd_value = 0
    for ele in array:
        odd_value = odd_value ^ ele
    return odd_value
