import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)



pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green


#### (Where to draw, color, start, end, ????) #####
pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)



####  (Where, color, tuple(topright x, topright y, width, height))####
pygame.draw.rect(gameDisplay, red, (400,400,50,25))



#### (where, color, center, radius, width? ) ####
#### pygame.draw.cricle(gameDisplay, white, (150,150), 75, 5)
pygame.draw.circle(gameDisplay, white, (150,150), 75)



#### (where, color, tuple(tuples(verticies coordinates)))  ####
#### verticies coordinates are drawn in order, can cause flips and twists ####
pygame.draw.polygon(gameDisplay, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))


#### GAMEPLAY LOOP NEEDED TO RUN CODE ABOVE ####
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
