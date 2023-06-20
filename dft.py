'''
Discrete Fourier Transform
Given a sequence, compute its Discrete Fourier Transform (DFT).

You don't need to worry about the efficiency for now.

Hints:

Use the built-in complex() function to get complex numbers.

Use the cmath module for mathematical functions for complex numbers.
'''
import cmath

def ComputeDFT(seq):
    """Compute Discrete Fourier Transform of a sequence.

    Args:
        seq: a list of floating point numbers

    Returns:
        a list of complex numbers
    """
    assert isinstance(seq, list)
    assert len(seq) &gt; 2

    # Add your code here
  
    N = len(seq)
    dft = []

    for k in range(N):
        sum_val = 0
        for n in range(N):
            angle = 2j * cmath.pi * k * n / N
            sum_val += seq[n] * cmath.exp(-angle)
        dft.append(sum_val)

    return dft