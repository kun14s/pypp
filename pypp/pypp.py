'''
===Py++语言===
'''

import sys

def include(s):
    if type(s) != str:
        raise ValueError("ERROR : invalid include")
    else:
        try:
            with open(rf"headers\{s}.py", "r", encoding = "utf-8") as f:
                exec(f.read(), globals())
        except FileNotFoundError:
            try:
                exec(f"import {s}", globals())
            except ModuleNotFoundError:
                raise ValueError("ERROR : invalid name")

true = True
false = False

class number:
    pass

class double(number):
    
    def __init__(self, val):
        if not isinstance(val, float):
            if not isinstance(val, int):
                raise ValueError("ERROR : value must be a double")
        self.v = val
        
    def __str__(self):
        return str(self.v)

    def __add__(self, other):
        if isinstance(other, int):
            return double(self.v + other)
        elif isinstance(other, float):
            return double(self.v + other)
        elif isinstance(other, number):
            return double(self.v + other.v)
        else:
            return NotImplemented
        
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            return double(self.v - other)
        elif isinstance(other, float):
            return double(self.v - other)
        elif isinstance(other, number):
            return double(self.v - other.v)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, integer):
            return double(other.v - self.v)
        elif isinstance(other, int):
            return double(other - self.v)
        elif isinstance(other, float):
            return double(other - self.v)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return double(self.v * other)
        elif isinstance(other, float):
            return double(self.v * other)
        elif isinstance(other, number):
            return double(self.v * other.v)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)
        
    def __truediv__(self, other):
        if isinstance(other, int):
            return double(self.v / other)
        elif isinstance(other, float):
            return double(self.v / other)
        elif isinstance(other, number):
            return double(self.v / other.v)
        else:
            return NotImplemented
    
    def __rtruediv__(self, other):
        if isinstance(other, integer):
            return double(other.v / self.v)
        elif isinstance(other, int):
            return double(other / self.v)
        elif isinstance(other, float):
            return double(other / self.v)
        else:
            return NotImplemented
            
    def __neg__(self):
        return double(-self.v)

    def __lt__(self, other):
        if isinstance(other, int):
            if self.v < other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v < other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v < other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, int):
            if self.v <= other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v <= other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v <= other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, int):
            if self.v == other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v == other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v == other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, int):
            if self.v > other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v > other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v > other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, int):
            if self.v >= other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v >= other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v >= other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, int):
            if self.v != other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v != other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v != other.v:
                return true
            else:
                return false
        else:
            return NotImplemented

class integer(number):
    
    def __init__(self, val):
        if not isinstance(val, int):
            raise ValueError("ERROR : value must be an integer")
        self.v = val
        
    def __str__(self):
        return str(self.v)
    
    def __add__(self, other):
        if isinstance(other, integer):
            return integer(self.v + other.v)
        elif isinstance(other, double):
            return double(self.v + other.v)
        elif isinstance(other, int):
            return integer(self.v + other)
        elif isinstance(other, float):
            return double(self.v + other)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, integer):
            return integer(self.v - other.v)
        elif isinstance(other, double):
            return double(self.v - other.v)
        elif isinstance(other, int):
            return integer(self.v - other)
        elif isinstance(other, float):
            return double(self.v - other)
        else:
            return NotImplemented
    
    def __rsub__(self, other):
        if isinstance(other, integer):
            return integer(other.v - self.v)
        elif isinstance(other, int):
            return integer(other - self.v)
        elif isinstance(other, float):
            return double(other - self.v)
        else:
            return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, integer):
            return integer(self.v * other.v)
        elif isinstance(other, double):
            return double(self.v * other.v)
        elif isinstance(other, int):
            return integer(self.v * other)
        elif isinstance(other, float):
            return double(self.v * other)
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, integer):
            return double(self.v / other.v)
        elif isinstance(other, double):
            return double(self.v / other.v)
        elif isinstance(other, int):
            return double(self.v / other)
        elif isinstance(other, float):
            return double(self.v / other)
        else:
            return NotImplemented
    
    def __rtruediv__(self, other):
        if isinstance(other, integer):
            return double(other.v / self.v)
        elif isinstance(other, double):
            return double(other.v / self.v)
        elif isinstance(other, int):
            return double(other / self.v)
        elif isinstance(other, float):
            return double(other / self.v)
        else:
            return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, integer):
            return integer(self.v // other.v)
        elif isinstance(other, int):
            return integer(self.v // other)
        else:
            return NotImplemented

    def __rfloordiv__(self, other):
        if isinstance(other, integer):
            return integer(other.v // self.v)
        elif isinstance(other, int):
            return integer(other // self.v)
        else:
            return NotImplemented
    
    def __mod__(self, other):
        if isinstance(other, integer):
            return integer(self.v % other.v)
        elif isinstance(other, int):
            return integer(self.v % other)
        else:
            return NotImplemented
    
    def __rmod__(self, other):
        if isinstance(other, integer):
            return integer(other.v % self.v)
        elif isinstance(other, int):
            return integer(other % self.v)
        else:
            return NotImplemented
            
    def __neg__(self):
        return integer(-self.v)

    def __lt__(self, other):
        if isinstance(other, int):
            if self.v < other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v < other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v < other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, int):
            if self.v <= other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v <= other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v <= other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, int):
            if self.v == other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v == other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v == other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, int):
            if self.v > other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v > other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v > other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, int):
            if self.v >= other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v >= other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v >= other.v:
                return true
            else:
                return false
        else:
            return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, int):
            if self.v != other:
                return true
            else:
                return false
        elif isinstance(other, float):
            if self.v != other:
                return true
            else:
                return false
        elif isinstance(other, number):
            if self.v != other.v:
                return true
            else:
                return false
        else:
            return NotImplemented

class string:
    
    def __init__(self, val):
        if not isinstance(val, str):
            raise ValueError("ERROR : value must be a string")
        self.v = val
        
    def __str__(self):
        return self.v
        
    def __eq__(self, other):
        if self.v == other.v:
            return true
        else:
            return false
    
def cout(*s):
    n = 0
    while n < len(s):
        if type(s[n]) != str:
            print(s[n], end = "")
            n += 1
            continue
        print(s[n], end = "")
        n += 1
    print()
    return 0

def cin(p, typ):
    val = input(p)
    if typ == "int":
        return integer(int(val))
    elif typ == "str":
        return string(val)
    elif typ == "db":
        return double(float(val))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if (sys.argv[1] == "-h") or (sys.argv[1] == "-help"):
            print("""
- 解释方法：
    `py++ your_file_name.py`
- -h或-help帮助
""")
        else:
            file_name = sys.argv[1]
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    code = f.read()
                exec(code, globals())
                if "main" in globals():
                    r = main()
                else:
                    print(f"ERROR : main() function isn't found in {file_name}")
            except FileNotFoundError:
                print(f"ERROR : file {file_name} not found")
            except Exception as e:
                print(f"EXCEPTION : {type(e).__name__} : {e}")
    else:
        print("""
解释方法：`py++ your_file_name.py`
-h或-help帮助
"""
)
