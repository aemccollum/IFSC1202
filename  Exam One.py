start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print("Super Special Numbers Between", start, "and", end)
for i in range (start, end + 1):
    num = i
    sum = 0
    while num > 0: 
        rem = num % 10
        factorial = 1
        for i in range(1, rem + 1):
            factorial *= i
        sum += factorial
        num = num // 10
        if num == sum:
            print(i)
        if rem > 0:
            rem = num % 10
            factorial = 1
            for i in range(1, rem + 1):
                factorial *= i
            sum += factorial
            num = num // 10
    if num == sum:
        print(i)









