import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 36)

# Set up display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)

# Define paddles and ball
paddle_width, paddle_height = 15, 60
ball_size = 15
paddle_speed = 5
ball_speed = 3

player1 = pygame.Rect(10, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 10 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)

ball_dx, ball_dy = ball_speed, ball_speed
score1, score2 = 0, 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= paddle_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += paddle_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += paddle_speed

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dx = -ball_dx
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy
    if ball.left <= 0:
         score2 += 1
         ball.x, ball ,2 - ball_size // 2, HEIGHT // 2 - ball_size // 2
         ball_dx = -ball_dx

    elif ball.right >= WIDTH:
         score1 += 1
         ball.x, ball.y = WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2
         ball_dx = -ball_dx

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))
    pygame.display.flip()
    pygame.time.delay(16)