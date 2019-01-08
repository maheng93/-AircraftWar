import pygame

pygame.init()
#背景图片大小480 * 800
screen = pygame.display.set_mode((480,800))
#1.加载图像
background1 = pygame.image.load("./images/background1.png")
#2.绑定图像
screen.blit(background1,(0,0))
#3.刷新
pygame.display.update()
#游戏循环
while True:
    pass
pygame.quit()
