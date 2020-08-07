"""
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
"""



def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    merging = {}
    for i, x in enumerate(weights):
        if x in merging:
            merging[x] = merging[x] + [i]
        else:
            merging[x] = [i]
        for key1 in merging:
            key2 = limit - key1
            if len(merging[key1]) >1:
                if key1 * 2 == limit:
                    return (merging[key1][1], merging[key1][0])
            if key2 in merging:
                if key1 !=key2:
                    index1 = merging[key1][0]
                    index2 = merging[key2][0]
                    if index1 < index2:
                        return(index2, index1)
                    if index2 < index1:
                        return (index1, index2)
    return None
