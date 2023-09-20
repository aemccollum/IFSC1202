s_range = int(input("Enter Start of Range: "))
e_range = int(input("Enter End of Range: ")) 
print("Special Numbers between", s_range, "and", e_range)
n = s_range + 1
i = 0
while i <= 10000:
    i = i // 10
    print(i)
    i += 1 
