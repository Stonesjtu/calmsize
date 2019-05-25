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
    assert '{:.2f}'.format(size(12345678)) == '11.77M'

def test_round():
    assert size(12345678) == '12M'

def test_compare():
    assert size(-10240) == '-10K'
    with pytest.raises(NotImplementedError) as e:
        size(-10241) < '-10K'
    with pytest.raises(NotImplementedError) as e:
        size(-10241) > '-10K'

    assert size(-10241) < size(-10240)
    assert size(-10241) > -10240
    assert size(-10241) > -10240.888

