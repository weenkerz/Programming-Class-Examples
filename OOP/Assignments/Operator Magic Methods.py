class RationalNumber:

    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = (other.d * self.n) + (self.d * other.n)
        d = other.d * self.d

        return RationalNumber(n, d)

    def __sub__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = (other.d * self.n) - (self.d * other.n)
        d = other.d * self.d

        return RationalNumber(n, d)

    def __mul__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.n
        d = self.d * other.d

        return RationalNumber(n, d)

    def __truediv__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d
        d = self.d * other.n

        return RationalNumber(n, d)

    def __str__(self):
        n = self.n
        d = self.d

        if n % d == 0:
            n = round(n/d)
            return f'{n}'

        else:
            divisors_n = [i for i in range(1, round(self.n**0.5)+2) if self.n % i == 0]
            divisors_d = [i for i in range(1, round(self.d**0.5)+2) if self.d % i == 0]

            gcf = max([i for i in divisors_d if i in divisors_n])

            return "%s/%s" % (round(n/gcf), round(d/gcf))


a = RationalNumber(7,2)
b = RationalNumber(1, 90)

print(f"Addition       | {a + b}")
print(f"Subtraction    | {a - b}")
print(f"Multiplication | {a * b}")
print(f"Division       | {a / b}")
