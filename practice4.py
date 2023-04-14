import logging
logging.basicConfig(filename="practice4.log",level = logging.INFO,format= "%(levelname)s %(name)s %(asctime)s %(message)s")


class ineuron:
    def __init__(self,students,courses,internhip):
        """" this is a constructor for students, courses and internhip at ineuron"""
        logging.info("this is a constructor for ineuron course details and number of students enrolled")
        self.students =students
        self.courses = courses
        self.internship = internhip


ds=ineuron(159,"50+", "yes provided")
data_engin=ineuron(300,"10+","yes")
data_analytics = ineuron(300,"5+","yes")

print(ds.students)
print(data_engin.courses)


class courses:
    logging.info("this is a list of internship courses in ineuron")
    def data_science(self):
        logging.info("data science course is offered")
    def data_engineering(self):
        logging.info("data engineering course is offered")
    def data_analytics(self):
        logging.info("data analytics course is offered")

class internship(courses):
    pass

i = internship()
i.data_science()
i.data_engineering()
i.data_analytics()


class ineuron:
    logging.info("this is an example to show the private, protected and public variable")
    __income = 124235235
    _affiliates = "Physics waala"
    jobs_offered = 'onsite placement'

    def income(self):
        logging.info("the income of the ineuron per year is %s",ineuron.__income)

    def affiliates(self):
        logging.info("the affiliate of the ineuron is %s",ineuron._affiliates)

    def jobs_offered1(self):
        logging.info("the placement offered is %s",ineuron.jobs_offered)
i = ineuron()
i.income()
i.affiliates()
i.jobs_offered1()


class ineuron():
    logging.info("this is an example to show the abstraction method")


    def income(self):
        v = int(input("enter the income of ineuron in the year 2022"))
        logging.info("the income of ineuron in Rupees is %s",v)

i = ineuron()
try:
    i.income()
except Exception as e:
    logging.error(e)
    logging.exception(e)



class jobs:
    logging.info("this is an example to show the encapsulation process")
    __position = "data science"

    def position(self):
        logging.info(self.__position)

    def position_change(self):   #setter or setup function
        self.__position="data analytics"

i = jobs()
i.position()
i.position_change()
i.position()


class students:
    logging.info("this is a class to show the polymorphism method ")
    def course(self):
        logging.info("this is to show the course taken by student in 2022")


class students1:
    def course(self):
        logging.info("this is to show the course taken by student in 2023")


def ineuron_external(a):
    a.course()

i = students()
v = students1()

ineuron_external(i)
ineuron_external(v)



class players:
    logging.info("this is an example to show the method overriding")

    def players(self):
        logging.info("this is the list of all the players in the team")

class ballondr:
    def players(self):
        logging.info("this is the list of all the players who won ballond'r")

i = ballondr()
i.players()