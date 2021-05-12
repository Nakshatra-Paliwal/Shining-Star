import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',200)
voices = engine.getProperty('voice')
engine.setProperty('voice',voices[2])
engine.say("Hello Techies!! Let's create Alexa!!")
engine.runAndWait()
