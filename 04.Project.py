start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print("Prime numbers between Range", start, "to", end)
for i in range(start, end + 1):
    num = 0
    for j in range(2, (i//2 + 1)):
      if (i % j == 0):
            num = 1
            break
    if (num == 0):
        print(i, end = " ")