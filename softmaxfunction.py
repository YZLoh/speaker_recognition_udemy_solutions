import math

def ComputeSoftmax(vec):
    """Compute the softmax of a vector.

    Args:
        vec: a list of floating point numbers

    Returns:
        a list of floating point numbers with the same length as vec
    """
    assert isinstance(vec, list)
    assert len(vec) > 1

    # Find the maximum value in the vector
    max_val = max(vec)

    # Subtract the maximum value from each element in the vector (softmax shift)
    shifted_vec = [x - max_val for x in vec]

    # Compute the exponential of each shifted element in the vector
    exp_vec = [math.exp(x) for x in shifted_vec]

    # Compute the sum of all exponential values
    exp_sum = sum(exp_vec)

    # Compute the softmax values by dividing each exponential value by the sum
    softmax_vec = [x / exp_sum for x in exp_vec]

    return softmax_vec