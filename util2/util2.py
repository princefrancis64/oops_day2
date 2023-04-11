class Person2:

    def __init__(self,name,surname,yob):
        self._name1=name
        self.__surname1=surname
        self.yob1=yob

barca=Person2("spotify","camp nou",1899)
print(barca._name1)
print(barca._Person2__surname1)
print(barca._name1 + barca._Person2__surname1)