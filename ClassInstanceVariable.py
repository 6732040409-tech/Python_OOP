# ClassInstanceVariable

# Class Variable คือ ตัวแปรที่ทำงานภายใน Class
# ส่วนอื่นสามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attribute)
# โดยไม่จำเป็นต่องสร้าง Object ขึ้นมา

# Instance Variable คือตัวแปรที่ทำงานภายใน Object
# สามารถเข้าถึงข้อมูลส่วนนี้โดยต้องสร้าง Object ขึ้นมา

# class Variable
class Employee:
    _minSalary = 12000
    _minSalary = 50000
    _companyName = 'บริษัท XYZ จำกัด'

    def __init__(self, name, salary, department):
        #instance Variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    def showData(self):
        print('ชื่อพนักงาน = {}' + self.__name)
        print('เงินเดือน = {}' + self.__salary)
        print('แผนก = {}' + self.__department)

emp1 = Employee('ชาลิสา', 50000, 'วิชาการ')
print('เงินเดือนขั้นต่ำ ' + str(Employee._minSalary))
print(Employee._companyName)