import pygame, sys   # Importar la libreria
pygame.init()   # Inicializar la libreria 

size = (800, 600)

# Creando ventana
screen = pygame.display.set_mode(size)      # Crea pantalla
while True:
    for event in pygame.event.get():         # Verificica el evento
        #print(event)                        Muestra los eventos en consola (opcional)
        if event.type == pygame.QUIT:        # Si el evento es QUIT
            sys.exit()                       # Se quita la ventana

