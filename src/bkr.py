import random as r
import numpy as np
from numpy.polynomial import polynomial as P


class bkr_utility:

    def __init__(self):
        pass

    def generateTestPolySet(self):
        # generates a random set of squarefre polynomials
        polynomials = []
        # based on the following parameters:

        n = 10 # the number of polynomials
        d = 10 # the maximal degree
        coeffRange = (-20, 20) # the range of possible integer coefficients

        print(f"generating polynomial set")

        availableRoots = n.random.randint(1, d+1, n*d)

        for i in range(n): # for every polynomial

            # generate d roots
            roots = []
            
            while (len(roots) < numberOfRoots):
                new_root = r.randint(coeffRange[0], coeffRange[1]+1)
                if (new_root == 0): # zero roots allowed
                    pass
                if (new_root in roots): # no repeated roots
                    continue
                roots.append(new_root)

            new_polynomial = P.polyfromroots(roots) # generate monic polynomial
            polynomials.append(new_polynomial)
        
        return polynomials
            
    def bkrIsConsistent(self, input_set):
        pass



    def printPolySet(self, toPrint):
        print("printing polynomial set:")
        for i, p in enumerate(toPrint):
            print(f"p{i}\t: {p}")


    def temporaryTest(self):
        testPolyset = self.generateTestPolySet()
        self.printPolySet(testPolyset)
        
        if (testPolyset.bkrIsConsistent(testPolyset)):
            print(f"Set is consistent")
        else:
            print(f"Set isn't consistent")