import pygame
from plane_sprites import *

from 飞机大战.plane_sprites import GameSprite

pygame.init()
# 背景图片大小480 * 800
screen = pygame.display.set_mode((480, 700))
# 1.加载图像
background1 = pygame.image.load("./images/background1.png")
# 2.绑定图像
screen.blit(background1, (0, 0))
# 3.刷新
# pygame.display.update()
# 游戏循环
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 550))
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()
hero_rect = pygame.Rect(200, 550, 102, 126)


# 创建精灵以及精灵组
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy2.png",2)
enemyGroup = pygame.sprite.Group(enemy,enemy1)


while True:
    # 可以指定游戏循环内部的代码执行速率
    clock.tick(60)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()
    hero_rect.y -= 1
    #判断y值是否小于等于0
    if hero_rect.y <= -126:
        hero_rect.y = 574
    screen.blit(background1,(0,0))
    screen.blit(hero, hero_rect)
    # 让精灵组调用两个方法
    # update - 让组中的所有精灵更新位置
    enemyGroup.update()
    # draw - 在screen上绘制所有的位置
    enemyGroup.draw(screen)



    pygame.display.update()


