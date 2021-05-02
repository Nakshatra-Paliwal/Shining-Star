"""
Write a code which generates Auto Replies according to the answer by the user:
The code will ask the questions and ask user to answer the question. And code will
generate the reply for the answer. The Queries and the relies are:
Query 1: What is your name?
Reply: Hello _name_by_user !! Welcome!!
Query 2: You are from which School?
Reply: _school_nam_by_user is a renowned school in the city.
Query 3: What is your Hobby?
Reply: _Hobby_name_by_user is an Unique Hobby

"""
print("Please Answer the Below Given Questions : ")
name = input("What is your name? ")
print(name + " !! Welcome !!")
school = input ("You are from which School? ")
print(school + (" is a renowned school in the city."))
hobby = input("What is your Hobby? ")
print(hobby + " is an unique hobby.")