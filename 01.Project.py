x = int(input("Enter a value: "))
years = int(x//365)
print("years:",years )
weeks = int(x%365//7)
print("weeks:", weeks)
days = int(x%365)%7
print("days:",days)
