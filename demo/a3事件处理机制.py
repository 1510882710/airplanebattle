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

        pygame.display.update()
        clock.tick(60)

# 2. 鼠标事件
def test03():
    pygame.init()
    window = pygame.display.set_mode([512, 768])
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
            # 鼠标按下事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if object.collidepoint(event.pos):
                        is_drag = True
            # 鼠标弹起事件
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    is_drag = False
            # 鼠标拖动事件
            if event.type == pygame.MOUSEMOTION:
                if is_drag:
                    # 计算鼠标位置和 object 位置之间的差值
                    dx = event.pos[0] - object[0] - object[2]/2
                    dy = event.pos[1] - object[1] - object[3]/2
                    object.move_ip(dx, dy)
        pygame.display.update()
        clock.tick(30)

# 3. 键盘事件
# 3. 键盘事件
def test04():
    pygame.init()
    window = pygame.display.set_mode([512, 500])
    pygame.display.set_caption("飞机大战")
    clock = pygame.time.Clock()
    # 创建矩形 (x, y, width, height)
    object = pygame.Rect(100, 100, 50, 50)
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
        # 获得所有键的状态
        keys = pygame.key.get_pressed()
        move_speed = 10
        # 上
        if keys[pygame.K_w]:
            object.move_ip(0, -move_speed)
        # 下
        if keys[pygame.K_s]:
            object.move_ip(0, move_speed)
        # 左
        if keys[pygame.K_a]:
            object.move_ip(-move_speed, 0)
        # 右
        if keys[pygame.K_d]:
            object.move_ip(move_speed, 0)

        pygame.display.update()
        clock.tick(30)



if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    test04()