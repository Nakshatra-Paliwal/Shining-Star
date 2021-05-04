"""
Write a code which finds the square of any number entered by the user. 
Program should ask user whether he wish to continue, if user responds in 
‘yes’ then program asks to enter number again and finds the square of it.
If user doesn’t wish to continue then the program ends.

"""

response = 'y'
while response == 'y':

        choice = int(input("Enter your number: "))
        num = choice ** 2
        print("The Square of " + str(choice) + " is : " + str(num))
        response = input ("Do you wish to continue ? y/n : ")

print ("Thank you for interacting with me!!")
