class Employee:
    a = 4  # Class attribute

    @classmethod
    def name(cls):
        print(f"The class attribute 'a' is {cls.a}")

n = Employee()  # Create an instance of Employee
n.a = 2  # Create an instance attribute 'a' specific to this instance

# Access instance attribute
print("Instance attribute 'a':", n.a)  # This will print 2

# Access class attribute
print("Class attribute 'a':", Employee.a)  # This will print 4

# Call the class method
n.name()  # This will print "The class attribute 'a' is 4"
