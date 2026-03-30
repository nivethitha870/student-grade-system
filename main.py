from student import Student
from grade import calculate_grade
from utils import validate_marks

marks=[85,90,80]

validate_marks(marks)

s=Student("Radha",marks)

avg=s.average()

grade=calculate_grade(avg)

print("Average:",avg)

print("Grade:",grade)
