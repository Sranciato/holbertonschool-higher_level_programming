#!/usr/bin/python3
"""Returns multiplied matrices

args: m_a, m_b

"""


def lazy_matrix_mul(m_a, m_b):
    """
    Returns multipled matrices
    """
    import numpy as np

    result = np.dot(m_a, m_b)

    return result
