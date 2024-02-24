import pygame
import sys
import random
import threading
from playsound import playsound
import os

soundsDirectory = os.getcwd() + "/Sounds/"

def soundTrigger(soundName):
    soundThread = threading.Thread(target=soundSystem,args=(soundName,))
    soundThread.start()

def soundSystem(soundName):
    playsound(soundsDirectory + soundName)

def run_fight_game(player_damage, initial_player_health):
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 800, 600
    FPS = 60

    # Colors
    WHITE = (29, 35, 54)  # Light gray
    LIGHT_GRAY = (40, 40, 40)
    BLACK = (165, 162, 221)
    RED = (150, 255, 151)
    BLUE = (255, 176, 176)

    # Initialize Pygame screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Homeless Simulator Fight Game")
    clock = pygame.time.Clock()

    # Rhythm Bar
    rhythm_bar = pygame.Rect(0, HEIGHT // 2 - 10 , WIDTH, 20)  # Taller and more rectangular

    # Receptor
    receptor_width, receptor_height = 30, 30  # Taller and more rectangular
    receptor = pygame.Rect(0, HEIGHT // 2 - receptor_height // 2, receptor_width, receptor_height)
    receptor_speed = 16  # Constant speed

    # Spot
    spot_width, spot_height = 30, 30  # Taller and more rectangular
    spot = pygame.Rect(WIDTH // 2 - spot_width // 2, HEIGHT // 2 - spot_height // 2, spot_width, spot_height)

    # Health Bars
    player_health = initial_player_health
    enemy_health = 25

    # Fonts
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

    # Text
    instruction_text = small_font.render("Press space when the green is over the red to attack", True, LIGHT_GRAY)
    instruction_rect = instruction_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    # Main game loop
    running = True
    pygame.mixer.music.load(soundsDirectory + "Fight Game Sound.mp3")
    while running:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.queue(soundsDirectory + "Fight Game Sound.mp3")
            pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Check if the Receptor is on The Spot
                    if receptor.colliderect(spot):
                        soundTrigger("Good Hit.mp3")
                        enemy_health -= player_damage
                    else:
                        soundTrigger("Miss.mp3")
                        player_health -= random.randint(1, 5)

        # Move the Receptor
        receptor.x += receptor_speed

        # Bounce the Receptor off the edges
        if receptor.right >= WIDTH or receptor.left <= 0:
            receptor_speed *= -1

        # Update
        screen.fill(BLACK)

        # Draw Rhythm Bar
        pygame.draw.rect(screen, WHITE, rhythm_bar)

        # Draw Receptor
        pygame.draw.rect(screen, RED, receptor)

        # Draw Spot
        pygame.draw.rect(screen, BLUE, spot)

        # Draw Health Bars
        player_health_text = font.render(f"Player Health: {player_health}", True, LIGHT_GRAY)
        player_health_rect = player_health_text.get_rect(center=(WIDTH // 2, 20))
        screen.blit(player_health_text, player_health_rect)

        enemy_health_text = font.render(f"Enemy Health: {enemy_health}", True, LIGHT_GRAY)
        enemy_health_rect = enemy_health_text.get_rect(center=(WIDTH // 2, HEIGHT - 30))
        screen.blit(enemy_health_text, enemy_health_rect)

        # Draw instruction text
        screen.blit(instruction_text, instruction_rect)

        pygame.display.flip()
        clock.tick(FPS)

        # Check for game over conditions
        if player_health <= 0 or enemy_health <= 0:
            pygame.quit()
            return player_health