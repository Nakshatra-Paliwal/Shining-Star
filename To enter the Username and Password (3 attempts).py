"""
Write a program to ask user to enter the Username and Password. If Username 
& Password entered by the user doesn’t match with already stored value, then 
user will get 2 more attempts to enter correct password. If the user is
unable to enter the correct Username & Password even after 2 Attempts. Show 
the message to the user that User is blocked and End the program.

"""
attempt=1
while(attempt<=3):
    username=input("Enter the Username : ")
    password=input("Enter the Password : ")
    if username=="Nakshatra" and password=="Creative":
        print("You are Authenticated!!")
        break
    else:
        attempt=attempt+1
    if attempt > 3:

        print("Your Attempts are Over!!")
    
    