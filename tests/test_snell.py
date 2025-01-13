# contents of tests/test_snell.py

import numpy as np
import pytest
import sys

from example.refraction import snell, my_func


# For any indexes, a ray normal to the surface should not bend.
# We'll try a couple different combinations of indexes....

# pytestmark = pytest.mark.skip(reason="skip all module")

def test_perpendicular_1():
    actual = snell(0, 2.00, 3.00)
    assert actual == pytest.approx(0)


def test_perpendicular_2():
    actual = snell(0, 3.00, 2.00)
    assert actual == pytest.approx(0)

# @pytest.mark.skipif(False, reason="do not skip this test")
def test_air_water():
    n_air, n_water = 1.00, 1.33
    actual = snell(np.pi / 4, n_air, n_water)
    expected = 0.5605584137424605
    assert actual == pytest.approx(expected)

@pytest.fixture(params=[
    (1.00, 1.33),
    (1.33, 1.00),
])
def indexes(request):
    return request.param

def test_round_trip(indexes):
    n1, n2 = indexes
    angle = np.pi / 5
    actual = snell(snell(angle, n1, n2), n2, n1)
    assert actual == pytest.approx(angle)

@pytest.mark.skipif("sys.version_info >= (3, 8)")
def test_only_on_38plus():
    x = 3
    assert f"{x = }" == "x = 3"

# python -m pytest -ra --cov=example --cov-branch /mnt/vepfs/fs_users/yuliang/test_package/tests/
def test_my_func_success():
    assert my_func(1) == True

def test_my_func_failure():
    assert  my_func(-1) == False
