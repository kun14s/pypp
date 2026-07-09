include("bernoulli")
include("maths")

def sin(n, x=1000):
    '''returns sine of n, loop count is x(Rad)'''
    if (not isinstance(n, double)) and (not isinstance(n, float)):
        raise ValueError("ERROR : sin's arg the n must be a double")
    elif (n == 0) or (n == double(0)):
        return double(0)
    elif (n == rad(30)) or (n == double(rad(30))):
        return double(0.5)
    elif (n == rad(45)) or (n == double(rad(45))):
        return root(2, 2) / 2
    elif (n == rad(60)) or (n == double(rad(60))):
        return root(3, 2) / 2
    elif (n == rad(90)) or (n == double(rad(90))):
        return double(1)
    elif (n == rad(120)) or (n == double(rad(120))):
        return root(3, 2) / 2
    elif (n == rad(135)) or (n == double(rad(135))):
        return root(2, 2) / 2
    elif (n == rad(150)) or (n == double(rad(150))):
        return double(0.5)
    elif (n == rad(180)) or (n == double(rad(180))):
        return double(0)
    elif (n == rad(210)) or (n == double(rad(210))):
        return double(-0.5)
    elif (n == rad(225)) or (n == double(rad(225))):
        return -(root(2, 2) / 2)
    elif (n == rad(240)) or (n == double(rad(240))):
        return -(root(3, 2) / 2)
    elif (n == rad(270)) or (n == double(rad(270))):
        return double(-1)
    elif (n == rad(300)) or (n == double(rad(300))):
        return -(root(3, 2) / 2)
    elif (n == rad(315)) or (n == double(rad(315))):
        return -(root(2, 2) / 2)
    elif (n == rad(330)) or (n == double(rad(330))):
        return double(-0.5)
    elif (n == rad(360)) or (n == double(rad(360))):
        return double(0)
    
    y = 3
    is_plus = False
    t = 1
    while t <= x:
        if is_plus:
            res = res + pow(res, y)/fact(y)
            y = y + 2
            t = t + 1
            is_plus = not is_plus
        else:
            res = res - pow(res, y)/fact(y)
            y = y + 2
            t = t + 1
            is_plus = not is_plus
    return res
    
def cos(n, x=1000):
    '''returns cosine of n, loop count is x(Rad)'''
    if (not isinstance(n, double)) and (not isinstance(n, float)):
        raise ValueError("ERROR : cos's arg the n must be a double")
    elif (n == rad(0)) or (n == double(rad(0))):
        return double(1)
    elif (n == rad(30)) or (n == double(rad(30))):
        return root(3, 2) / 2
    elif (n == rad(45)) or (n == double(rad(45))):
        return root(2, 2) / 2
    elif (n == rad(60)) or (n == double(rad(60))):
        return double(0.5)
    elif (n == rad(90)) or (n == double(rad(90))):
        return double(0)
    elif (n == rad(120)) or (n == double(rad(120))):
        return double(-0.5)
    elif (n == rad(135)) or (n == double(rad(135))):
        return -(root(2, 2) / 2)
    elif (n == rad(150)) or (n == double(rad(150))):
        return -(root(3, 2) / 2)
    elif (n == rad(180)) or (n == double(rad(180))):
        return double(-1)
    elif (n == rad(210)) or (n == double(rad(210))):
        return -(root(3, 2) / 2)
    elif (n == rad(225)) or (n == double(rad(225))):
        return -(root(2, 2) / 2)
    elif (n == rad(240)) or (n == double(rad(240))):
        return double(-0.5)
    elif (n == rad(270)) or (n == double(rad(270))):
        return double(0)
    elif (n == rad(300)) or (n == double(rad(300))):
        return double(-0.5)
    elif (n == rad(315)) or (n == double(rad(315))):
        return -(root(2, 2) / 2)
    elif (n == rad(330)) or (n == double(rad(330))):
        return -(root(3, 2) / 2)
    elif (n == rad(360)) or (n == double(rad(360))):
        return double(1)
    
    y = 2
    is_plus = False
    res = 1
    t = 1
    r = rad(n)
    while t <= x:
        if is_plus:
            res = res - pow(r, y)/fact(y)
            y = y + 2
            t = t + 1
            is_plus = not is_plus
        else:
            res = res + pow(r, y)/fact(y)
            y = y + 2
            t = t + 1
            is_plus = not is_plus
    return double(res)
    

def tan(n, x=1000):
    '''returns tangent of n, loop count is x(Rad)'''
    if (not isinstance(n, double)) and (not isinstance(n, float)):
        raise ValueError("ERROR : tan's arg the n must be a double")
    elif (n == rad(0)) or (n == double(rad(0))):
        return double(0)
    elif (n == rad(30)) or (n == double(rad(30))):
        return root(3, 2) / 3
    elif (n == rad(45)) or (n == double(rad(45))):
        return double(1)
    elif (n == rad(60)) or (n == double(rad(60))):
        return root(3, 2)
    elif (n == rad(90)) or (n == double(rad(90))):
        return Inf
    elif (n == rad(120)) or (n == double(rad(120))):
        return -(root(3, 2))
    elif (n == rad(135)) or (n == double(rad(135))):
        return double(-1)
    elif (n == rad(150)) or (n == double(rad(150))):
        return -(root(3, 2) / 3)
    elif (n == rad(180)) or (n == double(rad(180))):
        return double(0)
    elif (n == rad(210)) or (n == double(rad(210))):
        return -(root(3, 2) / 3)
    elif (n == rad(225)) or (n == double(rad(225))):
        return double(1)
    elif (n == rad(240)) or (n == double(rad(240))):
        return root(3, 2)
    elif (n == rad(270)) or (n == double(rad(270))):
        return Inf
    elif (n == rad(300)) or (n == double(rad(300))):
        return -(root(3, 2))
    elif (n == rad(315)) or (n == double(rad(315))):
        return double(-1)
    elif (n == rad(330)) or (n == double(rad(330))):
        return -(root(3, 2) / 3)
    elif (n == rad(360)) or (n == double(rad(360))):
        return double(0)

    k = 1
    o = 2
    res = rad(n)
    while k <= x:
        res = res + pow(o, 2) * pow(o, 2)-1 * abs(B(o)) / fact(o) * pow(n, 3)
        o = o + 2
        k = k + 1
    return double(res)
