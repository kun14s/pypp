PI = double(3.14159265358979324)
pi = PI
E = double(2.71828182845904524)
e = E

def strnan(self):
    return "NaN"

def ltnan(self, other):
    if isinstance(other, number):
        return false
    return NotImplemented

def lenan(self, other):
    if isinstance(other, number):
        return false
    return NotImplemented

def eqnan(self, other):
    if isinstance(other, number):
        return false
    return NotImplemented

def gtnan(self, other):
    if isinstance(other, number):
        return false
    return NotImplemented

def genan(self, other):
    if isinstance(other, number):
        return false
    return NotImplemented
    
def nenan(self, other):
    if isinstance(other, number):
        return true
    return NotImplemented

nan = number()
nan.__str__ = strnan
nan.__lt__ = ltnan
nan.__le__ = lenan
nan.__eq__ = eqnan
nan.__gt__ = gtnan
nan.__ge__ = genan
nan.__ne__ = nenan
NaN = nan

inf = number()

def strinf(self):
    return "Inf"

def ltinf(self, other):
    if isinstance(other, number):
        return false
    return NotImplemented

def leinf(self, other):
    if isinstance(other, number):
        if other is inf:
            return true
        else:
            return false
    return NotImplemented

def eqinf(self, other):
    if isinstance(other, number):
        if other is inf:
            return true
        else:
            return false
    return NotImplemented

def gtinf(self, other):
    if isinstance(other, number):
        return true
    return NotImplemented

def geinf(self, other):
    if isinstance(other, number):
        if other is inf:
            return true
        else:
            return false
    return NotImplemented

def neinf(self, other):
    if isinstance(other, number):
        if other is inf:
            return false
        else:
            return true
    return NotImplemented

inf.__str__ = strinf
inf.__lt__ = ltinf
inf.__le__ = leinf
inf.__eq__ = eqinf
inf.__gt__ = gtinf
inf.__ge__ = geinf
inf.__ne__ = neinf

Inf = inf

def gcd(a, b):
    if (not isinstance(a, integer)) and (not isinstance(a, int)):
        raise ValueError("invalid value : a")
    elif (not isinstance(b, integer)) and (not isinstance(b, int)):
        raise ValueError("invalid value : b")
    while b != 0:
        a, b = b, a%b
    return a
    
def lcm(a, b):
    '''returns lcm of a, b'''
    if (not isinstance(b, integer)) and (not isinstance(b, int)):
        raise ValueError("invalid value : a")
    elif (not isinstance(b, integer)) and (not isinstance(b, int)):
        raise ValueError("invalid value : b")
    if a == 0 or b == 0:
        return 0
    return integer(abs(a * b) // gcd(a, b))

def rad(deg):
    '''returns degree(deg) -> radian'''
    if (not isinstance(deg, double)) and (not isinstance(deg, float)):
        raise ValueError("ERROR : radian's arg must be a double")
    q = PI / 180
    return double(deg * q)

def deg(rad):
    '''returns radian(rad) -> degree'''
    if (not isinstance(deg, double)) and (not isinstance(deg, float)):
        raise ValueError("ERROR : degree's arg must be a double")
    q = 180 / PI
    return double(rad * q)

def fact(n):
    '''returns the factorial of x'''
    if (not isinstance(n, integer)) and (not isinstance(n, int)):
        raise ValueError("ERROR : factorial's arg must be an integer")
    elif n == 0:
        return integer(1)
    a = 2
    r = 1
    if isinstance(n, integer):
        while a<=n.v:
            r *= a
            a += 1
        return integer(r)
    else:
        while a<=n:
            r *= a
            a += 1
        return integer(r)

def root(y, x):
    '''returns the y-th root of x'''
    if (y % 2 == 0) and (x < 0):
        raise ValueError("Cannot take an even root when the radicand is negative")
    elif x == 0:
        return double(0)
    elif x == 1:
        return double(1)
    return double(pow(x, 1/y))

def comb(n, m):
    return integer(fact(n)/(fact(m)*fact(n-m)))