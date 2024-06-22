"""
游戏主窗口文件
    MainScene 类表示游戏主场景，负责游戏的核心逻辑：
    初始化主场景
	 def __init__(self):
	    创建主窗口,飞机大战等标题

    四个基本步骤的函数
    计算坐标,绘制元素,处理事件,碰撞检测

     主循环
    def run(self):
        while True:
        四种函数一直循环
"""

import pygame
from config1 import *
from GameMap import GameMap


# 主场景
class MainScene(object):

    """
    MainScene 类表示游戏主场景，负责游戏的核心逻辑
    """

    # 初始化主场景
    def __init__(self):
        # 初始化模块
        pygame.init()
        # 初始化时钟
        self.clock = pygame.time.Clock()
        # 初始化游戏窗口
        self.scene = pygame.display.set_mode((SCENE_W, SCENE_H))
        # 设置窗口标题
        pygame.display.set_caption("飞机大战-v1.0 作者: xyxwfg")
        # 初始化游戏元素
        self.init_elements()

    # 初始化游戏元素
    def init_elements(self):
        # 初始化游戏地图
        self.map = GameMap(self.scene)

    # 计算坐标
    def calc_position(self):
        self.map.calc_position()

    # 绘制元素
    def draw_elements(self):
        self.map.draw_element()

    # 处理事件
    def handle_events(self):
        pygame.event.get()

    # 碰撞检测
    def detect_conlision(self):
        pass

    # 主循环
    def run(self):
        while True:
            # 碰撞检测
            self.detect_conlision()
            # 计算元素坐标
            self.calc_position()
            # 绘制元素图片
            self.draw_elements()
            # 处理事件
            self.handle_events()
            # 刷新显示
            pygame.display.update()
            # 控制帧率
            self.clock.tick(60)
