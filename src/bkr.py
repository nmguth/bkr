import random as r
from urllib.parse import _NetlocResultMixinBytes
import numpy as np
from numpy.polynomial import polynomial as P
from sympy import sturm
from sympy.abc import x
import itertools


class bkr_utility:

    def __init__(self):
        pass

    def generateTestPolySet(self):
        # generates a random set of squarefre polynomials
        polynomials = []
        # based on the following parameters:

        n = 2 # the number of polynomials
        d = 3 # the maximal degree
        coeffRange = (-20, 20) # the range of possible integer coefficients

        for i in range(n): # for every polynomial
            coeffs = np.random.randint(coeffRange[0], coeffRange[1], r.randint(3, d))
            #new_polynomial = P.Polynomial(coeffs) # generate monic polynomial
            polynomials.append(coeffs)
        

        return polynomials
    
    def numberSignChanges(self, p):
        numSignChanges = len(list(itertools.groupby(p, lambda Input: Input >= 0)))-1
        return numSignChanges

    # evaluates the leading term of a polynomials at value a
    def evaluateLeadingTerm(self, poly, a):
        return poly[-1]*(a**(len(poly)-1))

    def sturmSeq(self, p1, p2):
        output = []
        output.append(p1)
        output.append(p2)
        done = False
        #for i in range(len(p1)-1):
        while (not done):
            output.append( P.polymul(-1, P.polydiv(output[-2], output[-1])[1] ))
            if (len(output[-1])==1):
                done = True
        return output

    def sturm(self, p1, p2):
        sequence = self.sturmSeq(p1, p2)

        valuesAtOne = [P.Polynomial(p_i)(1) for p_i in sequence]
        valuesAtMinusOne = [P.Polynomial(p_i)(-1) for p_i in sequence]

        evalA = self.numberSignChanges(valuesAtOne)
        evalB = self.numberSignChanges(valuesAtMinusOne)

        return (evalB - evalA)

    def recursiveDAC(self, p, pset):
        psetLength = len(pset)
        if (psetLength==1):

            A = np.asarray([[1, 1], [1, -1]])
            S = np.asarray([self.sturm(p, P.polyder(p)), self.sturm(p, P.polymul(P.polyder(p), pset[0]))])
            C = np.linalg.solve(A, S)

            return (A,S,C)
        else:
            # divide system in half
            setA = pset[:psetLength//2]
            setB = pset[psetLength//2:]
            a1, c1, s1 = self.recursiveDAC(p, setA)
            a2, c2, s2 = self.recursiveDAC(p, setB)

            # combine into new larger system

            outputA = np.kron(a1, a2)
            outputC = np.hstack((c1, c2))
            outputS = np.hstack((s1, s2))
            # reduce system

            # return system
            return outputA,outputC,outputS # ret A, C, S
            
    def bkrIsConsistent(self, input_set):
        
        polyProduct = input_set[0] # product of all polys in input_set
        for poly_i in input_set[1:]:
            polyProduct = P.polymul(polyProduct, poly_i)

        R = 1 + (np.array([a_i / polyProduct[-1] for a_i in polyProduct])).max()

        productDer = P.polyder(polyProduct)

        # test system at roots of p
        p = P.polymul( P.polymul([-R, 1],[R, 1]) , productDer )

        A, C, S = self.recursiveDAC(p, input_set)
    
        print(f"C:\n{C}")
        print(f"S:\n{S}")

        return not any(C)

    def printPolySet(self, toPrint):
        for i, p in enumerate(toPrint):
            print(f"p{i}\t: {p}")
