"""  
Ask the user to enter his/her name. Greet the user using voice. 
Say "Hello _________! How are you today?

"""
import pyttsx3 

engine=pyttsx3.init() 

userInput=input("Please enter your name : ")

engine.setProperty("RATE",200) 

engine.say("Hello" + userInput + "!! How are you today?") 
engine.runAndWait() 