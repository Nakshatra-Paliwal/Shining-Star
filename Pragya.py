import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',150)
voices = engine.getProperty('voice')
engine.setProperty('voice',voices[2])
engine.say("Hello Pragya!! How are you???? You are Genius Nakshatra's Sister know!!!! She told me about you...that you are a lazy girl!! But sometimes do some work too!!")
engine.runAndWait()
