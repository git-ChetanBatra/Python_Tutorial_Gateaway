a= int(input("Please enter any integer to find divisors = "))

print("The Divisors of the Number = ")

for i in range(1, a + 1):
    if a% i == 0:
        print(i)