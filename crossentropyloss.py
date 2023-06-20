'''
Cross entropy loss
Given two vectors p and q, for the reference and hypothesis, respectively.

The reference is a one-hot vector. The hypothesis is a probability distribution of N-classes.

Let's compute the cross entropy loss between p and q.

Note: Computing the cross entropy requires us to compute the log function. How do we avoid calling the log function on 0?
'''

import math

def ComputeCrossEntropy(p, q):
    """Compute the cross entropy between two distributions..

    Args:
        p: the reference, a list of floating point numbers, which is a
            one-hot vector
        q: the hypothesis, a list of floating point numbers, which are all
            non-negative and sum to 1

    Returns:
        a floating point number for the cross entropy
    """
    assert isinstance(p, list)
    assert isinstance(q, list)
    # p is a one-hot vector
    assert len(p) > 1
    assert sum(p) == 1
    assert min(p) == 0
    assert max(p) == 1
    # q is a probability
    assert sum(q) == 1
    assert len(q) == len(p)
    assert min(q) >= 0

    # Compute the cross entropy
    cross_entropy = -sum([p_i * math.log(q_i + 1e-9) for p_i, q_i in zip(p, q) if p_i > 0])

    return cross_entropy