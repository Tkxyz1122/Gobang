# 五子棋游戏  
这是一个使用 Python tkinter 库开发的简单五子棋游戏，支持双人对战，界面简洁美观，操作简单。  
# 功能特点  
15×15 标准棋盘，带有传统五子棋的星位标记  
黑白交替落子，实时显示当前玩家  
自动判断胜负，连成五子即获胜  
支持重新开始和退出游戏  
精确的鼠标点击识别，落子位置准确  
# 安装与运行  
## 环境要求  
Python 3.6 及以上版本  
无需额外安装第三方库（使用标准库 tkinter）  
## 运行方法  
将代码保存为 gobang_game.py  
打开终端或命令提示符  
导航到文件所在目录  
运行命令：python gobang_game.py  
## 使用说明  
游戏启动后自动显示棋盘，黑方先行  
点击棋盘上的交叉点放置棋子  
黑白双方轮流落子，目标是在横、竖、斜任意方向上连成五子  
游戏自动判断胜负，获胜方显示在状态栏  
点击 "重新开始" 按钮可以重置游戏  
点击 "退出" 按钮结束游戏  
## 代码结构  
游戏采用面向对象设计，主要类和方法说明：  
GobangGame 类：游戏主类  
__init__()：初始化游戏窗口和属性  
create_widgets()：创建游戏界面元素  
start_game()：开始或重新开始游戏  
draw_board()：绘制棋盘网格和星位  
place_chess()：处理鼠标点击，放置棋子  
draw_chess()：在指定位置绘制棋子  
check_win()：检查是否有玩家获胜  
## 技术细节  
使用浮点数计算鼠标位置，确保落子精度  
通过四舍五入和距离检测算法，准确识别最近的交叉点  
支持中文字符显示，界面友好  
固定窗口大小，防止界面变形  
# 贡献与改进  
如果你想改进这个游戏，可以考虑以下方向：  
添加悔棋功能  
实现人机对战（AI 功能）  
添加计时功能  
增加音效和动画效果  
改进界面设计，添加主题选择  
希望你喜欢这个简单的五子棋游戏！如有任何问题或建议，欢迎反馈。  

