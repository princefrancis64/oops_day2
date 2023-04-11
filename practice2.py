class Person4:
    _name="Manchester"
    __surname="United"
    yob=1878


    def age(self,current_year):
        return current_year-self.yob

    def age1(self,current_year):
        return current_year-self.yob


obj=Person4()
print(obj.age(2023))
print(obj.age1(2023))


class player(Person4):
    _name="Cristiano"
    __surname="Ronaldo"
    yob=1985

obj1=player()
print(obj1.age(2023))
print(obj1.age1(2023))

