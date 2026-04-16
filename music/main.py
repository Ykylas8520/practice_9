import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

playlist = ["track1.mp3", "track2.mp3"
""]
n = 0

font = pygame.font.Font(None, 36)

def play():
    global n
    if os.path.exists(playlist[n]):
        pygame.mixer.music.load(playlist[n])
        pygame.mixer.music.play()
    else:
        print("File not found:", playlist[n])

running = True

while running:
    screen.fill((0, 0, 0))

    text1 = font.render("Track: " + str(n + 1), True, (255, 255, 255))
    text2 = font.render("P-Play S-Stop N-Next B-Back Q-Quit", True, (200, 200, 200))

    screen.blit(text1, (220, 150))
    screen.blit(text2, (60, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()

            if event.key == pygame.K_n:
                n += 1
                if n >= len(playlist):
                    n = 0
                play()

            if event.key == pygame.K_b:
                n -= 1
                if n < 0:
                    n = len(playlist) - 1
                play()

            if event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()
