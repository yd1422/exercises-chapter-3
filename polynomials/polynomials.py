from numbers import Number
from typing import Any


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:])
        elif isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients[: common],other.coefficients[:common]))
            if len(self.coefficients) > len(other.coefficients):
                coefs += self.coefficients[common:]
            elif len(self.coefficients) < len(other.coefficients):
                coefs += tuple(-r for r in (other.coefficients[common:]))
            return Polynomial(coefs)
        else:
            return NotImplemented 
    def __rsub__(self, other):
        Poly = self - other
        Poly.coefficients = tuple(-r for r in Poly.coefficients)
        return Poly
    
    def __mul__(self, other):
        Poly = 0
        if isinstance(other, Number):
            return Polynomial(tuple(other*i for i in self.coefficients))
        elif isinstance(self,Polynomial):
            for i in range(0,len(other.coefficients)):
                tuple1 = (0,)*i
                Poly += Polynomial(tuple1 + tuple(other.coefficients[i]* r for r in self.coefficients))
            return Poly
    def __rmul__(self, other):
        return self * other 

    def __pow__(self, Number):
        self2 = self
        for i in range(0,Number-1):
            self1 = self2
            self2 = self * self1
        return self2 

    def __call__(self, x):
        val = 0
        for i in range(0, len(self.coefficients)):
            val = val + x**(i) * self.coefficients[i] 
        return val
                    