import pygame
import sys
import random

def snake_game():
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    width, height = 640, 480
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Homless Simulator Steal Game")

    # Colors
    white = (153, 255, 194)
    black = (29, 35, 54)
    red = (255, 66, 110)
    dark_gray = (40, 40, 40)

    # Snake properties
    snake_block = 20
    snake_speed = 15

    # Snake initialization
    snake = [[width // 2, height // 2]]
    snake_direction = 'RIGHT'

    # Food initialization
    food = [random.randrange(1, (width // snake_block)) * snake_block,
            random.randrange(1, (height // snake_block)) * snake_block]

    # Score initialization
    score = 0

    # Font for displaying the score
    font = pygame.font.SysFont(None, 35)

    # Clock to control the game speed
    clock = pygame.time.Clock()

    # Flag to control when to exit the game loop
    game_over = False
    game_started = False

    # Main game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Handle key presses
            if event.type == pygame.KEYDOWN:
                if not game_started:
                    game_started = True
                if event.key == pygame.K_LEFT and not snake_direction == 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and not snake_direction == 'LEFT':
                    snake_direction = 'RIGHT'
                elif event.key == pygame.K_UP and not snake_direction == 'DOWN':
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and not snake_direction == 'UP':
                    snake_direction = 'DOWN'

        if not game_started:
            # Display a message to start the game
            win.fill(white)
            start_message = font.render("Press any key to start", True, dark_gray)
            start_rect = start_message.get_rect(center=(width // 2, height // 2))
            win.blit(start_message, start_rect)
            pygame.display.update()
            continue  # Skip the rest of the loop until a key is pressed

        # Check if the snake eats the food
        if snake[0] == food:
            score += 1
            food = [random.randrange(1, (width // snake_block)) * snake_block,
                    random.randrange(1, (height // snake_block)) * snake_block]

            # Add a new segment to the snake at the tail
            snake.append([0, 0])

        # Update the positions of the snake segments
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = list(snake[i - 1])

        # Update the position of the snake's head
        if snake_direction == 'RIGHT':
            snake[0][0] += snake_block
        elif snake_direction == 'LEFT':
            snake[0][0] -= snake_block
        elif snake_direction == 'UP':
            snake[0][1] -= snake_block
        elif snake_direction == 'DOWN':
            snake[0][1] += snake_block

        # Draw the snake and food
        win.fill(white)
        for segment in snake:
            pygame.draw.rect(win, black, [segment[0], segment[1], snake_block, snake_block])

        pygame.draw.rect(win, red, [food[0], food[1], snake_block, snake_block])

        # Draw the score counter in the middle of the screen
        text = font.render(f'Score: {score}', True, dark_gray)
        text_rect = text.get_rect(center=(width // 2, height - 30))
        win.blit(text, text_rect)

        # Update display
        pygame.display.update()

        # Update game over conditions
        if (
            snake[0][0] < 0 or
            snake[0][0] >= width or
            snake[0][1] < 0 or
            snake[0][1] >= height or
            snake[0] in snake[1:]
        ):
            game_over = True

        # Control game speed
        clock.tick(snake_speed)

    pygame.quit()
    return score
snake_game()
