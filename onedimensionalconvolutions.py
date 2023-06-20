'''
1-dimensional convolutions
Let's implement 1-dimensional convolutions in Python.

Given an input sequence, and a kernel, compute the convolution result.

Assume the stride is 1.
'''
def ComputeConvolution(seq, kernel):
    """Compute 1-dim convolution.

    Args:
        seq: a list of floating point numbers as inputs
        kernel: a list of floating point numbers as the convolution kernel

    Returns:
        the output sequence, which is a list of floating point numbers
    """
    assert isinstance(seq, list)
    assert isinstance(kernel, list)
    assert len(seq) > 2
    assert len(kernel) >= 2
    assert len(seq) >= len(kernel)

    output_seq = []
    kernel_length = len(kernel)
    seq_length = len(seq)

    for i in range(seq_length - kernel_length + 1):
        window = seq[i:i+kernel_length]
        result = sum(a * b for a, b in zip(window, kernel))
        output_seq.append(result)

    return output_seq