a = []
inputfile = open("09.Project Distances.csv")
x = inputfile.readline()
while x != "":
	y = x.split(",")
	for i in range(len(y)):
		y[i] = (y[i])
	a.append(y)
	x = inputfile.readline()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
for i in range(len(a[0])):
	if from_city != a[0]:
    	print("Invalid From City")
for j in range (len(a[0])):
	if to_city != a[0]:
    	print("Invalid To City")   
from_city = input("Enter From City: ")
to_city = input("Enter To City: ")
print(from_city,"to",to_city,"-")