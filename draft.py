import itertools
import numpy as np


def get_combinations(arr):
    """
    Get all the combinations and permutations of the given array
    """
    # get all combinations
    all_combinations = [("".join(map(str, v)) + "0" * len(arr))[:len(arr)] for l in range(2, len(arr) + 1) for v in
                        list(itertools.combinations(arr, l))]

    # get all permutations
    all_permutations = np.unique(["".join(permutation) for combination in all_combinations for permutation in
                                  itertools.permutations(combination)])

    return all_permutations

arr = [1,2,3,4,5,6,7,8]
combinations = get_combinations(arr)
print(len(combinations))

