class car:
    def __init__(self,body,engine,tyre):
        self.body=body
        self.engine=engine
        self.tyre=tyre

    def mileage(self):
        print("mileage of this car")

c=car("solid","v6","radial")
print(c)

class tata(car):
    pass

t = tata("solid","turbo","spoke")
print(t)
print(t.mileage())