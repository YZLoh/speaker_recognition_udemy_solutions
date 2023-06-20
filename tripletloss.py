def ComputeTripletLess(anchor, pos, neg, alpha):
    """Compute the tripless loss.

    Args:
        anchor: embedding of the anchor sample, which is a list of floating
            point numbers
        pos: embedding of the positive sample, which is a list of floating
            point numbers
        neg: embedding of the negative sample, which is a list of floating
            point numbers
        alpha: a non-negative number for the margin value

    Returns:
        the loss, which is a floating point number
    """
    assert isinstance(anchor, list)
    assert isinstance(pos, list)
    assert isinstance(neg, list)
    assert len(anchor) == len(pos)
    assert len(anchor) == len(neg)
    assert len(anchor) > 1
    assert alpha >= 0

    # Add your code here
    distance_pos = sum([(a - p) ** 2 for a, p in zip(anchor, pos)])
    distance_neg = sum([(a - n) ** 2 for a, n in zip(anchor, neg)])
    loss = max(distance_pos - distance_neg + alpha, 0.0)

    return loss