import pygame
import math
import datetime

pygame.init()

w, h = 600, 600
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

img = pygame.image.load("images/mickey_hand.png")
img = pygame.transform.scale(img, (200, 20))

center = (w // 2, h // 2)

def rot(image, angle):
    return pygame.transform.rotate(image, angle)

run = True

while run:
    screen.fill((255, 255, 255))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    t = datetime.datetime.now()
    sec = t.second
    minute = t.minute

    sec_angle = -sec * 6
    min_angle = -minute * 6

    sec_hand = rot(img, sec_angle)
    min_hand = rot(img, min_angle)

    sec_rect = sec_hand.get_rect(center=center)
    min_rect = min_hand.get_rect(center=center)

    pygame.draw.circle(screen, (0, 0, 0), center, 10)

    screen.blit(sec_hand, sec_rect)
    screen.blit(min_hand, min_rect)

    pygame.display.update()
    clock.tick(1)

pygame.quit()