print("WELCOME TO THE BOUTIQUE APP!! ")
Fabric = input("Enter the Fabric you want : ")
Colour = input("Enter the Colour you Want : ")
fabric1 = "Cotton"
colour1 = "Blue"
print()
if Fabric == fabric1 and Colour == colour1:
    print("Product is Available!!")
    Quan = int(input("Enter the Quantity you want: "))
    Quantity = Quan * 100
    print("Bill for your Fabric is Rs." + str(Quantity))
fabric2 = "Silk"
colour2 = "Pink"
if Fabric == fabric2 and Colour == colour2 :
    print("Product is Available")
    Quan = int(input("Enter the Quantity you want: "))
    Quantity = Quan * 200
    print("Bill for your Fabric is Rs." + str(Quantity))






