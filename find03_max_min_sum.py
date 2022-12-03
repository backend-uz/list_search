def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i = 0
    max = 0
    min = 0
    while i < len(data):
        if data[i] > max:
            max = data[i]

        if data[i] < min:
            min += 1
        i+=1   

    return max+min
