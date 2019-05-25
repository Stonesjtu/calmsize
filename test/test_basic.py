import pytest
from calmsize import size, ByteSize

def test_basics():
    assert size(10) == '10B'
    assert size(1024) == '1K'
    assert size(1024 * 1024 * 10) == '10M'

def test_neg():
    assert size(-10) == '-10B'
    assert size(-1024) == '-1K'
    assert size(-1024 * 1024 * 10) == '-10M'

def test_format():
    bs = ByteSize(12345678)
    assert '{:.2f}'.format(bs) == '11.77M'

def test_round():
    assert size(12345678) == '12M'
