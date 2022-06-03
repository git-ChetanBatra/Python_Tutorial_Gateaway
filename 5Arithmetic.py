a=input("Enter First Number:")
b=input("Enter Second Number:")

a=int(a)
b=int(b)
t=input("Enter an Arithmetic Operation (+,-,*,/) \n")

if(t=='+'):
    print(a+b)
elif t=='-':
    print(a-b)
elif t=='*':
    print(a*b)
else:
    print(a/b)
