class Employee:
    a = 1
    def __init__(self):
        print("The Constructor of Employee")
class programmer(Employee):
    b = 2
    def __init__(self):
        print("The Constractor of Programmer")

class manager(programmer):
    c = 3
    def __init__(self):
        super().__init__()
        print("The Constructor of Manager")
# o = Employee()
# print(o.a)

# o = programmer()
# print(o.a, o.b)

# o = manager()
# print(o.a, o.b, o.c)