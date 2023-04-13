class car:

    def __init__(self,body,engine,tyre):
        self.body=body
        self.engine=engine
        self.tyre=tyre

    def mileage(self):
        print("mileage of this car")

c = car("solid","v6","radial")
print(c)

class tata(car):
    pass

altroz = tata("alpha","DCT",16)
print(altroz.body)
print(altroz.engine)
print(altroz.tyre)

class bank:
    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print("this will show your account open status")

    def deposit(self):
        print("this will show your deposited amount")


class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show all the transaction to icici through hdfc bank")


class icici(HDFC_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.account_opening()
i.transaction()
i.deposit()


class bank:
    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print("this will show your account open status")

    def deposit(self):
        print("this will show your deposited amount")

    def test(self):
        print("this is a test method from bank class")


class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transactions to icici through hdfc")

    def test(self):
        print("this is a test method from hdfc bank")


class ineuron_bank:
    def account_status_icici(self):
        print("print account status in icici")


class icici(bank,HDFC_bank,ineuron_bank):
    pass


i = icici()
i.test()


class ineuron:
    """"method overriding"""
    def student(self):
        print("print the details of all the students")

    def achievers(self):
        print("print the list of all the achievers")

    def hall_of_fame(self):
        print("print everyone from hall of fame")

class ineuron_vision(ineuron):

    def student(self):
        print("these are filtered student list")

iv = ineuron_vision()
iv.student()

class ineuron:
    __students = "data science"
    _barca = "camp nou"
    yob = 1899

    def student(self):
        print("print the class of students",ineuron.__students,ineuron._barca,ineuron.yob)

i = ineuron()
i.student()
print(i._ineuron__students)
print(i._barca)
print(i.yob)

class ineuron:
     def __init__(self):
         self.students1= "data science"

     def students(self):
         print(self.students1)

i = ineuron()
i.students()
i.students1 = "data analytics"
i.students()


class ineuron1:
    def __init__(self):
        self.__students1 = "data science"

    def students(self):
        print(self.__students1)

    def student_change(self,new_value):  #setter or setup function
        self.__students1=new_value



i1 = ineuron1()
i1.students()
i1.__students1 = "big data"
i1.students()
i1.student_change("data engineering")
i1.students()


class ineuron:
    def students(self):
        print("print a students details")

class class_type:
    def students(self):
        print("print the class type of students")

def ineuron_external(a):
    a.students()

i = ineuron()
j = class_type()
ineuron_external(i)
ineuron_external(j)
