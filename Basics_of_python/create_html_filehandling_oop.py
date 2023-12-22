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
        with open("./testingfiles/oop.html", "a") as f:
            # Write employee data as an HTML row
            f.write(f"<tr><td>{self.name}</td><td>{self.salary}</td><td>{self.description}</td><td></td></tr>\n")


class SubEmployee(Employee):
    def __init__(self, name, salary, description, subemploye) -> None:
        super().__init__(name, salary, description)
        self.subemploye = subemploye

    def dataPushInFile(self):
        with open("./testingfiles/oop.html", "a") as f:
            # Write employee data as an HTML row, including subemployee attribute
            f.write(f"<tr><td>{self.name}</td><td>{self.salary}</td><td>{self.description}</td><td>{self.subemploye}</td></tr>\n")


# Create instances of the Employee class
employees = [
    Employee("Umar", 555555, "Software Engineer with experience in React Native, ReactJS, Next.js, and Tailwind CSS."),
    Employee("John", 50000, "Web Developer with expertise in Python, Django, and JavaScript."),
    Employee("Alice", 60000, "Data Scientist specializing in machine learning and data analysis."),
    SubEmployee("Wick", 20000, "Data Scientist specializing in machine learning and data analysis.", True)
]

# Write the HTML table start tag and headers with center alignment
with open("./testingfiles/oop.html", "w") as f:
    f.write("<div style='display: flex; justify-content: center; align-items: center;'>")
    f.write("<table border='1' style='margin: auto;'>")
    f.write("<tr style='background-color: yellow'><th>Name</th><th>Salary</th><th>Description</th><th>SubEmployee</th></tr>")

# Write data to the file for each employee
for emp in employees:
    emp.dataPushInFile()

# Write the HTML table end tag
with open("./testingfiles/oop.html", "a") as f:
    f.write("</table>")
    f.write("</div>")
