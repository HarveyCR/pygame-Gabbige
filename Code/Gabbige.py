import sys
import pygame
import os


def load_image(name):
    fullname = os.path.join(name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


def start_screen():
    intro = ["Как играть!"]
    background = pygame.transform.scale(load_image("Menu.png"), (width, height))
    # background = pygame.transform.rotate()
    screen.blit(background, (0, 0))
    y = height // 2 + 50
    for line in intro:
        s = pygame.font.Font(None, 30).render(line, True, pygame.Color('red'))
        rect = s.get_rect()
        rect.top = y
        rect.x = width // 2 - rect.width // 2

        screen.blit(s, rect)

    running = True
    while running:
        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if 545 < event.pos[0] < 655 and 408 < event.pos[1] < 426:
                    rules()
                if 455 < event.pos[0] < 640 and 274 < event.pos[1] < 380:
                    return

        pygame.display.flip()
        clock.tick(fps)


def rules():
    background = pygame.transform.scale(load_image("Rules.png"), (width, height))
    # background = pygame.transform.rotate()
    screen.blit(background, (0, 0))
    y = height // 2 - 50
    y = height // 2 - 50
    s = pygame.font.Font(None, 30).render("Назад", True, pygame.Color('black'))

    rect = s.get_rect()
    rect.top = 680
    rect.x = 15

    screen.blit(s, rect)

    running = True
    while running:
        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if 14 < event.pos[0] < 77 and 678 < event.pos[1] < 698:
                    start_screen()
        pygame.display.flip()
        clock.tick(fps)


def Leng():
    background = pygame.transform.scale(load_image("Leng.png"), (width, height))
    # background = pygame.transform.rotate()
    screen.blit(background, (0, 0))

    running = True
    while running:
        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if 130 < event.pos[0] < 432 and 230 < event.pos[1] < 360:
                    return "rus"
                elif 704 < event.pos[0] < 1004 and 230 < event.pos[1] < 360:
                    return "eng"

        pygame.display.flip()
        clock.tick(fps)


def Difficulty():
    background = pygame.transform.scale(load_image("Dif.png"), (width, height))
    # background = pygame.transform.rotate()
    screen.blit(background, (0, 0))

    running = True
    while running:
        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if 74 < event.pos[0] < 380 and 233 < event.pos[1] < 360:
                    return "easy"
                elif 475 < event.pos[0] < 775 and 242 < event.pos[1] < 360:
                    return "normal"
                elif 840 < event.pos[0] < 1100 and 236 < event.pos[1] < 360:
                    return 'hard'

        pygame.display.flip()
        clock.tick(fps)


def Speech_part(f, s, e):
    background = pygame.transform.scale(load_image(f"ps{f}{s}{e}.png"), (width, height))
    screen.blit(background, (0, 0))

    running = True
    while running:
        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if 61 < event.pos[0] < 124 and 130 < event.pos[1] < 190:
                    f = 1
                    background = pygame.transform.scale(load_image(f"ps{f}{s}{e}.png"), (width, height))
                    screen.blit(background, (0, 0))
                elif 780 < event.pos[0] < 865 and 125 < event.pos[1] < 190:
                    s = 1
                    background = pygame.transform.scale(load_image(f"ps{f}{s}{e}.png"), (width, height))
                    screen.blit(background, (0, 0))
                if 435 < event.pos[0] < 760 and 280 < event.pos[1] < 400:
                    if f == 0 and s == 0:
                        e = 1
                        background = pygame.transform.scale(load_image(f"ps{f}{s}{e}.png"), (width, height))
                        screen.blit(background, (0, 0))
                        e = 0
                    else:
                        return f, s

        pygame.display.flip()
        clock.tick(fps)


def show_settings():
    background = pygame.transform.scale(load_image("Show.png"), (width, height))
    screen.blit(background, (0, 0))

    running = True
    while running:
        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if 545 < event.pos[0] < 655 and 408 < event.pos[1] < 426:
                    rules()
                if 455 < event.pos[0] < 640 and 274 < event.pos[1] < 380:
                    return

        pygame.display.flip()
        clock.tick(fps)


pygame.init()
size = width, height = 1200, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("")
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
running = True
fps = 60
clock = pygame.time.Clock()

start_screen()
settings = [Leng(), Difficulty(), Speech_part(0, 0, 0)]

show_settings()

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
