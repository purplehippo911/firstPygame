import pygame
from player import Player
from projectile import Projectile
from enemy import Enemy

pygame.init()

screen_width = 500
screen_height = 480

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First game")

bg = pygame.image.load('images/bg.jpg')

clock = pygame.time.Clock()


def redrawGameWindow():
    win.blit(bg, (0, 0))
    player.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# main loop
player = Player(200, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.vel  # Moves the bullet by its vel
        else:
            # This will remove the bullet if it is off the screen
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if player.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
            bullets.append(Projectile(round(player.x + player.width//2),
                           round(player.y + player.height // 2), 6, (0, 0, 0), facing))
        # This will create a bullet starting at the middle of the character

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_RIGHT] and player.x < screen_width - player.width - player.vel:
        player.x += player.vel
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    if not (player.isJump):
        # if keys[pygame.K_UP] and player.y > player.vel:
        #     player.y -= player.vel
        # if keys[pygame.K_DOWN] and player.y < screen_height - player.height - player.vel:
        #     player.y += player.vel
        if keys[pygame.K_UP]:
            player.isJump = True
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    redrawGameWindow()

pygame.quit()
