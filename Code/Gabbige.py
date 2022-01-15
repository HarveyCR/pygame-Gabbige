import sys
import pygame
import os
import rand_word
import random


class Game_play:
    def __init__(self, settings):
        self.letter_is = []
        self.letter_not = []

        lang = settings[0]

        # Часть речи
        sp = ''
        self.three = settings[2]
        if self.three == (1, 0):
            sp = "n"
        elif self.three == (0, 1):
            sp = "v"
        elif self.three == (1, 1):
            sp = "nv"

        # Сложность
        dif = -1
        self.two = settings[1]
        if self.two == "easy":
            dif = 0
        elif self.two == "hard":
            dif = 1
        else:
            dif = 2

        self.wordr = rand_word.get_word(lang, dif, sp).lower()
        self.word = list(self.wordr)

        self.word_star = ["*" for i in range(len(self.wordr))]

        print(self.wordr)
        self.Game_start()

    def get_word(language, difficulty, p_speech):
        if language == "rus":
            f_name = 'rus'
        elif language == "eng":
            f_name = 'eng'
        else:
            print('ERROR: get_word(): Wrong "language=="', language)
            return ""

        p_sp = []
        if "n" in p_speech:
            p_sp.append("_n")
        elif "v" in p_speech:
            p_sp.append("_v")

        if len(p_sp) == 0:
            print('ERROR: get_word(): Wrong "p_speech=="', p_speech)
            return ""

        if difficulty == 0:
            a = 1
            b = 4
        elif difficulty == 1:
            a = 5
            b = 8
        elif difficulty == 2:
            a = 9
            b = 99
        else:
            print('ERROR: get_word(): Wrong "difficulty=="', difficulty)
            return ""

        a += len("\n")
        b += len("\n")
        words = []
        for v in p_sp:
            f = f_name + v + ".txt"
            with open(f) as file_txt:
                w = [s.strip("\n") for s in file_txt if a <= len(s) <= b]
                words.extend(w)
                w = []
        # print(len(words))
        rez = random.choice(words)

        words = []
        return rez

    def Game_start(self):
        background = pygame.transform.scale(load_image(f"Game_0.png"), (width, height))
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 50)
        text_star = font.render(''.join(self.word_star), True, (0, 0, 0))
        screen.blit(text_star, (492, 300))

        k = 0
        self.used_word = []
        self.not_used_word = []

        running = True
        letter_is = False
        word_is = False
        msg_letter = ''
        msg_word = ''
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0]
                    y = event.pos[1]
                    # print(x, y)

                    if 537 < x < 1072 and 506 < y < 541 and msg_letter != '':
                        if msg_letter in self.used_word:
                            text_stick = font.render(str("Введите не использованную букву"), True, (0, 0, 0))
                            screen.blit(text_stick, (485, 368))
                        else:
                            err, k = self.check_letter(msg_letter, k)

                    elif 537 < x < 1072 and 506 < y < 541 and msg_letter == '':
                        print('Введите букву')

                    elif 485 < x < 1200 and 435 < y < 490:
                        pygame.draw.rect(screen, "white", [(485, 435), (100, 50)], width=0)
                        text_stick = font.render('|', True, (0, 0, 0))
                        screen.blit(text_stick, (485, 450))
                        letter_is = True
                        msg_letter = ''

                    elif letter_is:
                        pygame.draw.rect(screen, "white", [(485, 435), (100, 50)], width=0)
                        msg_letter = ''
                        letter_is = False

                    if 573 < x < 1072 and 675 < y < 705 and msg_word != '':
                        k = self.check_word(msg_word, k)

                    elif 573 < x < 1072 and 675 < y < 705 and msg_word == '':
                        print('Введите слово')

                    elif 485 < x < 1198 and 601 < y < 657:
                        pygame.draw.rect(screen, "white", [(488, 604), (900, 53)], width=0)
                        text_stick = font.render('|', True, (0, 0, 0))
                        screen.blit(text_stick, (490, 620))
                        word_is = True
                        msg_word = ''

                    elif word_is:
                        pygame.draw.rect(screen, "white", [(488, 604), (900, 53)], width=0)
                        msg_word = ''
                        word_is = False

                if event.type == pygame.KEYDOWN:
                    if letter_is:
                        msg_letter = event.unicode
                        # print(msg_letter)
                        pygame.draw.rect(screen, "white", [(485, 435), (900, 53)], width=0)
                        text_stick = font.render(msg_letter, True, (0, 0, 0))
                        screen.blit(text_stick, (485, 450))

                    elif word_is:
                        msg_word += event.unicode
                        # print(msg_word)
                        pygame.draw.rect(screen, "white", [(488, 604), (100, 50)], width=0)
                        text_stick = font.render(msg_word, True, (0, 0, 0))
                        screen.blit(text_stick, (490, 620))

            pygame.display.flip()
            clock.tick(fps)

    pygame.quit()

    def check_letter(self, letter_is, k):
        letter = letter_is.lower()
        if k < 10:
            if letter == '' or letter.isalpha() is False:
                er = "Введите букву"
            elif letter in self.word:
                er = "Есть такая буква!"
                self.used_word.append(letter)
                r = 0
                for l in self.word:
                    if l == letter:
                        self.word_star[r] = l
                    r += 1
            elif letter not in self.word:
                er = "Такой буквы нет"
                self.not_used_word.append(letter)
                k += 1
            # print(letter)

            font = pygame.font.Font(None, 50)
            background = pygame.transform.scale(load_image(f"Game_{k}.png"), (width, height))
            screen.blit(background, (0, 0))
            stars = font.render(''.join(self.word_star), True, (0, 0, 0))
            screen.blit(stars, (492, 300))
            text_stick = font.render(str(er), True, (0, 0, 0))
            screen.blit(text_stick, (485, 368))

            text_stick = font.render(', '.join(self.used_word), True, (0, 0, 0))
            screen.blit(text_stick, (490, 70))
            text_stick = font.render(', '.join(self.not_used_word), True, (0, 0, 0))
            screen.blit(text_stick, (490, 176))
            return er, k
        else:
            Lost()
            pygame.quit()

    def check_word(self, word, k):
        name = word.lower()
        if name == self.wordr:
            Win()
        else:
            k += 1
            font = pygame.font.Font(None, 50)
            background = pygame.transform.scale(load_image(f"Game_{k}.png"), (width, height))
            screen.blit(background, (0, 0))
            text_stick = font.render(str("Неправильное слово"), True, (0, 0, 0))
            screen.blit(text_stick, (485, 368))
            if k == 10:
                Lost()
            else:
                return k


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
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("Start")
                if 545 < event.pos[0] < 655 and 408 < event.pos[1] < 426:
                    rules()
                    running = False

                if 455 < event.pos[0] < 640 and 274 < event.pos[1] < 380:
                    running = False
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("Rules")
                if 14 < event.pos[0] < 77 and 678 < event.pos[1] < 698:
                    startit()
                    running = False
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if 130 < event.pos[0] < 432 and 230 < event.pos[1] < 360:
                    return "rus"
                elif 704 < event.pos[0] < 1004 and 230 < event.pos[1] < 360:
                    return "eng"

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


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
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if 74 < event.pos[0] < 380 and 233 < event.pos[1] < 360:
                    running = False
                    return "easy"
                elif 475 < event.pos[0] < 775 and 242 < event.pos[1] < 360:
                    running = False
                    return "normal"
                elif 840 < event.pos[0] < 1100 and 236 < event.pos[1] < 360:
                    running = False
                    return 'hard'

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


