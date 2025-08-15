# เขียนโปรแกรมสร้าง class ชื่อ people โดยมี attribute และ Method ดังนี้
# attribute
#   name เป็นชื่อของบุคคล
#   age เป็นอายุของบุคคล
# method
#   Introduce() เมื่อเรีอกใช้จะพมพ์ข้อความ
#   My name is <name>. I'm <age> year old

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Introduce(self):
        return print("My name is {}. I'm {} year old".format(self.name,self.age))

p1=people("Chalisa",20)
p1.Introduce()

