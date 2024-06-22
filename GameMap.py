"""
地图滚动
    创建地图滚动类,实现无缝衔接地图
    2. 创建完对象后,需加载到 MainScene.py

    GameMap类 只需要三个函数
        def __init__(self):
            pass

        def draw_element(self):
            绘制地图所需要的图像到窗口上
            pass

        def calc_position(self):
            计算需要绘制的图像的位置
            pass
"""
import random
import pygame
from config1 import *


class GameMap:
    """地图类GameMap"""
    # 初始化地图
    def __init__(self, scene):
        """
        初始化地图
        构造函数
        """
        # 地图编号
        map_index = MAP_INDEX if MAP_INDEX >= 1 and MAP_INDEX <= 3 else random.randint(1, 3)
        map_filename = f'source/map/map-{map_index}.jpg'

        # 加载相同图片资源,做交替实现地图滚动
        self.image1 = pygame.image.load(map_filename)
        self.image2 = self.image1.copy()

        # 地图滚动速度
        self.scroll_speed = 3

        # 保存场景对象
        self.main_scene = scene

        # 初始化两张图片初始化位置
        self.y1 = 0
        self.y2 = -SCENE_H

    # 计算地图图片绘制坐标
    def calc_position(self):
        """计算地图图片绘制坐标"""
        self.y1 = 0 if self.y1 >= SCENE_H else self.y1 + self.scroll_speed
        self.y2 = -SCENE_H if self.y2 >=0 else self.y2 + self.scroll_speed

    # 绘制地图的两张图片
    def draw_element(self):
        self.main_scene.blit(self.image1, (0, self.y1))
        self.main_scene.blit(self.image2, (0, self.y2))