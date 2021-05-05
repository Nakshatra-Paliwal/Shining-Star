"""
Write a code to display menu of Ice-Cream shop as:
a. Butterscotch - Rs. 180
b. Vanila - Rs. 100
c. Mango – Rs. 150
d. Strawberry – Rs. 120
e. ChocoChips – Rs. 200
Ask user to enter the flavor to be bought and the quantity. Repeat till user wish 
to continue buying. Once user finishes buying order, generate the bill for the user.

"""
print("Display Menu of Ice-Cream Shop :-")
print("a. Butterscotch - Rs. 180 ")
print("b. Vanila - Rs. 100 ")
print("c. Mango – Rs. 150 ")
print("d. Strawberry – Rs. 120 ")
print("e. ChocoChips – Rs. 200 ")
choice = (input("Enter the Flavour you want: "))
Quan = int(input("Enter the Quantity you want: "))
Quantity1 = Quan * 180
Quantity2 = Quan * 100
Quantity3 = Quan * 150
Quantity4 = Quan * 120
Quantity5 = Quan * 200
print()
if choice==("a"):
    print("Your Bill for Butterscotch Flavour is Rs." + str(Quantity1))
if choice=="b":
    print("Your Bill for Vanila Flavour is Rs." + str(Quantity2))
if choice=="c":
    print("Your Bill for Mango Flavour is Rs." + str(Quantity3))
if choice=="d":
    print("Your Bill for Strawberry Flavour is Rs." + str(Quantity4))
if choice=="e":
    print("Your Bill for ChocoChips Flavour is Rs." + str(Quantity5))