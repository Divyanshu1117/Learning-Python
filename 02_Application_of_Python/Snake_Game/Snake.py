author = "Divyanshu"

# Importing Modules
import pygame
import random
import os
import sys

# Initialization
pygame.init()
try:
    pygame.mixer.init()
except:
    print("Warning: Mixer could not initialize. Sounds may not work.")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SNAKE_GREEN = (35, 45, 40)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREEN_DIR = os.path.join(BASE_DIR, "Screen")
MUSIC_DIR = os.path.join(BASE_DIR, "Music")


# Safe image loader
def load_image(filename, size=(900, 600)):
    path = os.path.join(SCREEN_DIR, filename)
    try:
        return pygame.image.load(path)
    except:
        print(f"Warning: Could not load image {path}")
        return pygame.Surface(size)  # blank surface


bg2 = load_image("bg2.jpg")
intro = load_image("intro1.png")
outro = load_image("outro.png")

# Window setup
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake By Divyanshu")
pygame.display.update()


# Safe music loader
def play_music(filename, volume=0.6, loops=100):
    path = os.path.join(MUSIC_DIR, filename)
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops)
        pygame.mixer.music.set_volume(volume)
    except:
        print(f"Warning: Could not load/play music {path}")


play_music("wc.mp3")

# Game Variables
clock = pygame.time.Clock()
font = pygame.font.SysFont("Harrington", 35)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Welcome Screen
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(intro, (0, 0))
        text_screen("Press Enter to Start", RED, 300, 500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pygame.mixer.music.fadeout(200)
                play_music("bgm.mp3")
                gameloop()
        pygame.display.update()
        clock.tick(60)


# Main Game Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_size = 30
    init_velocity = 5
    fps = 60

    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = [[snake_x, snake_y]]  # Start with 1 snake block
    snk_length = 1

    # Highscore
    highscore_file = os.path.join(BASE_DIR, "highscore.txt")
    if not os.path.exists(highscore_file):
        with open(highscore_file, "w") as f:
            f.write("0")
    with open(highscore_file, "r") as f:
        highscore = f.read()
    try:
        highscore = int(highscore)
    except:
        highscore = 0

    # Food
    food_x = random.randint(20, SCREEN_WIDTH // 2)
    food_y = random.randint(20, SCREEN_HEIGHT // 2)

    score = 0

    while not exit_game:
        if game_over:
            with open(highscore_file, "w") as f:
                f.write(str(highscore))
            gameWindow.blit(outro, (0, 0))
            text_screen(f"Score: {score}", SNAKE_GREEN, 385, 350)
            text_screen("Press Enter to Restart", RED, 300, 500)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10  # cheat

            snake_x += velocity_x
            snake_y += velocity_y

            # Eating food
            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
                score += 10
                food_x = random.randint(20, SCREEN_WIDTH // 2)
                food_y = random.randint(20, SCREEN_HEIGHT // 2)
                snk_length += 5
                if score > highscore:
                    highscore = score

            gameWindow.blit(bg2, (0, 0))
            text_screen(f"Score: {score}  Highscore: {highscore}", SNAKE_GREEN, 5, 5)
            pygame.draw.rect(gameWindow, RED, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]

            # Collision
            if (
                head in snk_list[:-1]
                or snake_x < 0
                or snake_x > SCREEN_WIDTH
                or snake_y < 0
                or snake_y > SCREEN_HEIGHT
            ):
                game_over = True
                play_music("bgm1.mp3")

            plot_snake(gameWindow, BLACK, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


# Start Game
welcome()