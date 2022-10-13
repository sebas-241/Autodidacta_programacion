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

# Controlar los FPS del juego
clock = pygame.time.Clock()

# Coordenadas
cord_x = 400
cord_y = 240

# Velocidad a la que se movera el cuadrado 
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():                         
        if event.type == pygame.QUIT:        
            sys.exit()
                   
    # ---- Zona de Logica ---- 
    if cord_x > 720 or cord_x < 0:     
        speed_x *= -1
    if cord_y > 520 or cord_y < 0:
        speed_y *= -1
    
    cord_x += speed_x               # Animacion
    cord_y += speed_y 
                
    # ---- Zona de Logica ----    
    screen.fill(WHITE)              # Pintar la pantalla de un color
    # ---- ZONA DE DIBUJO ---

    pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))

    # ---- ZONA DE DIBUJO ---
    pygame.display.flip()           # Actualiza la pantalla
    clock.tick(60)                  # Valores de los FPS