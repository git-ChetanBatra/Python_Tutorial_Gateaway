a = int(input("Please Enter any Number: "))
sum = 0

for value in range(1, a + 1):
    sum = sum + value

average = sum / a

print("The Sum of Natural Numbers is",sum )
print("Average of Natural Numbers ",average)