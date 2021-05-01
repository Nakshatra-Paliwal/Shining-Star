"""
Enter marks in subjects, 
calculate percentage and based on the percentage decide the grade 
of the student as:

                       < 35 : Fail

                       35 - 45 : 3rd Div.

                       45 - 60: 2nd Div.

                       60 - 75: 1st Div.

                        >75 : Distinction
                        
"""

Marks1 = float( input("Enter Marks for Subject 1 : "))
Marks2 = float( input("Enter Marks for Subject 2 : "))
Marks3 = float( input("Enter Marks for Subject 3 : "))
Marks4 = float( input("Enter Marks for Subject 4 : "))
Marks5 = float( input("Enter Marks for Subject 5 : "))
Percentage = ((Marks1+Marks2+Marks3+Marks4+Marks5) / 500)*100
print()
print("Percentage: "+ str(Percentage) )

Percentage = float(input("Enter Your Percentage : "))

if Percentage<35:
    print("Fail ")
elif Percentage > 45 :
    print("3rd Div.")
elif Percentage > 60 :
    print("2nd Div.")
elif Percentage > 75 :
    print("1st Div.")
elif Percentage>85:
    print("Distinction.")

