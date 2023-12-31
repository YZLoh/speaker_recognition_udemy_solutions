import math

def FrequencyToMel(freq):
    """Convert frequency to mel.

    Args:
        freq: the frequency in Herz, a positive floating point number

    Returns:
        a positive floating point number
    """
    assert freq > 0

    # Add your code here
    mel = 2595 * math.log10(1 + (freq / 700))

    return mel