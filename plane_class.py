# import all the classes
from vehicle_class import *
from car_class import *

# create 2 vehicle instances
vehicle_one = vehicle(10,200)
vehicle_two = vehicle(4,50)

# call methods and attributes to test
vehicle_one.accelerate()
vehicle_two.n_passengers

# create 2 car instances
suzu = car('suzuki',98,110)
vaux = car('Vauxhall', 140, 100)

# make car accelerate and make them break
print(suzu.accelerate())
print(suzu.brake())

# make car honk and park
print(vaux.honk())
print(vaux.park())

# define plane class with vehicle parent
class plane(vehicle):
    def take_off(self):
        return 'Take off in 3\n2\n1\nHouston we have lift off'

    def touch_down(self):
        return '**clap**'

# create 2 plane instances here
boeing = plane(200,1000)
airbus = plane(200,1000)

# make plane accelerate and make them break
boeing.accelerate()
boeing.brake()

# make plane fly and land
airbus.take_off()
airbus.touch_down()