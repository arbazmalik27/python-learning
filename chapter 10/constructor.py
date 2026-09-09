class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("Employee created")
    
    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the company!")

arbaz = Employee("Arbaz", 1500000, "Python")
print(arbaz.name, arbaz.salary, arbaz.language)



