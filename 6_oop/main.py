class Student:
  # Static Property/Attribute
  count = 0
  
  # Constructor
  def __init__(self):
    Student.count = Student.count + 1

  # Static methods
  @staticmethod
  def print_count():
    print("The total student is:", Student.count)

ashvik = Student()
amulya = Student()

Student.print_count()
