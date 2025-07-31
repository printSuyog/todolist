import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 10

# Fonts
font = pygame.font.SysFont(None, 35)

# Score display
def draw_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, [10, 10])

# Snake
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, CELL_SIZE, CELL_SIZE])

# Game over screen
def game_over_screen(score):
    screen.fill(WHITE)
    text1 = font.render("Game Over", True, RED)
    text2 = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(text1, [WIDTH // 2 - 70, HEIGHT // 2 - 50])
    screen.blit(text2, [WIDTH // 2 - 90, HEIGHT // 2])
    pygame.display.update()
    time.sleep(2)

# Main game loop
def game_loop():
    game_over = False
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = CELL_SIZE
    dy = 0

    snake = []
    length = 1

    # Food
    food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
    food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -CELL_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = CELL_SIZE

        x += dx
        y += dy

        # Check wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over_screen(length - 1)
            break

        # Update snake
        head = [x, y]
        snake.append(head)

        if len(snake) > length:
            del snake[0]

        # Check self-collision
        for segment in snake[:-1]:
            if segment == head:
                game_over_screen(length - 1)
                return

        # Check food collision
        if x == food_x and y == food_y:
            length += 1
            food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
            food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, [food_x, food_y, CELL_SIZE, CELL_SIZE])
        draw_snake(snake)
        draw_score(length - 1)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

# Run game
game_loop()
