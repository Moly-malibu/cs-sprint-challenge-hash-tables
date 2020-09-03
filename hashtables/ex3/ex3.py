"""
[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]
"""

def intersection(arrays):
    #Your Code Here
    result = []
    dict_acount = {}
    for number in arrays[0]:
        dict_acount[number] = 1
    for array in arrays[1:]:
        for number in array:
            if number in dict_acount:
                dict_acount[number] += 1
    for key in dict_acount:
        if dict_acount[key] == len(arrays):
            result.append(key)
    return result
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
