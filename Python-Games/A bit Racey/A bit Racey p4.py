import pygame

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('J.D.Tatum: A bit Racey p4')

black = (0,0,0)
white = (255,255,255)

#1#############################################################################

red = (255,0,0)

car_width = 73

#1#############################################################################

clock = pygame.time.Clock()
####crashed = False

#Make sure this file is in the same directory as the script!!!!
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))


#2#############################################################################

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

####car_speed = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
#BAD CONTROLS: Releasing Either Key Stops "turning" Even When Another Key Is Pressed.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key -- pygame.K_RIGHT:
                    x_change = 0

        x += x_change
                

        gameDisplay.fill(white)
        car(x,y)

        if x > display_width - car_width or x < 0:
            gameExit = True

#2#############################################################################
            
        pygame.display.update()
        clock.tick(60)

#3#############################################################################        

game_loop()

#3#############################################################################

pygame.quit()
quit()
