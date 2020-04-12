import random
import os
from hm_pygame.hm_game_utils import *


class GameSprite(pygame.sprite.Sprite):
    """ 游戏精灵类 """

    def __init__(self, img_name, speed=PER_SPACE, image=None):
        super().__init__()
        self.image_url = img_name
        if img_name is None:
            self.image = image
        else:
            self.image = pygame.image.load(img_name)
        self.rect = self.image.get_rect()
        # self.rect.size = (1,2)
        print("精灵创建", "=" * 10, self.image_url, self.rect)
        self.speed = speed

    def update(self):
        """ 更新飞机速度 """
        self.rect.y += self.speed

    def __del__(self):
        print("精灵销毁 %s : %s" % (type(self), self.rect))


class BackGround(GameSprite):
    """ 背景精灵组 """

    def __init__(self, img_name="./images/background.png", speed=PER_SPACE, is_alt=False):
        super().__init__(img_name, speed)
        if is_alt:
            self.rect.y = -SCREEN_RECT.height

    def update(self):
        """ 背景拼接，如果背景移动结束"""
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = - SCREEN_RECT.height


class Enemy(GameSprite):
    """ 敌机精灵"""

    def __init__(self):
        speed = random.randint(1, 6)
        img_name = "./images/enemy1.png"
        if speed == 3:
            img_name = "./images/enemy2.png"
        elif speed == 2:
            img_name = "./images/enemy3.png"
        elif speed == 1:
            img_name = "./images/enemy3.png"
        elif speed == 5:
            img_name = "./images/bullet_supply.png"
        elif speed == 6:
            img_name = "./images/bomb_supply.png"
            speed = 4
        super().__init__(img_name, speed > 1 and speed - 1 or speed)
        self.rect.bottom = 0
        self.rect.x = random.randint(1, SCREEN_RECT.width)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # 敌机飞出，需要销毁
            self.kill()


class Hero(GameSprite):
    bullet_group = pygame.sprite.Group()

    def __init__(self, img_name="./images/me1.png", speed=0):
        super().__init__(img_name, speed)
        self.rect.bottom = SCREEN_RECT.bottom
        self.rect.centerx = SCREEN_RECT.centerx
        # 创建子弹

    def update(self):
        rect_ = self.rect
        if rect_.centerx > SCREEN_RECT.right:
            rect_.centerx = SCREEN_RECT.right
        if rect_.centery > SCREEN_RECT.bottom:
            rect_.centery = SCREEN_RECT.bottom

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet(i % 2 == 0 and "./images/bullet1.png" or "./images/bullet2.png")
            bullet.rect.bottom = self.rect.y - 15 * i
            bullet.rect.centerx = self.rect.centerx
            Hero.bullet_group.add(bullet)


class Bullet(GameSprite):
    """ 子弹类"""

    def __init__(self, image="./images/bullet1.png", speed=-5):
        super().__init__(image, speed)

    def update(self):
        super().update()
        rect_ = self.rect
        if rect_.bottom < SCREEN_RECT.x:
            self.kill()


class Bomb(GameSprite):
    """ 炸弹效果 """

    def __init__(self, img_name, rect):
        super().__init__(img_name)
        self.rect = rect

    def update(self):
        super().update()
        image_ = self.image_url
        a = image_.split(".")
        if a[1].find("_down") > -1:
            temp = int(image_[-5]) + 1
            if temp < 7:
                image_ = '.' + a[1][:-1] + str(temp) + '.' + a[2]
            else:
                self.kill()
        else:
            image_ = '.' + a[1] + "_down1" + '.' + a[2]
        if os.path.isfile(image_):
            self.image = pygame.image.load(image_)
            self.image_url = image_
            return
        self.kill()


class GameOn(GameSprite):
    """ 继续游戏精灵 """

    def __init__(self, image="./images/again.png", speed=0, x=SCREEN_RECT.centerx, y=SCREEN_RECT.centery):
        super().__init__(image, speed)
        self.rect.centery = y
        self.rect.centerx = x

    def update(self):
        pass


class GameIcon(GameSprite):
    """ 继续GameIcon精灵 """

    def __init__(self, image_url="./images/again.png", speed=0, x=0, y=0, imag=None):
        super().__init__(image_url, speed, image=imag)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
