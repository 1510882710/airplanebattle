"""
描述打包的配置信息。cx_Freeze
"""

from cx_Freeze import setup, Executable

# 配置信息
build_options = {
    "packages": [],  # 需要打包的额外模块
    "include_files": ["source"],  # 需要包含的额外文件或文件夹
    "excludes": [],  # 需要排除的模块
    "optimize": 2,  # 优化级别
}

# 执行文件
executables = [
    Executable("main.py", base=None)  # 主程序入口文件
]

# 执行打包
setup(
    name="MyApp",  # 程序名称
    version="1.0",  # 版本号
    description="飞机大战动态地图程序,键盘大写操控飞机,敌机出现发射子弹,碰撞检测,得分打包",  # 程序描述
    options={"build_exe": build_options},  # 打包选项
    executables=executables  # 可执行文件
)
