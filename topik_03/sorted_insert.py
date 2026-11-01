def find_insertion_position(values, value):
    left = 0
    right = len(values)

    while left < right:
        middle = (left + right) // 2
        if values[middle] < value:
            left = middle + 1
        else:
            right = middle

    return left
