"""
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
"""

#finds two items whose sum of weights equals the weight limit

two items whose sum of weights equals the weight limi
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    merging = {}
    for i, item in enumerate(weights):
        if item in merging:
            merging[item] = merging[item] + [i]
        else:
            merging[item] = [i]
        for key_1 in merging:
            key_2 = limit - key_1
            if len(merging[key_1]) >1:
                if key_1 * 2 == limit:
                    return (merging[key_1][1], merging[key_1][0])
            if key_2 in merging:
                if key_1 !=key_2:
                    index_1 = merging[key_1][0]
                    index_2 = merging[key_2][0]
                    if index_1 < index_2:
                        return(index_2, index_1)
                    if index_2 < index_1:
                        return (index_1, index_2)
    return None
