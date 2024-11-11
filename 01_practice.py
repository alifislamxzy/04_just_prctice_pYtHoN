st = "This is new line for this file"
with open('file.txt', 'w') as f:
    date = f.write(st)
    print(date)
    f.close()

class employee:

    def __init__(self, nam):
        self.nam = nam
        print(f"Good morning {self.nam}")
    
    name = "Alif"
    def getInfo(self):
        print(f"Good Day, {self.name} ")

a = employee("Apon")
a.getInfo()