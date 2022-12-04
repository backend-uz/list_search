def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i = 0
    max = 0
    while i < len(data):
        if data[i] > max:
            max = data[i]
        i+=1
        index = data.index(max)
    return index
print(find_max_index([2,4,8,9]))
