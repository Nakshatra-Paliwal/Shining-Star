print("Menu Card of an Ice-Cream Shop.")
print("Please Select the Flavour you wanna buy :- ")
print("1. Chocolate Flavour")
print("2. Strawberry Flavour")
print("3. Butterscotch Flavour")
choice = int(input("Enter the Flavour you want:"))
Quan = int(input("Enter the Quantity you want:"))
Quantity = Quan * 100
if choice==1:
    print("Bill for Chocolate Flavour is Rs." + str(Quantity))
if choice==2:
    print("Bill for Strawberry Flavour is Rs." + str(Quantity))
if choice==3:
    print("Bill for Butterscotch Flavour is Rs." + str(Quantity))
