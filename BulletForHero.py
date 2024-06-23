"""
子弹弹夹 一次性发射3,4个子弹
    calc_position 计算所有子弹的位置
    draw_element 绘制所有子弹对象
    shoot 子弹发射的策略。在该函数的开始位置，我们增加了函数触发的间隔，例如：当键按下时，经过 10 帧时间才会发射子弹，这样有助于控制子弹发射间隔。
"""

import math
import pygame
from Bullet import Bullet


class BulletForHero:

    def __init__(self, scene):
        # 初始化子弹列表
        self.bullet_list = [Bullet(scene) for _ in range(15)]
        # 子弹发射频率
        self.frame_limit = 8
        self.frame_index = 0

    def calc_position(self):
        for bullet in self.bullet_list:
            bullet.move(0, -15)

    def draw_element(self):
        for bullet in self.bullet_list:
            bullet.draw_element()

    def shoot(self, start_x, start_y, shoot_number):

        self.frame_index += 1
        if self.frame_index < self.frame_limit:
            return
        self.frame_index = 0

        # 计算子弹初始位置
        distance = 31
        position_xs = [ start_x + (index - math.floor(shoot_number / 2)) * distance for index in range(shoot_number)]

        wait_for_shoot = []
        for bullet in self.bullet_list:
            if not bullet.visible:
                wait_for_shoot.append(bullet)
            if len(wait_for_shoot) == shoot_number:
                break

        if len(wait_for_shoot) == shoot_number:
            for bullet, x in zip(wait_for_shoot, position_xs):
                bullet.set_used(x - bullet.bbox[2]/2, start_y - bullet.bbox[3])

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode([512, 768])
    clock = pygame.time.Clock()
    # 初始化弹夹
    bullets = BulletForHero(window)
    while True:
        # 清空屏幕
        window.fill((0, 0, 0))
        # 子弹坐标
        bullets.calc_position()
        # 子弹绘制
        bullets.draw_element()
        # 发射子弹
        bullets.shoot(250, 400, 3)
        # 读取事件，避免窗口卡顿
        pygame.event.get()
        pygame.display.update()
        clock.tick(60)