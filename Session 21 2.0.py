from Session21 import foodRA

def createlist():
    lists = []
    count = int(input("Enter the amount of items you want to purchase"))
    while count<1:
        print("Please re-enter a value more or equal to 1")
        count = int(input("Enter the amount of items you want to purchase"))
    for i in range(count):
        print(f"Item #{i+1}-")
        name = input("Enter food name: ")
        foodAmount = float(input("Enter amount of pounds: "))
        while foodAmount <= 0 :
            foodAmount = float(input("Enter amount of pounds you want to buy"))
        lists.append(foodRA(name, foodAmount))
    
    return lists

def resultRA(lists):
    print("Here's a summary of the items purchased:")
    print("---------------------------")
    for food in lists:
        print(f"Item: {food.foodName}")
        print(f"Amount ordered: {food.amountOfFood} lbs")
        standardPrice = "{:.2f}".format(food.standardPrice)
        print(f"Price per pound: ${standardPrice}")
        calculatedPrice = "{:.2f}".format(food.calculatedPrice)
        print(f"Price of order: ${calculatedPrice}")
        print(" ")    

def totalCostCalculatorRA(lists):
    totalPrice = 0
    for foodData in lists:
        totalPrice += foodData.calculatedPrice
        totalPriceRounded = "{:.2f}".format(totalPrice)
    print(f"Total cost: ${totalPriceRounded}")

def startRA():
    lists = createlist()
    resultRA(lists)
    totalCostCalculatorRA(lists)

startRA()
