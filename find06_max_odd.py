def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i = 0
    mx = 0
    while i >len(data):
        if data[i] > mx:
            if data[i] % 2 != 0:
                mx = data[i]
        i += 1
    return mx