import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrow Key Controlled Bot Path Tracer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)  # Color for the traced path

# Bot properties
body_width, body_height = 80, 100
wheel_width, wheel_height = 10, 20
bot_speed = 5
rotation_speed = 3

# Path tracing
path_points = []

# Function to draw the bot
def draw_bot(x, y, angle):
    bot_surface = pygame.Surface((body_width + 20, body_height + 20), pygame.SRCALPHA)
    bot_surface.fill((0, 0, 0, 0))

    pygame.draw.rect(bot_surface, GREY, (10, 10, body_width, body_height))

    wheel_side_offset = 5
    wheel_front_offset = 20

    # Front wheels
    pygame.draw.ellipse(bot_surface, BLACK, (10 - wheel_width // 2 - wheel_side_offset, wheel_front_offset, wheel_width, wheel_height))
    pygame.draw.ellipse(bot_surface, BLACK, (10 + body_width - wheel_width // 2 + wheel_side_offset, wheel_front_offset, wheel_width, wheel_height))

    # Rear wheels
    pygame.draw.ellipse(bot_surface, BLACK, (10 - wheel_width // 2 - wheel_side_offset, body_height - wheel_front_offset - wheel_height + 10, wheel_width, wheel_height))
    pygame.draw.ellipse(bot_surface, BLACK, (10 + body_width - wheel_width // 2 + wheel_side_offset, body_height - wheel_front_offset - wheel_height + 10, wheel_width, wheel_height))

    rotated_surface = pygame.transform.rotate(bot_surface, -angle)
    rotated_rect = rotated_surface.get_rect(center=(x, y))

    screen.blit(rotated_surface, rotated_rect.topleft)

# Initialize bot state
bot_x, bot_y = WIDTH // 2, HEIGHT // 2
bot_angle = 0

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Clear path when 'C' is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                path_points.clear()

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Movement controls
    if keys[pygame.K_LEFT]:
        bot_angle += rotation_speed
    if keys[pygame.K_RIGHT]:
        bot_angle -= rotation_speed
    
    # Forward and backward movement
    if keys[pygame.K_UP]:
        # Convert angle to radians
        radians = math.radians(bot_angle)
        # Move in the direction of the angle
        bot_x += bot_speed * math.cos(radians)
        bot_y -= bot_speed * math.sin(radians)
    
    if keys[pygame.K_DOWN]:
        # Convert angle to radians
        radians = math.radians(bot_angle)
        # Move in the opposite direction of the angle
        bot_x -= bot_speed * math.cos(radians)
        bot_y += bot_speed * math.sin(radians)

    # Keep bot within screen bounds
    bot_x = max(0, min(bot_x, WIDTH))
    bot_y = max(0, min(bot_y, HEIGHT))

    # Add current position to path points
    path_points.append((int(bot_x), int(bot_y)))

    # Limit path points to prevent memory overflow
    if len(path_points) > 1000:
        path_points.pop(0)

    # Draw the traced path
    if len(path_points) >= 2:
        pygame.draw.lines(screen, RED, False, path_points, 2)

    # Draw the bot
    draw_bot(int(bot_x), int(bot_y), bot_angle)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()