# Getter / Setter method
# Setter การกำหนดค่าให้ object
# Setter การดึงค่าให้ object

# Ex_Setter
    # def setName(self, newname):
    #   Self.__name = newname
# Ex_Getter
    # def getName(self):
    #   return self.__name

class Employee:
    def __init__(self, name, salary, department):
        # private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

    # private method
    def showData(self):
        print('ชื่อพนักงาน = {}' + self.getName())
        print('เงินเดือน = {}' + self.getSalary())
        print('แผนก = {}' + self.getDepartment())

    # setter method
    def setName(self, newneme):
        self.__name = newneme
    def setSalary(self, newdeprtment):
        self.__department = newdeprtment

        # getter method
    def getName(self):
            return self.__name
    def getSalary(self):
            return self.__salary
    def getDepartment(self):
            return self.__department


emp1 = Employee('ชาลิสา', 50000, 'วิชาการ')
print('พนักงานดีเด่นประจำปี = {}'.format((emp1.getName())))
print('เงินเดือน = {}'.format(emp1.getName()))
print('แผนก = {}'.format(emp1.getDepartment()))