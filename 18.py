cost=int(input("Enter the cost price\n"))
sale=int(input("Enter the sale price\n"))

if(sale>cost):
    profit=sale-cost
    print("Profit of",profit)
elif(cost>sale):
    loss=cost-sale
    print("Loss of",loss)    