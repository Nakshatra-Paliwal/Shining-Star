query=["Which is the brightest planet in the universe?",
       "Which is the nearest planet to the sun?",
       "Which is the nearest planet to the sun?",
       "Which planet appears to be yellowish?",
       "Which is the farthest planet of solar system?",
       "The first outside orbit of the earth planet is",
       "Which is the largest planet in solar system?",
       "What is the gap between the orbit of mars and Jupiter called?",
       "Stars appear to move from",
       "The tilting of the earth is responsible for"]

response=["Venus",
          "Mercury",
          "Earth",
          "Saturn",
          "Neptune",
          "Mars",
          "Jupiter",
          "Asteroids",
          "East to west",
          "Change of the season"]

userquery=input("Ask your Query related to 'THE SOLAR SYSTEM' : ")
for i in range (10):
    if userquery==query[i]:
        print(response[i])