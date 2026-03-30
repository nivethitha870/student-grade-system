import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from student import Student

@pytest.fixture
def sample_student():

    return Student("Test",[70,80,90])

def test_average(sample_student):

    assert sample_student.average()==80
