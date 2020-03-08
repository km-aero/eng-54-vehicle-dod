# define vehicle class here
class vehicle():
    def __init__(self, n_p, s_c):
        self.n_passengers = n_p
        self.size_cargo = s_c

    def accelerate(self):
        return 'VROOOOM'

    def brake(self):
        return 'SKRRRRRR'

#Characteristics:
# n_passengers
# size_cargo

#methods:
# accelerate
# break