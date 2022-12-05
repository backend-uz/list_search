def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i = 0
    mx = 0
    while i < len(data):
        if data[i] > mx:
            if data[i] % 2 == 0:
                mx = data[i]
        i += 1
    return mx
print(find_max_even([-1,9,7,-8,6]))
