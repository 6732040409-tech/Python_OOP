# ชื่อ ,เงินเดือน
class Employee: #การสร้าง class
   # สร้าง Method
    def detail(self, name, salary, department):
        # สร้าง Attribute
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

# Attribute เป็นกลไกที่กำหนดคุณสมบัดิให้กับ class
# การสร้าง Attribute
# self.name = ชื่อพนักงาน
    # self.salry = เงินเดือน
    # self.age = อายของหนักงาน
#Method เป็นกลไกที่กำหนดพฤกรรมให้กั class
# การสร้าง Method
#   def getName(self):
#       return self.name
# การเรียกใช้งาน
# ชื่อวัตถุ.getName

# คีย์เวิร์ด self
#    การใช้คีย์เวิร์ด self  จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เรราทำงานกับวัตถุใด
#    ให้บอกตัวตนของวัตถุนั้น ๆ เช่น การกำหนดคุณสมบัติต่าง ๆ ให้วัตถุ

# Constructor
#   เป็น method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
# โครงสร้าง Constructor
#   def __init__(self):
# การสร้างวัตถุ



emp1 = Employee()
emp1.detail("ชาลิสา", 50000, 'การเงิน' )
emp1.showData()

emp2 = Employee()
emp2.detail("สมศักดิ์", 25000, 'ฝ่ายขาย')
emp2.showData()

emp3 = Employee()
emp3.detail("เขียวจัน", 500, 'ปวส')
emp3.showData()