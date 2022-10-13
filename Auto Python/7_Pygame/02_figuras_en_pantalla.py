import pygame, sys   
pygame.init()    

# Definir colores RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800, 600)

# Creando ventana
screen = pygame.display.set_mode(size)     
while True:
    for event in pygame.event.get():                         
        if event.type == pygame.QUIT:        
            sys.exit()                       
    screen.fill(WHITE)              # Pintar la pantalla de un color
    # ---- ZONA DE DIBUJO ---
    pygame.draw.line(screen, GREEN, [0, 100], [200, 300], 5)
        # Donde se quiere dibujar, color, empiece a pintar, no se sabe, grosor
    pygame.draw.rect(screen, BLACK, (100, 100, 80, 80)) 
    pygame.draw.circle(screen, RED, (200, 200), 30)
    
    for x in range(100, 800, 100):      # Uso del for en pygame par dibujar
        pygame.draw.rect(screen, BLUE, (x, 500, 80, 80))

    # ---- ZONA DE DIBUJO ---
    pygame.display.flip()           # Actualiza la pantalla