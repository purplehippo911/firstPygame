import pygame
pygame.init()

screen_width = 500
screen_height = 480

win = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("First game")


walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load(
    'images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load(
    'images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 40
height = 60
vel = 5
color = (255, 0, 0)

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))
    if walkCount + 1 > 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    # pygame.draw.rect(win, color, (x, y, width, height, vel))
    pygame.display.update()


run = True
while run:
    clock.tick(27)

    # class Character():
    #     def __init__(self, x, y, width, height, vel, color):
    #         self.x = x
    #         self.y = y
    #         self.width = width
    #         self.height = height
    #         self.vel = vel
    #         self.color = color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # block = Character(50, 440, 40, 60, 5, (255, 0, 0))

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not (isJump):
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < screen_height - height - vel:
        #     y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()
