cddef printHair(info):
    pass

class Person: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def printInformation(self):
        print(f"name:{self.name} age:{self.age}")

class Grad(Person):
    def __init__(self, name, age, degree):
        super().__init__(name, age)
        self.degree = degree
    def printDegree(self):
        print(self.degree)

class PHD(Grad):
    def __init__(self, name, age, degree, master, phd):
        super().__init__(name, age, degree)
        self.master = master
        self.phd = phd

class SoftwareDev(Person):
    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

    def getAccess(self):
        return "VCSe, Git, ..."

#person -> grad -> phd 
#  -> schoolBoy


m1 = Person("Bob", 21).printInformation()

g1 = Grad("Sam",34,"Dnt")
g1.printDegree()
g1.printInformation()

s1 = SoftwareDev("s345", 12, "math")

print(s1.getAccess())