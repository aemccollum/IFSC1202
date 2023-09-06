import math
a = float(input("Enter a Value: "))
b = float(input("Enter a Value: "))
c = float(input("Enter a Value: "))
s=(a+b+c)/2
area=float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print(area)
