Tuple = (78, 67, 44, 9, 34, 88, 11, 122, 23, 19)
print("Tuple Items = ", Tuple)

print("\nThe Even Numbers in this Tuple  are:")
for i in range(len(Tuple)):
    if(Tuple[i] % 2 == 0):
        print(Tuple[i], end = "  ")