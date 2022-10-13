import pygame, sys
pygame.init()

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.mouse.set_visible(0)     # Visibilidad del mouse 0 = false, 1 = true

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    posicion_mouse = pygame.mouse.get_pos()
    x = posicion_mouse[0]
    y = posicion_mouse[1]
    #print(posicion_mouse)
    screen.fill(white)
    
    
    pygame.draw.rect(screen, black, (x, y, 100, 100))
    
    pygame.display.flip()
    clock.tick(60)