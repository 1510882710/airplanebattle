"""
事件处理机制
    控制图像的上下移动
    键盘控制上下移动
    鼠标的拖动
"""

import pygame

# 1. 绘制矩形
def test01():

    """
    绘制 一个矩形
    目的是熟悉对象的创建 与 绘制函数rect的使用
    :return:
    """

    pygame.init()
    window = pygame.display.set_mode([512, 500])
    pygame.display.set_caption("飞机大战")
    clock = pygame.time.Clock()
    # 创建矩形 (x, y, width, height)
    object = pygame.Rect(100, 100, 50, 50)
    while True:
        window.fill((0, 0, 0))
        # 第一个参数: 窗口对象
        # 第二个参数: 矩形颜色
        # 第三个参数: 位置尺寸
        pygame.draw.rect(window, (0, 0, 255), object)
        pygame.display.update()
        clock.tick(60)

# 关闭窗口---点击叉号
# 2. 鼠标事件
def test02():

    """
    窗口关闭事件
        点击叉号关闭主窗口
    pygame.QUIT: 代表 时间的类型, 窗口关闭按钮被点击



    :return:
    """

    pygame.init()
    window = pygame.display.set_mode([512, 500])
    pygame.display.set_caption("飞机大战")
    clock = pygame.time.Clock()
    # 创建矩形 (x, y, width, height)
    object = pygame.Rect(100, 100, 50, 50)
    is_drag = False
    while True:
        # 清屏
        window.fill((0, 0, 0))
        # 绘制
        pygame.draw.rect(window, (255, 0, 0), object)
        # 获得当前帧所有事件
        event_list = pygame.event.get()
        for event in event_list:
            # 窗口关闭事件
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()

            clock.tick(60)




if __name__ == '__main__':
    # test01()
    test02()
