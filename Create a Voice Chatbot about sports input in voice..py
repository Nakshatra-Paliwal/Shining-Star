"""
Create a Voice Chatbot about sports. Ask the user to speak the name of 
any sport. The Chatbot then speaks about interesting information about 
that specific sport.
 
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
            if "cricket" in command:
                engine.say("Cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two bails balanced on three stumps.")
                engine.runAndWait()
            if "football" in command:
                engine.say("Football, also called association football or soccer, is a game involving two teams of 11 players who try to maneuver the ball into the other team's goal without using their hands or arms. The team that scores more goals wins. Football is the world's most popular ball game in numbers of participants and spectators.")
                engine.runAndWait()
            if "hockey" in command:
                engine.say("hockey, also called Field hockey, outdoor game played by two opposing teams of 11 players each who use sticks curved at the striking end to hit a small, hard ball into their opponent's goal. It is called field hockey to distinguish it from the similar game played on ice.")
                engine.runAndWait()
            if "basketball" in command:
                engine.say("Basketball is a team sport in which two teams, most commonly of five players each, opposing one another on a rectangular court, compete with the primary objective of shooting a basketball (approximately 9.4 inches (24 cm) in diameter) through the defender's hoop (a basket 18 inches (46 cm) in diameter mounted 10 feet (3.048 m) high to a backboard at each end of the court) while preventing the opposing team from shooting through their own hoop.")
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