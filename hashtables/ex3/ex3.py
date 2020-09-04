"""
[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]
"""

def intersection(arrays):
    """
    YOUR CODE HERE
    """ 
    result = []
    cache = {}
    for number in arrays[0]:
        cache[number] = 1
    for array in arrays[1:]:
        for number in array:
            if number in cache:
                cache[number] += 1
    for key in cache:
        if cache[key] == len(arrays):
            result.append(key)
    return result
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
