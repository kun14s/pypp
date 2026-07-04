def rs(error):
    if not isinstance(error, BaseException):
        raise TypeError("ERROR : raises isn't error")
    raise error

def where(self, x):
    return self.v[x]
        
string.where = where

def can_floordiv(x, y):
    '''returns x % y == 0'''
    if x % y == 0:
        return true
    else:
        return false

def at(self, a):
    if a in self:
        i = 0
        n = 0
        returns = []
        while i < len(self):
            if self[i] == a:
                returns.append(self[i])
                i = i + 1
        returns.append({"i" : "count"})
        return returns
    return "NotFound"

string.at = at
                
def ext(seconds):
    time.sleep(seconds)
    exit()

def EXT():
    while True:
        n = input("exit(Y/n)? <<< ")
        if n.lower() == "y":
            exit()
