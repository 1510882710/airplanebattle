"""
单个子弹类
    1. move 子弹移动函数，根据具体的子弹发射策略来指定子弹的移动方向
    2. draw_element 绘制子弹对象
    3. set_unused 当子弹无效时设置可不见，并将其设置到一个不合法的位置上
    4. set_used 当子弹发射时设置可见，并设置初始位置
"""

import random
import pygame
from config1 import *

class Bullet:

    def __init__(self, scene, is_enemy=False):

        # 保存主场景
        self.scene = scene
        # 子弹是否可见 默认不可用
        self.visible = False
        # 加载子弹资源
        bullet_index = ENEM_BULLET_INDEX if is_enemy else HERO_BULLET_INDEX
        bullet_filename = f'source/bullet/bullet_{bullet_index}.png'
        self.image = pygame.image.load(bullet_filename)
        if is_enemy:
            self.image = pygame.transform.flip(self.image, False, True)
        # 子弹位置边框
        self.bbox = self.image.get_rect()

    def move(self, dx, dy):
        if not self.visible:
            return
        self.bbox.move_ip(dx, dy)
        if self.bbox[1] < 0 or self.bbox[1] > SCENE_H - 10:
            self.set_unused()

    def draw_element(self):
        if not self.visible:
            return
        self.scene.blit(self.image, self.bbox)

    def set_unused(self):
        self.visible = False
        self.bbox[0] = -1000
        self.bbox[1] = -1000

    def set_used(self, start_x, start_y):
        self.visible = True     # 初始位置,且子弹设置为可见 不然绘制时绘制不进来
        self.bbox[0] = start_x
        self.bbox[1] = start_y


if __name__ == '__main__':

    # 创建窗口
    pygame.init()
    window = pygame.display.set_mode([500, 500])
    clock = pygame.time.Clock()

    # 初始化子弹
    bullet1 = Bullet(window)
    bullet1.set_used(100, 400)

    bullet2 = Bullet(window)
    bullet2.set_used(300, 400)

    while True:

        # 清空屏幕
        window.fill((0, 0, 0))

        # 子弹坐标
        bullet1.move(0, -5)   # 每一帧向上移动5个像素
        bullet2.move(0, -3)

        # 子弹绘制
        bullet1.draw_element()
        bullet2.draw_element()

        if bullet1.bbox[1] <= 0:
            bullet1.set_used(100, 600)

        if bullet2.bbox[1] <= 0:
            bullet2.set_used(300, 600)

        # 读取事件，避免窗口卡顿
        pygame.event.get()

        pygame.display.update()     # 刷新屏幕,不然看不到
        clock.tick(60)
