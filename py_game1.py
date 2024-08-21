import pygame
from personaje import Cubo
from enemigo import Enemigo
import random


ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO,ALTO])
FPS = 60

jugando = True

reloj = pygame.time.Clock()
tiempo_passado = 0
tiempo_entre_enemigos = 550

cubo = Cubo((ANCHO/2),ALTO-125)

enemigos = []

enemigos.append(Enemigo(ANCHO/2, 100))

def gestionar_teclas(teclas):
    # if teclas[pygame.K_w]:
    #     cubo.y -= cubo.velocidad
    # if teclas[pygame.K_s]:
    #     cubo.y += cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
while jugando:
    
    tiempo_passado += reloj.tick(FPS)
    if tiempo_passado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random .randint(0,ANCHO),(-50)))
        tiempo_passado = 0

    eventos = pygame.event.get()
    
    teclas = pygame.key.get_pressed()
    
    gestionar_teclas(teclas)
    
    for evento in eventos:  
        if evento.type == pygame.QUIT:
            jugando = False
            
    VENTANA.fill("black")
    cubo.dibujar(VENTANA)    
    
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()        
    pygame.display.update()
quit()





