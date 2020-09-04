import math
"""
Input
[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
Return Value
[ 1, 3, 4 ]
"""
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    join = {}
    result = []
    for number in a:
        if join.get(abs(number)):
            if(join.get(abs(number))+number)==0:
                result.append(abs(number))
        else:
            join[abs(number)] = number
    return result 

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
