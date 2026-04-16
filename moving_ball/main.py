import pygame

pygame.init()

w = 800
h = 600
screen = pygame.display.set_mode((w, h))

x = 400
y = 300

running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x + 25 < w:
                x += 20
            if event.key == pygame.K_LEFT and x - 25 > 0:
                x -= 20
            if event.key == pygame.K_UP and y - 25 > 0:
                y -= 20
            if event.key == pygame.K_DOWN and y + 25 < h:
                y += 20

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.flip()

pygame.quit()