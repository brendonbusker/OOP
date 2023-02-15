from datetime import date

class Student:

    def __init__(self, id, n, dob, classif):
        self.__studentID = id
        self.__name = n
        self.__dateOfBirth = dob
        self.__classification = classif
        self.__age = 0
        self.__register = ""

    def determine_age(self):
        today = date.today()
        year = today.year

        self.__dateOfBirth = self.__dateOfBirth.split("/")
        dob_year = self.__dateOfBirth[2]

        self.__age = year - int(dob_year)

    def determine_register(self):
        if self.__classification == "F":
            self.__register = "4/10 - 4/12"

        elif self.__classification == "S":
            self.__register = "4/7 - 4/9"

        elif self.__classification == "Jr":
            self.__register = "4/4 - 4/6"

        elif self.__classification == "Sr":
            self.__register = "4/1 - 4/3"

        else:
            self.__register = "Classification invalid"

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_register(self):
        return self.__register
    




    
