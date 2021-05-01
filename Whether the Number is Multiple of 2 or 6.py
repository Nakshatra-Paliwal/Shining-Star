"""
Create a program to check whether the number is multiple of 2 or 6. 
If it is either multiple of 2 or 6 then print “Lucky Numbers” 
else “Unlucky Numbers”

"""
num = int(input("Enter the Number: "))

if num % 2==0 or num % 6==0:
    print("Lucky Numbers.")
else:
    print("Unlucky Numbers.")