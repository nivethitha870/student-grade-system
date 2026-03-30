def validate_marks(marks):

    for m in marks:

        if m<0 or m>100:
            raise ValueError("Invalid Marks")

    return True
