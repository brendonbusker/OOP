import random

class Insect:


    def wingsNum(self):
        self.wings = 2

    def legsNum(self):
        self.legs = 4

    def flight_len(self):
        self.flight = random.randint(1, 10)

    def get_flight_len(self):
        return self.flight