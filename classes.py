class Flights():
    def __init__(self,capacity):
        self.capacity = capacity
        self.__passengers = []

    def add_passenger(self,passenger):
        if not self.open_seats():
            return False
        self.__passengers.append(passenger)
        return True

    def get_passengers(self):
        return self.__passengers

    def open_seats(self):
        return self.capacity - len(self.__passengers)


flight = Flights(3)
people = ["Harry","Hermione","Hagrid","Draco"]

for i in people:
    if flight.add_passenger(i):
        print(f"Added passenger {i} to the flight")
    else:
        print(f"Can not add {i} due to flight being full")
