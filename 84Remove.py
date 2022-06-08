numTuple = (24,11,3,14,56,79,65,31,19)
print("Tuple Items = ", numTuple)

numTuple = numTuple[:3] + numTuple[4:]
print("After Removing 4th Tuple Item = ", numTuple)

numTuple = numTuple[:5] + numTuple[7:]
print("After Removing 5th and 6th Tuple Item = ", numTuple)