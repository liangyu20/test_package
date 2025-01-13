# contents of refraction.py

import numpy as np
import sys


def snell(theta_inc: float, n1: float, n2: float) -> float:
    """
    Compute the refraction angle using Snell's Law.

    See https://en.wikipedia.org/wiki/Snell%27s_law

    Parameters
    ----------
    theta_inc : float
        Incident angle in radians.
    n1, n2 : float
        The refractive index of medium of origin and destination medium.

    Returns
    -------
    theta : float
        refraction angle

    Examples
    --------
    A ray enters an air--water boundary at pi/4 radians (45 degrees).
    Compute exit angle.

    >>> snell(np.pi/4, 1.00, 1.33)
    0.5605584137424605
    """
    return np.arcsin(n1 / n2 * np.sin(theta_inc))

def my_func(param: int) -> bool:
    """
    function for branch coverage test

    Parameters
    ----------
    param : int

    Returns
    ----------
    True or False : bool
        True when param is greater than 0, otherwise False

    Examples
    ----------
    >>> my_func(1)
    True
    >>> my_func(0)
    False
    """
    if param > 0:
        return True
    else:
        return False