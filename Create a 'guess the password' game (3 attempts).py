"""
Create a 'guess the password' game , the user is given 3 attempts 
to guess the password. Set the Password as “TechClub!!”
"""
attempt=1
while(attempt<=3):
    password=input("Enter the Password : ")
    if password=="TechClub!!":
        print("You are Authenticated!!")
        break
    else:
        attempt=attempt+1
    if attempt > 3:

        print("Your Attempts are Over!!")