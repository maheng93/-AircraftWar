import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 每秒刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹的常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        # 调用父类的init方法
        super().__init__()
        # 定义属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在子类中定义更新方法
        self.rect.y += self.speed


class BackGround(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        super().__init__("./images/background1.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的update方法
        super().update()
        # 图像移出屏幕后立即放在最上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，同时指定图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的随机速度
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始化位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def __del__(self):
        # print("敌机被销毁 %s" % self.rect)
        pass

    def update(self):
        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.飞出屏幕，销毁敌机精灵
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机飞出屏幕")
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""

    # 1.初始化英雄精灵
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        # 2.初始化英雄位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        else:
            self.rect.x = self.rect.x

    def fire(self):
        # print("发射子弹.....")
        # 创建子弹精灵
        for i in (0, 1, 2):
            bullet = Bullet()
            # 设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法设置子弹图片以及初始化速度
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 调用父类方法设置子弹延垂直方向
        super().update()
        # 判断字子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁....")
        pass