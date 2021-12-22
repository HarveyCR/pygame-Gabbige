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
                    print("Играть!")


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


def load_data(filename):
    with open(filename, "r") as file:
        levels_map = [line.strip() for line in file]
        max_wight = max(map(len, levels_map))
        return list(map(lambda x: x.ljust(max_wight, "."), levels_map))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("")

    # class Title(pygame.sprite.Sprite):
    #     tile_images = {
    #         'wall': load_image('box.png'),
    #         "empty": load_image("grass.png")
    #     }
    #
    #     tile_size = 50
    #
    #     def __init__(self, tile_type, pos_x, pos_y):
    #         super().__init__(tiles_group, all_sprites)
    #         self.image = Title.tile_images[tile_type]
    #         self.rect = self.image.get_rect().move(Title.tile_size * pos_x, Title.tile_size * pos_y)

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()

    running = True
    fps = 60
    clock = pygame.time.Clock()

    # wall = Title("wall", 0, 0)
    # grass = Title("empty", 1, 0)
    start_screen()

    level = load_data("map.map")

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
