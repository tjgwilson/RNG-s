import numpy as np
import random
import math

class rand:
    gaussian_random = 0.0
    check = False
    def box_muller(self):
        if(rand.check == False):
            u1 = random.random()
            u2 = random.random()
            rand.gaussian_random = math.sqrt(-2.0*math.log(u1))*math.sin(2.0*math.pi*u2)
            rand.check = not rand.check
            return (math.sqrt(-2.0*math.log(u1))*math.cos(2.0*math.pi*u2))
        elif(rand.check == True):
            rand.check = not rand.check
            return rand.gaussian_random



a=rand()
print(a.box_muller())
