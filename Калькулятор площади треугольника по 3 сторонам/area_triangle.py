a = float(input('Side A: '))
b = float(input('Side B: '))
c = float(input('Side C: '))

half_p = (a + b + c) / 2

area = (half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5

print(area)