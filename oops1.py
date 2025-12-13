class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"

    def travel(self,destination):
        print(f"Employee is now traveling to {destination}")

#creating an object of class
sam = employee()

sam.travel("Kerala")