import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
SNAKE_SPEED = 15
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snack Game")

# Snake initial position and direction
snake_x, snake_y = WIDTH // 2, HEIGHT // 2
snake_dx, snake_dy = 0, 0

# Snake body
snake_body = []

# Initial snack position
snack_x, snack_y = random.randint(0, WIDTH - SNAKE_SIZE), random.randint(0, HEIGHT - SNAKE_SIZE)

# Score
score = 0

# Game Over flag
game_over = False

# Clock to control game speed
clock = pygame.time.Clock()

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            elif event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # Check for collisions with the boundaries
    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        game_over = True

    # Move the snake
    snake_x += snake_dx
    snake_y += snake_dy

    # Snake body growing logic
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    if len(snake_body) > score + 1:
        del snake_body[0]

    # Check for collisions with the snack
    if snake_x == snack_x and snake_y == snack_y:
        score += 1
        snack_x, snack_y = random.randint(0, WIDTH - SNAKE_SIZE), random.randint(0, HEIGHT - SNAKE_SIZE)

    # Check for collisions with itself
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])

    # Draw the snack
    pygame.draw.rect(screen, RED, [snack_x, snack_y, SNAKE_SIZE, SNAKE_SIZE])

    # Update the display
    pygame.display.update()

    # Control the game speed
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
