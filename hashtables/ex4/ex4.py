import math
"""
Input
[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
Return Value
[ 1, 3, 4 ]
"""
def has_negatives(a):
    #Your Code Here
    positive = {}
    negative = {}
    result = []
    for number in a:
        if number > 0:
            positive[number] = -number
        if number < 0:
            negative[number] = number * -1
    for key in positive:
        if positive[key] in negative:
            result.append(key)
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
