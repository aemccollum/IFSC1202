from math import pi
from math import sqrt
from math import acos
class Triangle:
    def __init__(self, s1, s2, s3):
        self.A = s1
        self.B = s2
        self.C = s3
    def type(self):
        if s1 == s2 == s3:
            return "Equilateral"
        if s1 == s2:
            return "Isoceles"
        if s1 == s3: 
            return "Isoceles"
        if s2 == s3:
            return "Isoceles"
        return "Scalene"
    def perimeter(self):
        perimeter == A + B + C
        return (perimeter)
    def area(self):
        s=(A+B+C)/2
        area=float(math.sqrt(s*(s-A)*(s-B)*(s-C)))
        return(area)
    def angles(self):
        for i in range(len(self.A)):
            if self.A[i].strip() != "":
                acos(B**2+C**2-A**2/(2*B*C))*(180/pi)
                return (Angle1)
        for i in range(len(self.B)):
            if self.B[i].strip() != "":
                acos(C**2+A**2-B**2/(2*C*A))*(180/pi)
                return (Angle2)
        for i in range(len(self.C)):
            if self.C[i].strip() != "":
                acos(A**2+B**2-C**2/(2*a*b))*(180/pi)
                return (Angle3)
    def Triangle(self):
        Triangle.append(TriangleList)
TriangleList = []
trianglefile = open("Exam Three Triangles.txt")
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("Type", "Side 1", "Side 2", "Side 3", "Perimeter","Area","Angle 1","Angle 2", "Angle 3"))
x = trianglefile.readline()
while x!="":
    y = x.split(",")
    print("{:>12s} {:>12s} {:>12s} {:>12.2f} {:>12.2f} {:>12.2f}".format(type, TriangleList1.A(), TriangleList1.B(), TriangleList1.C(), TriangleList1.perimeter(), TriangleList1.area(), TriangleList1.Angle1(), TriangleList1.Angle2(), TriangleList1.Angle3()))
    x = trianglefile.readline()
    trianglefile.close()

