import pygame
pygame.init()
screen=pygame.display.set_mode((700,700))
clock=pygame.time.Clock()
done=False
screen.fill((255,255,255))
x=25
y=25
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 20
    if pressed[pygame.K_DOWN]:
        y += 20
    if pressed[pygame.K_RIGHT]:
        x += 20
    if pressed[pygame.K_LEFT]:
        x -= 20
    if x + 25 > 700:
        x = 675
    if x < 25:
        x = 25
    if y + 25 > 700:
        y = 675
    if y < 25:
        y = 25
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen,(0,255,255),[x,y],25)
    pygame.display.flip()
    clock.tick(60)
