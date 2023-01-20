"""
Для представления рациональных чисел разработайте и реализуйте отдельную АСД RatNum.
RatNum представляет собой неизменяемое (immutable) рациональное число. 
RatNum может использоваться для представления любого элемента множества рациональных чисел,
а также специального элемента “NaN” (не-число), получающегося в результате деления на ноль.

Элемент “NaN” является во многом особенным. 
При выполнении любых арифметических операций с “NaN”, результат будет “NaN”. 
Что касается операций сравнения, таких как “меньше чем”, 
“NaN” считается равным самому себе и большим, чем любые другие рациональные числа.

Примеры объектов RatNum включают “-1/13”, “53/7”, “4”, “NaN” и “0”.
Необходимо обеспечить выполнение следующих операций:
– is_nan()
– is_negative()
– is_positive()
– compare_to()
– float_value()
– int_value()
– negate()
– add()
– sub()
– mul()
– div()
– gcd()
– __str__()
– __hash__()
– __eq__()
"""


class RatNum:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        if type(numerator) != int or type(denominator) != int:
            raise ValueError("Wrong type of numerator/denominator! Must be 'int' type") 

    @property
    def _value(self):
        return "NaN" if self.is_nan() else self.numerator / self.denominator

    def is_nan(self):
        if self.denominator == 0:
            return True
        return False

    def is_negative(self):
        if self.numerator < 0 and self.denominator > 0:
            return True
        elif self.numerator > 0 and self.denominator < 0:
            return True
        return False

    def is_positive(self):
        if self.numerator > 0 and self.denominator > 0:
            return True
        elif self.numerator < 0 and self.denominator < 0:
            return True
        return False
    
    def compare_to(self, other):
        s = self._value
        o = other._value
        if s == "NaN" and o != "NaN":
            return f"{self} > {other}"
        elif s != "NaN" and o == "NaN":
            return f"{self} < {other}"
        elif s == "NaN" and o == "NaN":
            return f"{self} = {other}"
        else:
            if s > o:
                return f"{self} > {other}"
            elif s < o:
                return f"{self} < {other}"
            elif s == o:
                return f"{self} = {other}"

    def float_value(self):
        if self.is_nan():
            return "NaN"
        return float(self.numerator / self.denominator)
    
    def int_value(self):
        if self.is_nan():
            return "NaN"
        return int(self.numerator / self.denominator)
    
    def negate(self):
        if self.is_positive():
            return RatNum(-self.numerator, self.denominator)
        return RatNum(self.numerator, self.denominator)
    
    def add(self, other):
        if self.is_nan() or other.is_nan():
            return "NaN"
        else:
            denominator = self.denominator * other.denominator
            numerator1 = self.numerator * (denominator / self.denominator)
            numerator2 = other.numerator * (denominator / other.denominator)
            return (numerator1 + numerator2) / denominator
    
    def sub(self, other):
        if self.is_nan() or other.is_nan():
            return "NaN"
        else:
            denominator = self.denominator * other.denominator
            numerator1 = self.numerator * (denominator / self.denominator)
            numerator2 = other.numerator * (denominator / other.denominator)
            return (numerator1 - numerator2) / denominator
    
    def mul(self, other):
        if self.is_nan() or other.is_nan():
            return "NaN"
        else:
            denominator = self.denominator * other.denominator
            numerator = self.numerator * other.numerator
            return numerator / denominator
    
    def div(self, other):
        if self.is_nan() or other.is_nan():
            return "NaN"
        else:
            denominator = self.denominator * other.numerator
            numerator = self.numerator * other.denominator
            if denominator == 0:
                return "NaN"
            return numerator / denominator
    
    def gcd(self, other):
        if self.is_nan() or other.is_nan():
            return "NaN"
        a, b = self._value, other._value
        if a == 0 or b == 0:
            return "NaN"
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        if self.is_nan():
            return "NaN"
        elif self._value == 0:
            return "0"
        else:
            n = RatNum(self.numerator)
            d = RatNum(self.denominator)
            gcd = n.gcd(d)
            if self.denominator == 1:
                return f"{self.numerator}"
            else:
                return f"{int(self.numerator/gcd)}/{int(self.denominator/gcd)}"    

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator


if __name__ == "__main__":
    a = RatNum(-1, 13)
    b = RatNum(53, 7)
    c = RatNum(4)
    d = RatNum(4, 0)
    e = RatNum(0)
    
    print("\nTests 'compare_to()'")
    print(a.compare_to(b))
    print(b.compare_to(c))
    print(c.compare_to(d))
    print(d.compare_to(e))
    print(e.compare_to(a))

    print("\nTests 'add()'")
    print(a.add(b))
    print(b.add(c))
    print(c.add(d))
    print(d.add(e))
    print(e.add(a))

    print("\nTests 'sub()'")
    print(a.sub(b))
    print(b.sub(c))
    print(c.sub(d))
    print(d.sub(e))
    print(e.sub(a))

    print("\nTests 'mul()'")
    print(a.mul(b))
    print(b.mul(c))
    print(c.mul(d))
    print(d.mul(e))
    print(e.mul(a))

    print("\nTests 'div()'")
    print(a.div(b))
    print(b.div(c))
    print(c.div(d))
    print(d.div(e))
    print(e.div(a))

    print("\nTests 'gcd()'")
    print(a.gcd(b))
    print(b.gcd(c))
    print(c.gcd(d))
    print(d.gcd(e))
    print(e.gcd(a))

    print("\nTests '__eq__'")
    print(a == b)
    print(b == c)
    print(c == d)
    print(d == e)
    print(e == a)
    print(a == a)
    print(d == d)
