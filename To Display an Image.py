import pygame
Width = 800
Height = 600
pygame.init()
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Our First Screen")
Img = pygame.image.load("Images/Universe.jpg")
screen.blit(Img,(0,0))
EventStatus = "None"
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            EventStatus = "Quit"
            break
        if EventStatus == "Quit":
            break
print("Closing")