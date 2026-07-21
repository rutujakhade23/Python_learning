class Student:
    # subject = "Python"
    # college = "ABC"
    # year = "4th year"
    college_name = "ABC college" #class attribute

    def __init__(self):  
        print("obj is being constructed")


    def __init__(self, name, cgpa):   #parametrized constructor
        self.name = name    #instance attribute
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa


stu1 = Student("Rutuja", 9.2)
stu2 = Student("Swaraj", 9.8)
print(stu1.name, stu1.cgpa)
print(stu2.name, stu2.cgpa)
# print(stu1.subject, stu1.college, stu1.year)
# print(type(stu1))

print(f"{stu2.name} has cgpa = {stu2.get_cgpa()}")

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage) :
        self.RAM = RAM
        self.storage = storage

    @classmethod    #class method 
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self): #instace method 
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod    #static method
    def discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"discounted price = {final_price}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb","256gb")

l1.get_info()

l1.get_storage_type()

l1.discount(40_000, 10)

#practice Problem : Product Store ....That store products 

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):  #instance method
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod 
    def calc_discount(price, discount):
        print(f"discounted price = {price - (price * discount / 100)}")

p1 = Product("phone", 10_000)
p2 = Product("Laptop", 50_000)
p3 = Product("pen", 10)

p1.get_info()
p3.get_info()

Product.get_count()

p1.calc_discount(10_000, 12)


class BankAccount:
    def __init__(self, name, balance):
        self.name = name #public
        self.__balance = balance #private --- data mangling
    def get_balance(self):  #getter
        return self.__balance


acc1 = BankAccount("Rahul Kumar", 100_000)

print(acc1.name, acc1.get_balance())

class Employee:
    start_time = "10am"
    end_time = "6pm"

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

t1 = Teacher("Math")
print(t1.subject, t1.start_time, t1.end_time)

staff1 = AdminStaff("manager")
print(staff1.role, staff1.start_time, staff1.end_time)
