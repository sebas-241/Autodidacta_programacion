import pygame, sys
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

cord_x = 20
cord_y = 200

speedx = 0
speedy = 0
speedx2 = 0
speedy2 = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #Jugador 1
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
        cord_y += 10
    
    #Jugador 2
    mouse_posicion = pygame.mouse.get_pos()
    cord_x2 = mouse_posicion[0]
    cord_y2 = mouse_posicion[1]
    if cord_y2 > 500 or cord_y2 < 0:
        cord_y2 -= 10
    
           
    screen.fill(WHITE)
    cord_y += speedx    
    cord_y2 += speedx2   
    pygame.draw.rect(screen, BLACK, (cord_x, cord_y, 10, 100))
    pygame.draw.rect(screen, BLACK, (cord_x2, cord_y2, 10, 100))
    
    pygame.display.flip()
    clock.tick(30)