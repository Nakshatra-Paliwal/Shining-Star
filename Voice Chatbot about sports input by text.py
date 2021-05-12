"""
Create a Voice Chatbot about sports. Ask the user to type the name of any 
sport. The Chatbot then speaks about interesting information about that 
specific sport.

"""

import pyttsx3 


engine=pyttsx3.init()

print("Welcome !! This is a Voice Chatbot about sports.")
print("Please choose the Operation:")
print("1. Cricket")
print("2. Football")
print("3. Hockey")
print("4. Basketball")

choice = int(input("Please Enter your choice in Numbers : "))

if choice==1:
    engine.setProperty("RATE",100) 
    engine.say("Cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two bails balanced on three stumps.") 
    engine.runAndWait() 
    
if choice==2:
    engine.setProperty("RATE",100) 
    engine.say("Football, also called association football or soccer, is a game involving two teams of 11 players who try to maneuver the ball into the other team's goal without using their hands or arms. The team that scores more goals wins. Football is the world's most popular ball game in numbers of participants and spectators.") 
    engine.runAndWait()   
    
if choice==3:
    engine.setProperty("RATE",100) 
    engine.say("hockey, also called Field hockey, outdoor game played by two opposing teams of 11 players each who use sticks curved at the striking end to hit a small, hard ball into their opponent's goal. It is called field hockey to distinguish it from the similar game played on ice.")
    engine.runAndWait() 
    
if choice==4:
    engine.setProperty("RATE",100) 
    engine.say("Basketball is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court, compete with the primary objective of shooting a basketball (approximately 9.4 inches (24 cm) in diameter) through the defender's hoop (a basket 18 inches (46 cm) in diameter mounted 10 feet (3.048 m) high to a backboard at each end of the court) while preventing the opposing team from shooting through their own hoop.") 
    engine.runAndWait() 