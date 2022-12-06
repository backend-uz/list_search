def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i = 0
    max = data[0]
    min = data[0]
    while i < len(data):
        if data[i] > max:
            max = data[i]
        if data[i] < min:
            min = data[i]
        
        i += 1

    return min + max
print(find_max_min_sum([3, 5, 9]))
