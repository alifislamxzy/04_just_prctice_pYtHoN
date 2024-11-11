class programmer:
    language = "Python"
    name = "Apon"
    def getInfo(self):
        print(f"The programmer name is {self.name}, Her programming language is {self.language}")

class coder:
    languag = "JavaScript"
    nam = "Alif"
    def show(self):
        print(f"The Programmer name is {self.nam}. Her language is {self.languag}")

class Employee(programmer, coder):
    companey = "Meta"
    salary = 1200000
    def job(self):
        print(f"The companey name is {self.companey}. The Salary is {self.salary}")

b = Employee()

b.getInfo()
b.show()
b.job()