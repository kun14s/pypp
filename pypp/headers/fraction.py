class Fraction:

    def reduction(self):
        
        def gcd(a, b):
            if (not isinstance(a, integer)) and (not isinstance(a, int)):
                raise ValueError("invalid value : a")
            elif (not isinstance(b, integer)) and (not isinstance(b, int)):
                raise ValueError("invalid value : b")
            while b != 0:
                a, b = b, a%b
            return a
            
        g = gcd(self.n, self.d)
        self.n, self.d = self.n // g, self.d // g
    
    def __init__(self, numerator, denominator):
        
        self.n = numerator
        self.d = denominator
        
        if not isinstance(self.n, integer) and (not isinstance(self.n, int)):
            raise ValueError("invalid value : numerator")
            
        elif not isinstance(self.d, integer) and (not isinstance(self.d, int)):
            raise ValueError("invalid value : denominator")
            
        elif (self.d == 0) or (self.d == integer(0)):
            raise ValueError("invalid value : denominator")
            
        elif self.d < 0:
            self.d, self.n = -self.d, -self.n
        
        self.reduction()
        self.double_val = self.n / self.d
    
    def __str__(self):
        if (self.d == 1) or (self.d == integer(1)):
            return str(self.n)
        return str(self.n) + "/" + str(self.d)

    def str_value(self):
        return str(self.val)

    def reciprocal(self):
        return Fraction(self.d, self.n)
        
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        
        def gcd(a, b):
            if (not isinstance(a, integer)) and (not isinstance(a, int)):
                raise ValueError("invalid value : a")
            elif (not isinstance(b, integer)) and (not isinstance(b, int)):
                raise ValueError("invalid value : b")
            while b != 0:
                a, b = b, a%b
            return a
        
        l = (self.d * other.d) // gcd(self.d, other.d)
        n1 = self.n * (l // self.d)
        n2 = other.n * (l // other.d)
        return Fraction(n1 + n2, self.d)

    def __radd__(self, other):
        return self.__add__(other)
        
    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("invalid value : other")
        
        def gcd(a, b):
            if (not isinstance(a, integer)) and (not isinstance(a, int)):
                return NotImplemented
            elif (not isinstance(b, integer)) and (not isinstance(b, int)):
                return NotImplemented
            while b != 0:
                a, b = b, a%b
            return a
            
        l = (self.d * other.d) // gcd(self.d, other.d)
        n1 = self.n * (l // self.d)
        n2 = other.n * (l // other.d)
        return Fraction(n1 - n2, self.d)

    def __rsub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return other.__sub__(self)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.n*other.n, self.d*other.d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self * other.reciprocal()
    
    def __rtruediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return other.__truediv__(self)
