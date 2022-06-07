a = int(input(" Please Enter the First Value a: "))
b = int(input(" Please Enter the Second Value b: "))

if(a > b):
    max = a
else:
    max = b

while(True):
    if(max % a == 0 and max % b == 0):
        print("\n LCM is",max)
        break;
    max = max + 1