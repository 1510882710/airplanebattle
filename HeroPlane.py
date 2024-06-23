"""
英雄飞机的类
    英雄飞机的移动是由按键事件驱动
    top、bottom、left、right 4 个函数是飞机在不同方向上的移动函数
    shoot 用于发射子弹
    draw_element 绘制英雄飞机、以及英雄飞机发射出的子弹
    calc_position 计算英雄飞机、以及英雄飞机发射子弹的坐标
"""
import pygame
import random
from BulletForHero import BulletForHero
from config1 import *


class HeroPlane:

    def __init__(self, scene):
        # 游戏主场景
        self.scene = scene
        # 英雄飞机资源
        self.image = pygame.image.load(f'source/plane/hero.png')
        # 英雄飞机边框
        self.bbox = self.image.get_rect()
        # 初始化飞机位置
        self.bbox[0] = SCENE_W / 2 - self.bbox[2] / 2
        self.bbox[1] = SCENE_H - self.bbox[3] - 10
        # 初始化弹夹
        self.bullets = BulletForHero(scene)
        # 移动速度
        self.speed = 4


    def top(self):
        if self.bbox[1] <= 0:
            return
        self.bbox.move_ip(0, -self.speed)

    def bottom(self):
        if self.bbox[1] >= SCENE_H - self.bbox[3]:
            return
        self.bbox.move_ip(0, self.speed)

    def left(self):
        if self.bbox[0] <= 0:
            return
        self.bbox.move_ip(-self.speed, 0)

    def right(self):
        if self.bbox[0] >= (SCENE_W - self.bbox[2]):
            return
        self.bbox.move_ip(self.speed, 0)

    def shoot(self, num):
        shoot_x = self.bbox[0] + self.bbox[2] / 2
        shoot_y = self.bbox[1]
        self.bullets.shoot(shoot_x, shoot_y, num)

    def draw_element(self):
        self.scene.blit(self.image, self.bbox)
        self.bullets.draw_element()

    def calc_position(self):
        self.bullets.calc_position()

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()
    # 初始化英雄飞机
    hero = HeroPlane(window)
    actions = [hero.left, hero.right, hero.top, hero.bottom]

    index = 0
    action_index = 0
    while True:

        # 清空窗口
        window.fill((0, 0, 0))
        # 计算坐标
        hero.calc_position()
        # 绘制图像
        hero.draw_element()
        # 发射子弹
        hero.shoot(3)

        # 随机选择方向
        actions[action_index]()
        index += 1
        if index > 50:
            action_index = random.randint(0, 3)
            index = 0

        pygame.event.get()
        pygame.display.update()
        clock.tick(60)