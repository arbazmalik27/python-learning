class Employee:
    language = "Python" #This is a class attribute
    salary = 125000 

    def getInfo(self):
        print(f"Language: {self.language}")
        print(f"Salary: {self.salary}")

    #sometimes we need a function that does not use the self-parameter. we can defime a dtatic method like this
    @staticmethod
    def greet():
        print("Good Morning")


arbaz = Employee()
#arbaz.language = "Javascript" # This is an attribute
arbaz.greet()
arbaz.getInfo()
#Employee.getInfo(arbaz)


#self parameter 
# self refers to the instance of the class. it is automatically passed with a function call from an object.