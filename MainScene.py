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
import sys
import pygame
from config1 import *
from GameMap import GameMap
from HeroPlane import HeroPlane
from EnemyManager import EnemyManager

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
        # 初始化英雄飞机
        self.hero = HeroPlane(self.scene)
        # 初始化敌机序列
        self.enemy = EnemyManager(self.scene)

    # 计算坐标
    def calc_position(self):
        self.map.calc_position()
        # 计算英雄弹夹坐标
        self.hero.calc_position()
        # 计算敌机位置
        self.enemy.calc_position()

    # 绘制元素
    def draw_elements(self):
        self.map.draw_element()
        # 绘制英雄飞机
        self.hero.draw_element()
        # 绘制敌机
        self.enemy.draw_element()

    # 处理事件
    def handle_events(self):

        # 点击窗口关闭按钮
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                # 敌机出发事件
            if event.type == EnemyManager.ENEMY_START_EVENT:
                self.enemy.set_out()
                # 敌机发射子弹
            if event.type == EnemyManager.ENEMY_SHOOT_EVENT:
                self.enemy.shoot()

        # 获得当前按下的键
        keys = pygame.key.get_pressed()
        # 射击
        if keys[pygame.K_j]:
            self.hero.shoot(1)
        if keys[pygame.K_k]:
            self.hero.shoot(3)
        if keys[pygame.K_l]:
            self.hero.shoot(5)
        # 上
        if keys[pygame.K_w]:
            self.hero.top()
        # 下
        if keys[pygame.K_s]:
            self.hero.bottom()
        # 左
        if keys[pygame.K_a]:
            self.hero.left()
        # 右
        if keys[pygame.K_d]:
            self.hero.right()

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
