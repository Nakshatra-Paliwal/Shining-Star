"""
Create a Area of Rectangle Calculator by asking user to enter 
Length and Breadth. Continue calculating Area till user say “no”.
"""
choice ='y'

while(choice=='y'):
    length = int(input("Enter the Length of Rectangle: "))
    breadth = int(input("Enter the Breadth of Rectangle: "))
    
    Area = length*breadth
    
    print("Area of the Rectangle"+" is "+str(Area))
    
    choice = input("Wish to continue calculating: (enter y/n) ")

print("Thanks for using Rectangle calculator.")