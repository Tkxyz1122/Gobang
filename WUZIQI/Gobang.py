import tkinter as tk


class GobangGame:
    def __init__(self, root):
        self.root = root
        self.root.title("五子棋游戏")

        # 棋盘属性
        self.board_size = 15
        self.cell_size = 30
        self.chess_board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1  # 1: 黑棋, 2: 白棋
        self.is_game_over = False

        # 创建界面
        self.create_widgets()
        self.start_game()  # 初始化时就显示棋盘

    def create_widgets(self):
        # 按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="重新开始", command=self.start_game)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.quit_button = tk.Button(button_frame, text="退出", command=self.root.destroy)
        self.quit_button.pack(side=tk.LEFT, padx=5)

        # 状态标签
        self.status_var = tk.StringVar()
        self.status_var.set("当前玩家: 黑棋")
        self.status_label = tk.Label(self.root, textvariable=self.status_var)
        self.status_label.pack(pady=5)

        # 棋盘画布
        canvas_width = self.board_size * self.cell_size
        canvas_height = self.board_size * self.cell_size
        self.canvas = tk.Canvas(
            self.root,
            width=canvas_width,
            height=canvas_height,
            bg="#E6C375",  # 更逼真的棋盘颜色
            highlightthickness=0
        )
        self.canvas.pack(padx=10, pady=10)

    def start_game(self):
        # 重置游戏状态
        self.chess_board = [[0] * self.board_size for _ in range(self.board_size)]
        self.current_player = 1
        self.is_game_over = False
        self.status_var.set("当前玩家: 黑棋")

        # 清空并重新绘制棋盘
        self.canvas.delete("all")
        self.draw_board()

        # 绑定鼠标点击事件
        self.canvas.bind("<Button-1>", self.place_chess)

    def draw_board(self):
        # 绘制棋盘网格
        for i in range(self.board_size):
            x = i * self.cell_size
            y = i * self.cell_size
            # 绘制横线和竖线
            self.canvas.create_line(
                self.cell_size, y + self.cell_size,
                                (self.board_size - 1) * self.cell_size, y + self.cell_size,
                width=1.5
            )
            self.canvas.create_line(
                x + self.cell_size, self.cell_size,
                x + self.cell_size, (self.board_size - 1) * self.cell_size,
                width=1.5
            )

        # 绘制五个标记点
        dots = [(3, 3), (3, 11), (7, 7), (11, 3), (11, 11)]
        for x, y in dots:
            cx = (x * self.cell_size) + self.cell_size
            cy = (y * self.cell_size) + self.cell_size
            self.canvas.create_oval(
                cx - 3, cy - 3, cx + 3, cy + 3,
                fill="black"
            )

    def place_chess(self, event):
        if self.is_game_over:
            return

        # 精确计算落子位置
        board_x = (event.x - self.cell_size) / self.cell_size
        board_y = (event.y - self.cell_size) / self.cell_size

        # 四舍五入到最近的交叉点
        grid_x = round(board_x)
        grid_y = round(board_y)

        # 检查是否在有效范围内
        if 0 <= grid_x < self.board_size and 0 <= grid_y < self.board_size:
            # 计算点击位置与最近交叉点的距离
            dx = abs(board_x - grid_x)
            dy = abs(board_y - grid_y)
            distance = (dx ** 2 + dy ** 2) ** 0.5

            # 只有当距离足够近时才允许落子
            if distance < 0.5:
                # 检查是否为空位
                if self.chess_board[grid_y][grid_x] == 0:
                    # 放置棋子
                    self.chess_board[grid_y][grid_x] = self.current_player
                    self.draw_chess(grid_x, grid_y, "black" if self.current_player == 1 else "white")

                    # 检查是否获胜
                    if self.check_win(grid_x, grid_y):
                        winner = "黑棋" if self.current_player == 1 else "白棋"
                        self.status_var.set(f"{winner}获胜!")
                        self.is_game_over = True
                        return

                    # 切换玩家
                    self.current_player = 2 if self.current_player == 1 else 1
                    self.status_var.set(f"当前玩家: {'黑棋' if self.current_player == 1 else '白棋'}")

    def draw_chess(self, x, y, color):
        # 计算棋子位置
        cx = (x * self.cell_size) + self.cell_size
        cy = (y * self.cell_size) + self.cell_size
        radius = self.cell_size // 2 - 2

        # 绘制棋子
        self.canvas.create_oval(
            cx - radius, cy - radius,
            cx + radius, cy + radius,
            fill=color, outline="black" if color == "white" else ""
        )

    def check_win(self, x, y):
        player = self.chess_board[y][x]
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for dx, dy in directions:
            count = 1

            # 检查正方向
            for i in range(1, 5):
                nx = x + dx * i
                ny = y + dy * i
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.chess_board[ny][nx] == player:
                    count += 1
                else:
                    break

            # 检查反方向
            for i in range(1, 5):
                nx = x - dx * i
                ny = y - dy * i
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size and self.chess_board[ny][nx] == player:
                    count += 1
                else:
                    break

            # 五子连珠
            if count >= 5:
                return True

        return False


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)  # 固定窗口大小
    game = GobangGame(root)
    root.mainloop()