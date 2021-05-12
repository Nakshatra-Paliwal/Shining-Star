"""
Ask the User to choose a famous personality from the list (display a list in 
console). Speak out a quote by the user chosen personality.

"""
import pyttsx3 


engine=pyttsx3.init()

print("Welcome !! Choose a famous personality from the list given below & listen their famous quotes :- ")
print("1. Albert Einstein")
print("2. Walt Disney")
print("3. Nelson Mandela")
print("4. Napoleon Bonaparte")

choice = int(input("Please Enter your choice in Numbers : "))

if choice==1:
    engine.setProperty("RATE",100) 
    engine.say("Imagination is more important than knowledge.") 
    engine.runAndWait() 
    
if choice==2:
    engine.setProperty("RATE",100) 
    engine.say("All our dreams can come true, if we have the courage to pursue them.") 
    engine.runAndWait()   
    
if choice==3:
    engine.setProperty("RATE",100) 
    engine.say("I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear. ")
    engine.runAndWait() 
    
if choice==4:
    engine.setProperty("RATE",100) 
    engine.say("Victory is not always winning the battle...but rising every time you fall.") 
    engine.runAndWait() 