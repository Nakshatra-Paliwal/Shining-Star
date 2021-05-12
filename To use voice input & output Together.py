"""
To use voice input & output Together

"""

#Using speech_recognition library
import speech_recognition as speech
import pyttsx3

engine=pyttsx3.init()


while True:
    try:
        #Take the user input to activate reception of Voice Commands
        activate=input("Press 's' to start voice commands and q to quit :")    
        
        if activate=='s':
            
            #Take Voice Input
            r=speech.Recognizer()
            with speech.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Speak:")
                audio=r.listen(source)
            #Convert Voice Commands to Text
            command=r.recognize_google(audio)
            print("You said: "+command) 
            if "runs" in command:
                engine.say("Highest runs are scored by")
                engine.runAndWait()
            
            
        else:
            break
   
    #Stop Services and Exit the Program
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
print("Nice interacting with you!!")