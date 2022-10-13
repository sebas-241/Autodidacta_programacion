import random
import pygame, sys
pygame.init()

White = (255, 255, 255)
Red = (255, 0, 0)

size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

list_cord = []
for i in range(60):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        list_cord.append([x, y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()    
            
    screen.fill(White)
    
    for j in list_cord:
        x = j[0]
        y = j[1]
        pygame.draw.circle(screen, Red, (x, y), 2)
        j[1] += 3
        if j[1] > 600:
            j[1] = 0
    
    pygame.display.flip()
    clock.tick(60)