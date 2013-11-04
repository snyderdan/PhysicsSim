import pygame
from pygame.locals import *
from PyVector import Vector

ihat = 0
jhat = 1
khat = 2

def axis2str(axis):
    if axis == ihat:
        return "i"
    elif axis == jhat:
        return "j"
    elif axis == khat:
        return "k"
    else:
        raise ValueError, "'%d' is not a valid axis number" % axis

def renderVector2D(v, scale=1, frame=(ihat,jhat), col=(255,0,0)):
    font = pygame.font.SysFont("Calibri",14)
    wh   = int(v.length())*2
    text = axis2str(frame[0]) + ", " + axis2str(frame[1])
    image = pygame.Surface((wh*scale, wh*scale))
    
    image.fill((255,255,255))
    image.blit(font.render(text, True, (0,0,0)), (0,0))
    pygame.draw.line(image, (0,0,0), (wh/2*scale,0), (wh/2*scale,wh*scale), 1)
    pygame.draw.line(image, (0,0,0), (0,wh/2*scale), (wh*scale,wh/2*scale), 1)
    pygame.draw.line(image, col, (wh/2*scale, wh/2*scale), ((wh/2+v.components[frame[0]])*scale, (wh/2-v.components[frame[1]])*scale))

    return image

pygame.init()

screen = pygame.display.set_mode((500,500))
vector = Vector((22.5,7.8,-2))
frames = ((ihat, jhat), (khat, jhat), (ihat, khat))
index  = 0

screen.fill((255,255,255))

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_UP:
                screen.fill((255,255,255))
                img   = renderVector2D(vector, scale=4, frame=frames[index])
                index = (index + 1) % 3
                screen.blit(img, (screen.get_width()/2-img.get_width()/2, screen.get_height()/2-img.get_height()/2))
        elif event.type == QUIT:
            running = False
            
    pygame.display.flip()
pygame.quit()
