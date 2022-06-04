p=float(input("Enter marks in Physics\n"))
c=float(input("Enter marks in Chemistry\n"))
m=float(input("Enter marks in Maths\n"))

percentage=(p+c+m)/3
print(percentage)
if(percentage>60):
    print("I DIVISION")
elif(percentage<=60 and percentage>40):
    print("II DIVISION")
elif(percentage<=40 and percentage>32):
    print("III DIVISION")
else:
    print("YOU FAILED")            