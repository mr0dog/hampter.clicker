import pygame
import math 
ismad = False


pygame.init()#initializes Pygame
print(pygame.font.get_fonts())
pygame.display.set_caption("hampter clicker")#sets the window title
screen = pygame.display.set_mode((400,400))#creates game screen

print(pygame.font.get_fonts())
#player variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0

#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 190
circY = 197
radius = 100
Catpic = pygame.image.load("hamster.png")
CatRect = Catpic.get_rect(topleft=(100,100))

CatPic2 = pygame.image.load("hampter.png")
CatRect2 = CatPic2.get_rect(topleft=(0,0))

font = pygame.font.Font('sewer.ttf', 32)
text1 = font.render('score:', False, (0, 200, 200))
text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
music = pygame.mixer.music.load('misc.mp3')
Click = pygame.mixer.Sound('ya.mp3')
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)
#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:#check if clicked
        mousePos = event.pos
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
        if math.sqrt((mousePos[0]-circX)**2+(mousePos[1]-circY)**2)<radius:
            pygame.mixer.Sound.play(Click)

            ismad = True
            numClicks+=1
            print("CLICK")
    else:
        ismad = False
            

    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        mousePos = event.pos #refreshes mouse position
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
 
#render section---------------------------------------------
    screen.fill((255, 255, 255)) #wipe screen (without this, things smear)
    text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
    screen.blit(text1, (10, 10))
    screen.blit(text2, (110, 10))
    pygame.draw.circle(screen, (255, 255, 255), (circX,circY), radius)
    
    if ismad == False:
        screen.blit(Catpic, CatRect)
    else:
        screen.blit(CatPic2, CatRect2)
    print("clicks:", numClicks) #uncomment this once collision is set up
        
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()





