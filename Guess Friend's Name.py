"""
Write a code to take input as Friends name 
and if the name is “Sheela”, 
then print”She’s a Best Friend”.
If the name is “Rina” , 
then print “I know her”. 
If any other name is found 
then print “I don’t know her"

"""
friend = input("What is the Name of my Friend? ")

if friend == "Sheela":
    print("She's my Best Friend!!")
elif friend == "Rina":
    print("I Know Her!!")
else:
    print("I Don't Know Her!!")