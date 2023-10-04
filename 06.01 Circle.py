from math import pi
radius = float(input("Enter the Radius: "))
def diameter(d):
    d = radius * 2
def circumference(C):
    C = 2*pi*radius
def area(a):
    a = pi* radius**2
inputfilename = "06.01 Radius.txt"
def main():
    inputfile = open(inputfilename, "r")
    lst = []
while True:
    line = inputfile.readline()
    if not line:
        break
    else:
        lst.append(float(line))

