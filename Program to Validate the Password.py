"""
Create a program to validate the password, 
the password here is not Case Sensitive. 
Set the password as “creativity!”. 
Allow the user to login even if he enters, “Creativity!” or “CREATIVITY!”

"""
password = input("Enter the Password : ")

if password == "Creativity!" or password =="CREATIVITY!" or password == "creativity!" :
    print("The Password is Valid")
else:
    print("The Password is not Valid")