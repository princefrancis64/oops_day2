class ineuron:
    def student(self):
        print("print the details of all the students")

    def achievers(self):
        print("print the list of all the achievers")

    def hall_of_fame(self):
        print("print everyone from hall of fame")


class ineuron_vision(ineuron):

    def student(self):
        print("these are the filtered student list")
iv = ineuron_vision()
iv.student()