def Speech_part(f, s, e):
    background = pygame.transform.scale(load_image(f"ps{f}{s}{e}.png"), (width, height))
    screen.blit(background, (0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if 61 < event.pos[0] < 124 and 130 < event.pos[1] < 190:
                    if f == 1:
                        f = 0
                    else:
                        f = 1
                    background = pygame.transform.scale(load_image(f"ps{f}{s}{e}.png"), (width, height))
                    screen.blit(background, (0, 0))
                elif 780 < event.pos[0] < 865 and 125 < event.pos[1] < 190:
                    if s == 1:
                        s = 0
                    else:
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
                        running = False
                        return f, s

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


def Win():
    background = pygame.transform.scale(load_image("Win.png"), (width, height))
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
                if 9 < event.pos[0] < 760 and 615 < event.pos[1] < 710:
                    start()
                if 782 < event.pos[0] < 1187 and 616 < event.pos[1] < 707:
                    exit()

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


def Lost():
    background = pygame.transform.scale(load_image("Lost.png"), (width, height))
    screen.blit(background, (0, 0))

    running = True
    while running:
        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 610 < event.pos[0] < 1150 and 660 < event.pos[1] < 700:
                    start()
                if 415 < event.pos[0] < 785 and 490 < event.pos[1] < 580:
                    exit()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


def show_settings(settings):
    background = pygame.transform.scale(load_image("Show.png"), (width, height))
    screen.blit(background, (0, 0))
    x, y = 518, 165
    rule = []
    for i in settings:
        if i == 'rus':
            leng = "Русский"
        elif i == 'eng':
            leng = "Английский"
        if i == "easy":
            dif = 'Легко'
        elif i == "normal":
            dif = 'Среднее'
        elif i == "hard":
            dif = "сложно"
        elif i == (1, 0):
            part = 'Существительные'
        elif i == (0, 1):
            part = 'Глагол'
        elif i == (1, 1):
            part = 'Существительные и Глагол'
    rule.append(leng)
    rule.append(dif)
    rule.append(part)

    for _ in rule:
        font = pygame.font.Font(None, 50)
        text = font.render(str(_), True, (0, 0, 0))
        screen.blit(text, (x, y))
        y += 100
    running = True
    while running:
        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 610 < event.pos[0] < 1150 and 660 < event.pos[1] < 700:
                    settings = [Leng(), Difficulty(), Speech_part(0, 0, 0)]
                    show_settings(settings)
                if 415 < event.pos[0] < 785 and 490 < event.pos[1] < 580:
                    Game_play(settings)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


def start():
    settings = [Leng(), Difficulty(), Speech_part(0, 0, 0)]
    show_settings(settings)
    return


def startit():
    start_screen()


pygame.init()
size = width, height = 1200, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("")
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
running = True
fps = 60
clock = pygame.time.Clock()

startit()
settings = [Leng(), Difficulty(), Speech_part(0, 0, 0)]
show_settings(settings)

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
