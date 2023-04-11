class ineuron:
    __students = "data science"

    def students(self):
        print("print the class of students",ineuron.__students)

i = ineuron()
i.students()
print(i._ineuron__students)

class ineuron1:
    __students = "data science"

    def students(self):
        print("print the class of students")

i = ineuron1()
i.students()
print(i._ineuron1__students)


list()