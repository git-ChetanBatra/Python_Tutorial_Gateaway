number = int(input("Please Enter any Integer : "))

val = 1
print("The Result of a Given ",number)

while (val <= number):
    if(number % val == 0):
        print(val)
    val = val + 1