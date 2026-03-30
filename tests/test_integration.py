from student import Student
from grade import calculate_grade
from utils import validate_marks

def test_full_system():

    marks=[80,85,90]

    validate_marks(marks)

    s=Student("Test",marks)

    avg=s.average()

    grade=calculate_grade(avg)

    assert grade=="B"
