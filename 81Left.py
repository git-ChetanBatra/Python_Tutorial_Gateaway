List = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

ltRotate = int(input("Enter Position to Left Rotate List Items = "))

print('Original List Items Before Left Rotating')
print(List)

list2 = List[ltRotate:] + List[:ltRotate]

print('\nFinal List Items After Left Rotating')
print(list2)