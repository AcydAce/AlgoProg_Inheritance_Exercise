class person:
    def __init__(self, name="", address=""):
        self.__name = name
        self.__address = address

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setaddress(self, address):
        self.__address = address

    def getaddress(self):
        return self.__address

    def __str__(self):
        return self.getname(), self.getaddress()


class student:
    def __init__(self, name="", address="", grade=""):
        super().__init__(name, address)
        self.setgrade(grade)

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setaddress(self, address):
        self.address = address

    def getaddress(self):
        return self.address

    def setgrade(self, grade):
        self.__grade = grade

    def getgrade(self):
        return self.__grade

    def __str__(self):
        return super().__str__() + "student : ".format(self.getname()(self.getaddress()))

    def displaystudent(self):
        print(self.name(self.address))


class teacher:
    def __init__(self, name, address, course):
        super().__init__(name, address)
        self.__course = course

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setaddress(self, address):
        self.address = address

    def getaddress(self):
        return self.address

    def setcourse(self, course):
        self.__course = course

    def getcourse(self):
        return self.__course

    def __str__(self):
        return super().__str__() + "teacher : ".format(self.getname()(self.getaddress()))

    def displayteacher(self):
        print(self.name(self.address))


student().setname("me")
student().setaddress("place")
