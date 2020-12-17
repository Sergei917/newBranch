import time
import random
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтые круг')
    size = width, height = random.randint(100, 800), random.randint(100, 400)
    screen = pygame.display.set_mode(size)

    fps = 60
    clock = pygame.time.Clock()
    running = True

    center = (0, 0)
    radius = 0
    circle = False
    x_pos = 0  # пикселей в секунду
    screen.fill(pygame.Color('blue'))
    Pl = pygame.USEREVENT + 1
    pygame.time.set_timer(Pl, 10)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(pygame.Color('blue'))
                center = event.pos
                radius = 1
                circle = True
            if event.type == Pl and circle:
                radius += 1
                pygame.draw.circle(screen, pygame.Color('yellow'), center, radius)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()