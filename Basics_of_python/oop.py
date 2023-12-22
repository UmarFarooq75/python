class Employee:
    def __init__(self, name, salary, description) -> None:
        self.name = name
        self.salary = salary
        self.description = description

    def getSalary(self):
        return self.salary

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def dataPushInFile(self):
        with open("./testingfiles/oop.txt", "a") as f:
            # Write headers if not already written
            f.write("Name\tSalary\tDescription\tSubEmployee\n")

            # Write employee data
            f.write(f"{self.name}\t{self.salary}\t{self.description}\n")


class SubEmployee(Employee):
    def __init__(self, name, salary, description, subemploye) -> None:
        super().__init__(name, salary, description)
        self.subemploye = subemploye

    def dataPushInFile(self):
        with open("./testingfiles/oop.txt", "a") as f:
            # Write employee data including subemployee attribute
            f.write(f"{self.name}\t{self.salary}\t{self.description}\t{self.subemploye}\n")


# Create instances of the Employee class
employees = [
    Employee("Umar", 555555, "Software Engineer with experience in React Native, ReactJS, Next.js, and Tailwind CSS."),
    Employee("John", 50000, "Web Developer with expertise in Python, Django, and JavaScript."),
    Employee("Alice", 60000, "Data Scientist specializing in machine learning and data analysis."),
    SubEmployee("Wick", 20000, "Data Scientist specializing in machine learning and data analysis.", True)
]

for emp in employees:
    emp.dataPushInFile()
