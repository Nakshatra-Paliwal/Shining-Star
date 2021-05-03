"""
Write a code which displays the 5 shopping items and their prices. Take the user
input of
a) Item to be bought
b) Quantity to be bought
Generate the bill according to the quantity of particular Item bought.

"""
print("Shopping Items :-")
print("Please Select the Ice Cream Flavour you wanna buy :- ")
print("1. Chocolate Flavour = Rs. 100 ")
print("2. Strawberry Flavour = Rs. 150 ")
print("3. Butterscotch Flavour = Rs. 200")
choice = int(input("Enter the Flavour you want: "))
Quan = int(input("Enter the Quantity you want: "))
Quantity1 = Quan * 100
Quantity2 = Quan * 150
Quantity3 = Quan * 200
print()
if choice==1:
    print("Your Bill is Rs." + str(Quantity1))
if choice==2:
    print("Your Bill is Rs." + str(Quantity2))
if choice==3:
    print("Your Bill is Rs." + str(Quantity3))
