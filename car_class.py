# import my vehicle class
from vehicle_class import *

# define car class here and make it inherit from vehicle
class car(vehicle):
    def __init__(self, brand, hp, ms):
        self.brand = brand
        self.horse_power = hp
        self.max_speed = ms

    def park(self):
        return 'Beep Beep Beep'

    def honk(self):
        return 'hoonnnnnnnnn'

#Characterists:
# brand
# horse_power
# max_speed

#methods :
# park
# honk