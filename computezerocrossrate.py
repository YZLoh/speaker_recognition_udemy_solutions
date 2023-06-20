def ComputeZeroCross(signal):
    """Compute the zero cross rate of the signal.

    Args:
        signal: a list of floating point numbers

    Returns:
        an integer for the number of zero cross in the signal
    """
    assert isinstance(signal, list)
    assert len(signal) &gt; 1

    # Add your code here
    
    zero_crossings = 0

    for i in range(1, len(signal)):
        if (signal[i] &gt;= 0 and signal[i - 1] &lt; 0) or (signal[i] &lt; 0 and signal[i - 1] &gt;= 0):
            zero_crossings += 1

    return zero_crossings