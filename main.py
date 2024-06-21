"""
程序入口
    1. 导入主框架的文件MainScene.py
    2. 创建类MainScene的对象
    3. 对象调用 类MainScene的run函数
"""
from MainScene import MainScene


if __name__ == "__main__":
    # 创建主场景
    mainScene = MainScene()
    # 开始游戏
    mainScene.run()