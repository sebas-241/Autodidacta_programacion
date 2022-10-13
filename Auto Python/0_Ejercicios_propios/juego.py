import pygame, sys
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cord_x = 20
cord_y = 200
speedx = 0
speedy = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            speedx = -3
        if event.key == pygame.K_DOWN:
            speedx = 3
            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            speedx = 0
        if event.key == pygame.K_DOWN:
            speedx = 0
    
    if cord_y > 500 or cord_y < 0:     
        cord_y = -1
            
    screen.fill(WHITE)
    cord_y += speedx       
    pygame.draw.rect(screen, BLACK, (cord_x, cord_y, 10, 100))
    
    pygame.display.flip()
    clock.tick(60)