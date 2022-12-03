def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i = 0
    max = 0
    while i < len(data):
        if data[i] > max:
            max = data[i]
        i+=1
        c = data.count(max)
    return c
print(find_max_count([1,2,4,4]))
