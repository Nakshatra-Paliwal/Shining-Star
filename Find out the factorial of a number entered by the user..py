"""
Write a code to find out the factorial of a number entered by the user. 
For e.g. user enters 6 then factorial of 6 is: 6*5*4*3*2*1 i.e 720.

"""

factorial=1
num1 = int(input("Enter the Number : "))
for num in range(num1,0,-1):
    factorial = factorial * num
    print (factorial)
