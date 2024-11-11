class Employee:
    companey = 'Google' # This is Class Attribute

alif = Employee() # This is Object 
alif.companey = 'FaceBook' # This is Object Attribute or inctace Attribute
print(alif.companey)# print this object

class name:# This is class 

    def __init__(self): # This is python dunder method
         print("Hello")
        
    @staticmethod
    def goodday():
        print("Good Morning")
    
        
n = name()
n.goodday()

def getInfo(): 
        x = input("what's you x") # User print x number
        y = input("what's your y") # User print y number
        if x<y: # comparetion x less-than y
            print("x less-than y")# print x less-than y
        else: # Else add
            print("x greater-than y") # print x greater-than y

getInfo()# This is function call
