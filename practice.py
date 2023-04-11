from util2.util2 import Person2

real = Person2("real","madrid",1902)
print(real._name1)
print(real._Person2__surname1)


class Person3:

    def __init__(self,name,surname,yob):
        self._name1=name
        self.__surname1=surname
        self.yob1=yob

barca=Person3("spotify","camp nou",1899)
print(barca._name1)
print(barca._Person3__surname1)
print(barca._name1 + barca._Person3__surname1)