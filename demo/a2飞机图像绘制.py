"""
指定位置绘制图像:
    例如左上角显示出来飞机的图片

两个函数
    1. 指定位置绘制图像
    2. 图像的移动

制图像函数1:
    1，加载图像：将图片加载到PyGame中，转换为PyGame对象
    2.绘制图像
    3.刷新窗口
"""

import pygame


# 1. 指定位置绘制图像
def test01():

    pygame.init()
    window = pygame.display.set_mode([500, 500])
    clock = pygame.time.Clock()

    # 1.1 加载图像
    image = pygame.image.load('airplane1.png')
    while True:
        # 1.2 绘制图像
        window.blit(image, (0, 0))
        # 绘制部分图像
        window.blit(image, (100, 100), (0, 0, 70, 70))

        # 1.3 刷新窗口
        pygame.display.update()
        clock.tick(60)


# 2. 绘制图像移动
# def test02():
#
#     pygame.init()
#     window = pygame.display.set_mode([512, 768])
#     clock = pygame.time.Clock()
#
#     # 1.1 加载图像
#     image = pygame.image.load('hero.png')
#     postion = [0, 0]
#     while True:
#
#         # 清空窗口
#         window.fill((0, 0, 0))
#
#         # 1.2 绘制图像
#         window.blit(image, postion)
#         postion[0] += 1
#         # 1.3 刷新窗口
#         pygame.display.update()
#         clock.tick(60)


if __name__ == '__main__':
    test01()
