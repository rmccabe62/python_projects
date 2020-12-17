

# create parent class
class Student:
    studentName = 'No name provided'
    email = ' '
    password = 'password1'
    major = ' '
    
# create first child class for parent
class Teacher(Student):
    subject = 'Math'
    semester = 'Spring'

# create second child class for parent
class GPA(Student):
    testAvg = 'B'
    attendance = 'Satisfactory'

    
    
