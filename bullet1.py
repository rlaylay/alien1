import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
   """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
       """在飞船所在位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

   # 加载子弹图案，并设置其rect属性
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)


        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        self.y -=self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)