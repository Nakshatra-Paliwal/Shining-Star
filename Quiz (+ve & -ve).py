"""
Write a code for the Quiz game. Ask user 3 questions with 2 Answer options.
Check the answers given by the user and update the score, 
also give feedback to the user if the answer is correct or not.

"""
score = 0
print("Q.1 By which process do Plants Make their Food? ")
print("Q.2 How to Exchange of Gases takes place in Plants?  ")
print("Q.3 By Which Process Roots Absorbs Water & Minerals? ")
ans1 = input("Your Answer 1 : ")
if ans1 == "Photosynthesis":
    print("Well Done ! Correct Answer !!")
    score = score + 1
else:
    print("Wrong Answer!!")
    score = score - 1
ans2 = input("Your Answer 2 : ")
if ans2 == "Stomata":
    print("Well Done ! Correct Answer !!")
    score = score + 1
else:
    print("Wrong Answer!!")
    score = score - 1
ans3 = input("Your Answer 3 : ")
if ans3 == "Osmosis":
    print("Well Done ! Correct Answer !!")
    score = score + 1
else:
    print("Wrong Answer!!")
    score = score - 1
print("Your Score is : " + str(score))