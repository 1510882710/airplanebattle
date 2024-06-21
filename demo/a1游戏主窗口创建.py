"""
使用pygame创建游戏主窗口

步骤:
1. PyGame模块初始化
2.创建窗口
3.设置标题
4.窗口循环  ---重点理解
    不让窗口一闪而过
"""
import pygame


if __name__ == '__main__':

    # 初始化模块
    pygame.init()

    # 创建窗口
    SCENE_W, SCEBE_H = 512, 500
    window = pygame.display.set_mode([SCENE_W, SCEBE_H])

    # 设置标题
    pygame.display.set_caption("飞机大战")

    # 设置循环帧率 30FPS,60FPS
    clock = pygame.time.Clock()

    while True:

        """
        while 循环被称作窗口的主循环，它主要有两个作用：
        避免程序结束，窗口关闭
        实时在窗口中绘制其他图像
        """

        # 设置 30 帧数
        clock.tick(30)
