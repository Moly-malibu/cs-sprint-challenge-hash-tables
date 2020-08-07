"""
IN
[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]
OUT
[1, 2]
"""

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dictionary = {}
    result = []

    for number in arrays[0]:
        dictionary[number] = 1
    for array in arrays[1:]:
        for number in array:
            if number in dictionary:
                dictionary[number] += 1
    for key in dictionary:
        if dictionary[key] == len(arrays):
            result.append(key)
    return result
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
