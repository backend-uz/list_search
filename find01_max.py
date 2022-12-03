def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i = 0
    max = 0
    while i < len(data):
        if data[i] > max:
            max = data[i]
        i+=1

    return max
print(find_max([1,7,3]))