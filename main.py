## electric charge is q = ne where n is an integer.
""" and e = -1.6 * 10**-19 c """
## matter with alike charges repell each other and matter with different charges attract eachother.
## so how can we predict how strong the foces between them are going to be?
## coulumb law is:
""" f = k*q1*q2 / r**2 """
""" ke = 8.98 * 10**9 """

#### FIRST: WE NEED A CALCULATOR FOR COILOMBS LAW ####
import numpy as np
class CoulombLaw:
    def __init__(self,
                 q1,
                 q2,
                 r,
                 k = 9e9,
                 ):
        self.q1 = q1
        self.q2 = q2
        self.r = r
        self.k = k
        
    def calculate_coulomb_law(self):
        print(abs(self.q1 * self.q2) * self.k / self.r**2)
    

particle = CoulombLaw(+5e-3, -1e-1, 0.5)
particle.calculate_coulomb_law()