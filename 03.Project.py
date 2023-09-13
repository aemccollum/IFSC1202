def add(numb1, numb2):
    return numb1 + numb2
def subtract(numb1, numb2):
    return numb1 - numb2
def divide(numb1, numb2):
    return numb1 / numb2
def multiply(numb1, numb2):
    return numb1 * numb2
print("Select Operation")
print("a. Add")
print("b. Subtract")
print("c. Divide")
print("d. Multiply")
choice = input("Enter Choice(a/b/c/d): ")
numb1= float(input("Enter First Number: "))
numb2= float(input("Enter Second Number: "))
if choice == 'a':
    print(numb1, "+", numb2, "=", add(numb1,numb2))
elif choice == 'b':
    print(numb1, "-", numb2,"=", subtract(numb1,numb2))
elif choice == 'c':
    print(numb1, "/", numb2,"=", divide(numb1,numb2))
elif choice == 'd':
    print(numb1,"*", numb2, "=", multiply(numb1,numb2))
else:
    print("Invalid Input")