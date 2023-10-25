a = []
inputfile = open("09.Project Distances.csv")
x = inputfile.readline()
while x != "":
	y = x.split(" ")
	for i in range(len(y)):
		y[i] = (y[i])
	a.append(y)
	x = inputfile.readline()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    
from_city = input("Enter From City: ")
to_city = input("Enter To City: ")
print(from_city,"to",to_city,"-")