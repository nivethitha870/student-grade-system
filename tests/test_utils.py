import pytest
from utils import validate_marks

def test_valid_marks():

    assert validate_marks([50,60,70])==True

def test_invalid_marks():

    with pytest.raises(ValueError):

        validate_marks([120,50])
