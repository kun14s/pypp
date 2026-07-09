include("fraction")

def B(n):
    '''returns the n-th bernoulli number'''
    def comb(a, b):
        return integer(fact(a)/(fact(b)*fact(a-b)))
    if n == 0:
        return double(1)
    elif n == 1:
        return double(-0.5)
    elif n % 2 == 1:
        return double(0)
    res = double(-1) / (n+1)
    b_values = [Fraction(1, 1)]
    k = integer(0)
    while k <= n:
        b_values.append(Fraction(comb(n+1, k) * b_values[k], 1))
        k = k + 1
    r = sum(b_values)
    res = res + r.double_val
    return res

bernoulli = B
bernoulli_number = B