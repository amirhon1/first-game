import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Shooter Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Bullet settings
bullet_width, bullet_height = 5, 10
bullets = []
bullet_speed = 10

# Target settings
target_width, target_height = 50, 50
targets = []
target_speed = 2
num_targets = 5

# Create targets
for _ in range(num_targets):
    target_x = random.randint(0, WIDTH - target_width)
    targets.append([target_x, 0])

# Game loop
running = True
while running:
    pygame.time.delay(30)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_width // 2, player_y])
    
    # Update bullet positions
    for bullet in bullets:
        bullet[1] -= bullet_speed
        
    # Remove off-screen bullets
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Update target positions
    for target in targets:
        target[1] += target_speed
        if target[1] > HEIGHT:
            target[0] = random.randint(0, WIDTH - target_width)
            target[1] = 0
    
    # Collision detection
    for bullet in bullets:
        for target in targets:
            if (target[0] < bullet[0] < target[0] + target_width and
                    target[1] < bullet[1] < target[1] + target_height):
                bullets.remove(bullet)
                targets.remove(target)
                targets.append([random.randint(0, WIDTH - target_width), 0])
                break

    # Drawing
    screen.fill(WHITE)
    
    # Draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))
    
    # Draw targets
    for target in targets:
        pygame.draw.rect(screen, BLACK, (target[0], target[1], target_width, target_height))

    pygame.display.update()

# Quit Pygame
pygame.quit()
