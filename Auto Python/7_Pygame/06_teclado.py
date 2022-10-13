import pygame, sys
pygame.init()

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

cord_x = 10
cord_y = 10

speed_x = 0
speed_y = 0

clock = pygame.time.Clock()
size = (800, 600)
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Eventos del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -3
            if event.key == pygame.K_RIGHT:
                speed_x = 3
            if event.key == pygame.K_UP:
                speed_y = -3
            if event.key == pygame.K_DOWN:
                speed_y = 3
        
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0
                
                
    screen.fill(white)
    
    cord_x += speed_x
    cord_y += speed_y
    
    pygame.draw.rect(screen, black, (cord_x, cord_y, 100, 100))
    
    pygame.display.flip()
    clock.tick(60)