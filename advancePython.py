#Dunder and magic method 
class Vector:
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y

    def __del__(self) -> None:
        pass # print("Object is being deleted")

    def __add__(self, other):
        return Vector(self.x +other.x, self.y+other.y)

    def __repr__(self):
        return f"{self.x} and {self.y}"

v1 = Vector(3, 22)
v2 = Vector(3, 22)

v3 = v1 + v2
print(v3)

# decorators 
def dec(func):
    def wrapper():
        func()
        print("i am decorating your function")
    return wrapper

@dec
def hello():
    print("hello world")
hello()

# generator 
def mygen(n): 
    for x in range(n):
        yield x ** 3 

values = mygen(900000)


print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

#args parsing 
import sys, getopt

print(sys.argv)

opts, args = getopt.getopt(sys.argv [1:], "f:m", ['filename', 'message'])
print(opts)
print(args)

#Encapsulation
class Person:
    def __init__(self,name, age):
        self.__age = age
        self.__name = name
    
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def myMethod():
        print("hello")


# type hinting 
def myFunction(param: str) -> str:
    print(param)
    return "print is completed"

myFunction("hello")

# factory design pattern
from abc import ABCMeta, abstractclassmethod, abstractmethod, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_method():
        """interface method"""

class Student(IPerson):
    def __init__(self):
        self.name = "bob"
    
    def person_method():
        print("I am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "mike"

    def person_method():
        print("I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "S":
             Student.person_method()
        if person_type == "T":
            Teacher.person_method()

#type = input("type")
#PersonFactory.build_person(type)

#Proxy Design Pattern 
class Person(IPerson):

    def person_method(self):
        print("I'm a person")

class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()
    
    def person_method(self):
        print("I am the proxy func")
        self.person.person_method()
p1 = ProxyPerson().person_method()
#Singleton Design Pattern

class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("name", 0) 
        return PersonSingleton.__instance
    
    def __init__(self,name,age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be created more than once")
        else:
            self.name = name    
            self.age = age
            PersonSingleton.__instance = self
    @staticmethod
    def person_method():
        print(f"{PersonSingleton.__instance.name}, {PersonSingleton.__instance.age}")

p = PersonSingleton("Saf", 12)
print(p)
p.person_method()

p1 = PersonSingleton.get_instance()
print(p1)
p1.person_method()

#Composite Design Pattern
class IDepartment(metaclass= ABCMeta):
    @abstractmethod
    def __init__(self, employee):
        """implemented in child class"""
    @abstractstaticmethod
    def print_department():
        """implemented in child class"""

class Accounting(IDepartment):
    
    def __init__(self, employee):
        self.employee = employee

    def print_department(self):
        print(f"Account department: {self.employee}")


class Development(IDepartment):
    
    def __init__(self, employee):
        self.employee = employee

    def print_department(self):
        print(f"Development department: {self.employee}")

class ParentDepartment(IDepartment):
    def __init__(self, employee):
        self.employee= employee
        self.base_employee= employee
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employee += dept.employee

    def print_department(self):

        print(f"Parent department base employee {self.base_employee}")
        print(f"Total number {self.employee}")
        for dept in self.sub_depts:
            print(dept)

dept1 = Accounting(200)
dept2 = Development(300)

dept3 = ParentDepartment(30)
dept3.add(dept1)
dept3.add(dept2)
dept3.print_department()

if __name__ == "__main__":
    print("advance python script here")