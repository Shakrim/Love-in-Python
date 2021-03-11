""" My vehicle code"""
import random

#Define a vehicle class
class Vehicle:
    def __init__(self, make = "unknown", model = "unknown", year = "unknown", weight = "unknown", needs_maintenance = False, trips_since_maintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maintenance = needs_maintenance
        self.trips_since_maintenance = trips_since_maintenance

#Setters: take in variable and set the variable
    def Set_Manufacture(self, make):
        self.make = make

    def Set_Model(self, model):
        self.model = model

    def Set_Year(self, year):
        self.year = year

    def Set_Weight(self, weight):
        self.weight = weight
#Getters: return variables
    def Get_Manufacture(self):
        return self.make

    def Get_Model(self):
        return self.model

    def Get_Year(self):
        return self.year

    def Get_Weight(self):
        return self.weight

    def Repair(self):
        self.trips_since_maintenance = 0
        self.needs_maintenance = False

class Cars(Vehicle):

    def __init__(self, make = "unknown", model = "unknown", year = "unknown", weight = "unknown", is_driving = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.is_driving = is_driving

    def Drive(self):
        self.is_driving = True

    def Stop(self):
        if self.is_driving:
            self.trips_since_maintenance += 1
            if self.trips_since_maintenance > 100:
                self.needs_maintenance = True
        self.is_driving = False


#drive and stop car random no of times
def Journey(car):
    drive_times = random.randint(1, 200)
    for i in range(drive_times):
        car.Drive()
        car.Stop()

#printing my cars
car1 = Cars("Renault", "Megane", 2018, 1220)
car2 = Cars("Renault", "Talisman", 2019, 1543)
car3 = Cars("Renault", "Coleos", 2020, 1703)

Journey(car1)
Journey(car2)
Journey(car3)


my_cars = [car1, car2, car3]
for i, car in enumerate(my_cars,1):
    print(f"""
    {i}.car 
    Manufacturer: {car.make}
    Model: {car.model}
    year {car.year}
    weight {car.weight}
    need for maintainance {car.needs_maintenance}
    no. trips since maintance {car.trips_since_maintenance}
    """)




