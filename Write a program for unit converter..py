"""
Write a program for unit converter. A menu of operations is displayed to the user as:
a. Meter-Cm
b. Kg-Grams
c. Liter-Ml
Ask the user to enter the choice about which conversion to be done. Ask user to enter the 
quantity to be converted and show the result after conversion. Ask user whether he wish to 
continue conversion or quit. Repeat the operations till the user wish to continue

"""
print("Display Menu of Unit Converters :-")
print("a. Meter-Cm")
print("b. Kg-Grams")
print("c. Litre-Ml ")

response = 'y'
while response == 'y':

    choice = (input("Enter the Conversion you want to Perform: "))
    Quan = int(input("Enter the Number: "))
    
    
    cm = (Quan * 100)
    kg = (Quan * 1000)
    ml = (Quan * 1000)
    print()
    if choice==("a"):
        print("Conversion of" + str(Quan) + "m to cm is :" + str(cm))
    if choice=="b":
        print("Conversion of" + str(Quan) + "m to cm is :" + str(kg))
    if choice=="c":
        print("Conversion of" + str(Quan) + "m to cm is :" + str(ml))
  
    response = input ("Do you wish to continue ? y/n : ")
print()
print ("Thank you for interacting with me!!")