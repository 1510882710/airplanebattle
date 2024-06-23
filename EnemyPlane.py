"""
功能: 多个敌机从上向屏幕下方移动，并能够随机发射子弹。
    单个敌机的实现，
    主要实现方法如下：
    set_used 设置飞机可用，并随机设置其初始位置
    set_unused 设置飞机不可用，并将其设置到不合法的位置
    calc_position 计算敌机位置、以及敌机发射的子弹位置
    draw_element 绘制敌机、以及敌机子弹图像
    shoot 敌机发射子弹
"""
import pygame
import random
from Bullet import Bullet
from config1 import *


class EnemyPlane:

    def __init__(self, scene, speed=10):
        # 游戏主场景
        self.scene = scene
        # 敌机资源
        self.image = pygame.image.load(f'source/plane/enemy-{random.randint(1, 4)}.png')
        # 敌机边框
        self.bbox = self.image.get_rect()
        # 移动速度
        self.speed = speed
        # 是否可见
        self.visible = False
        # 初始化子弹
        self.bullet = Bullet(scene, is_enemy=True)

    def set_used(self, start_x, start_y):
        self.bbox[0] = start_x
        self.bbox[1] = start_y
        self.speed = random.randint(4, 8)   # 每次生成的飞机是随机速度
        self.visible = True


    def calc_position(self):

        # 计算飞机位置
        if self.visible:
            self.bbox.move_ip(0, self.speed)
            if self.bbox[1] > SCENE_H:
                self.set_unused()

        # 计算子弹位置
        if self.bullet.visible:
            self.bullet.move(0, self.speed + 5)

    def draw_element(self):
        # 绘制飞机
        if self.visible:
            self.scene.blit(self.image, self.bbox)
        # 绘制子弹
        if self.bullet.visible:
            self.bullet.draw_element()

    def set_unused(self):
        self.visible = False
        self.bbox[0] = -1000    # 随意位置,只要在屏幕之外
        self.bbox[1] = -1000

    # 发射子弹
    def shoot(self):

        # 子弹可见时就不再发射
        if self.bullet.visible:
            return
        start_x = self.bbox[0] + self.bbox[2]/2 - self.bullet.bbox[2]/2
        start_y = self.bbox[1] + self.bbox[3] - 10
        self.bullet.set_used(start_x, start_y)  # 给子弹初始坐标

if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()

    enemy = EnemyPlane(window)
    enemy.set_used(random.randint(0, SCENE_W - enemy.bbox[2]), -enemy.bbox[3])

    index = 0
    while True:
        # 清空窗口
        window.fill((0, 0, 0))
        # 计算位置
        enemy.calc_position()
        # 绘制敌机
        enemy.draw_element()
        # 发射子弹
        index += 1
        if index > 120 and random.randint(1, 100) > 80 and enemy.bbox[1] < 300:
            enemy.shoot()
            index = 0

        # 敌机复活
        if not enemy.visible:
            enemy.set_used(random.randint(0, SCENE_W - enemy.bbox[2]), -enemy.bbox[3])

        pygame.event.get()
        pygame.display.update()
        clock.tick(60)