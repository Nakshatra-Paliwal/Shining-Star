"""Program to generate the Speech Output. 
This program uses library pyttsx3, which converts text to Speech"""


import pyttsx3 #Speech Generation Library

engine=pyttsx3.init() # Starting the Text to Speech conversion process

engine.setProperty("RATE",200) #Setting the Speed of Speech

engine.say("Hello!! Welcome to TechClub") #The Text written here will be converted to Speech
engine.runAndWait() #This function makes the program wait till speaking is over