import pygame
import random



pygame.init()

pygame.display.set_caption('敵を避けてゴール！')
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

x = 250
y = 250

x2 = 250
y2 = 0

x0 = 250
y0 = 470

x3 = random.randint(0,470)
y3 = random.randint(0,470)

count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += 5
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += 5

    if x < 0:
        x = 0
    elif x > 470:
        x = 470
    elif y < 0:
        y = 0
    elif y > 470:
        y = 470

    if x2 < x:
        x2 += 3
    if x2 > x:
        x2 -= 3
    elif y2 < y:
        y2 += 3
    elif y2 > y:
        y2 -= 3

    screen.fill((30,30,30))

    pygame.draw.rect(screen,(255,200,100),(x,y,30,30), border_radius=20)
    z = pygame.draw.rect(screen, (255, 0, 0), (x2, y2, 15, 15), border_radius=20)

    player_rect = pygame.Rect(x,y,15,15)
    enemy_rect = pygame.Rect(x2,y2,7,7)

    if player_rect.colliderect(enemy_rect):
        running = False
        print(f'goalは{count}回達成！')

    font = pygame.font.Font(None, 36)
    text = font.render('goal!', True,(255,255,255))
    screen.blit(text, (x3,y3))

    text_rect = pygame.Rect(x3,y3,20,20)

    if text_rect.colliderect(player_rect):
        count += 1
        x3 = random.randint(0,470)
        y3 = random.randint(0,470)





    pygame.display.flip()
    clock.tick(30)

pygame.quit()