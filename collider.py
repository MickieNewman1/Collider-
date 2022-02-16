# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:46:36 2020

@author: mwnew
"""

import pygame
from random import *

screen = pygame.display.set_mode((800,800))
Run = True
drag = False
width = 40
height = 60
color = (0,0,0)
vel = 5
x1 = 100
x2 = 600
y1 = 200
y2 = 300
r = 20
hit = False

#create Rects
blackRect = pygame.Rect(x1,y1,r,r)
greenRect = pygame.Rect(x2,y2,r,r)

while Run:
  
    for event in pygame.event.get(): #check our event queue for useful biz
            if event.type == pygame.QUIT:
                Run = False

    #keystroke detection: blackRect moves left-right only, greenRect moves up-down only
    #how would you change this to make your own movements?
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blackRect.x -= vel
        
    if keys[pygame.K_RIGHT]:
        blackRect.x += vel
    
    if keys[pygame.K_UP]:
        greenRect.y -= vel
        
    if keys[pygame.K_DOWN]:
        greenRect.y += vel
            
    if (blackRect.colliderect(greenRect)):
        #the blackRect checks to see if the greenRect is within its boundaries
        hit = True
    
    
    screen.fill((0,0,255))
    
    if(hit): 
        #if a collision happens, hit becomes true and the shape and color changes
        pygame.draw.rect(screen,color,(blackRect.x,blackRect.y,width,height))
        pygame.draw.circle(screen, (255,0,0), (greenRect.x,greenRect.y), r) 
    else:
        #otherwise, just draw the shapes as rectangles...
        pygame.draw.rect(screen,color,(blackRect.x,blackRect.y,width,height))
        pygame.draw.rect(screen,(0,255,0),(greenRect.x,greenRect.y,width,height))

 
    pygame.display.update()