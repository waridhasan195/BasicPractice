class Student:
    Name = '',
    Age = '',
    Department = '',
    Student_Id = '',

    #Constructor
    def __init__(self, name, age, department, studentId):
        self.Name = name
        self.Age = age
        self.Department = department
        self.Student_Id = studentId

    # def setData(self, name, age, department, studentId):
    #     self.Name = name
    #     self.Age = age
    #     self.Department = department
    #     self.Student_Id = studentId
    
    def displayData(self):
        print(f"Name: {self.Name} \nAge: {self.Age} \nDepartment: {self.Department} \nStudent ID: {self.Student_Id}")



student = Student('Tamim', 20, 'SWE', '161-15-7142')
# student.setData('Tamim', 20, 'SWE', '161-15-7142')
student.displayData()
