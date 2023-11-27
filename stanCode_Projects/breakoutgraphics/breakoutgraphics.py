"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

move = False  # if the ball starts moving or not


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.p_o = paddle_offset
        self.__dx = 0
        self.__dy = 0
        self.count = 0  # number of failures

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset-self.paddle.height)
        self.py = window_height-paddle_offset-self.paddle.height

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-self.ball.width)/2, y=(window_height-self.ball.height)/2)
        self.original_ball = self.window.get_object_at(self.ball.x, self.ball.y)

        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmousemoved(self.change_position)
        onmouseclicked(self.start)

        # Draw bricks
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.brick_num = BRICK_ROWS * BRICK_COLS
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = colors[j//int(BRICK_ROWS / len(colors))]
                self.window.add(self.brick, x=brick_width*i+brick_spacing*i,
                                y=brick_offset+brick_spacing*j+brick_height*j)

    # Move the paddle
    def change_position(self, mouse):
        if mouse.x - self.paddle.width/2 < 0:
            self.paddle.x = 0
        elif mouse.x + self.paddle.width/2 < self.window.width:
            self.paddle.x = mouse.x - self.paddle.width/2
        else:
            self.paddle.x = self.window.width - self.paddle.width
            self.paddle.y = self.py

    def start(self, mouse):
        global move
        if move is False:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            move = True
            if random.random() > 0.5:
                self.__dx *= -1

    def ball_move(self):
        global move
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx *= -1
        if self.ball.y <= 0:
            self.__dy *= -1

        # collision check
        if self.brick_num > 0:
            # point 1
            if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
                if self.ball.y + self.ball.height < self.paddle.y:
                    self.__dx *= -1
                    self.__dy *= -1
                    self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y))
                    self.brick_num += -1
                else:
                    self.__dy *= -1
            # point 2
            elif self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y) is not None:
                if self.ball.y + self.ball.height < self.paddle.y:
                    self.__dx *= -1
                    self.__dy *= -1
                    self.window.remove(self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y))
                    self.brick_num += -1
                else:
                    self.__dx *= -1
                    self.__dy *= -1
            # point 3
            elif self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS*2) is not None:
                if self.ball.y + self.ball.height < self.paddle.y:
                    self.__dx *= -1
                    self.__dy *= -1
                    self.window.remove(self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2))
                    self.brick_num += -1
                else:
                    self.__dx *= -1
                    self.__dy *= -1
            # point 4
            elif self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y + BALL_RADIUS*2) is not None:
                if self.ball.y + self.ball.height < self.paddle.y:
                    self.__dx *= -1
                    self.__dy *= -1
                    self.window.remove(self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y + BALL_RADIUS * 2))
                    self.brick_num += -1
                else:
                    self.__dx *= -1
                    self.__dy *= -1
            else:
                if self.ball.y > self.window.height:
                    self.game_restart()
        else:
            self.game_end()

    def game_restart(self):
        global move
        move = False
        self.count += 1
        self.window.add(self.ball, (self.window.width-BALL_RADIUS)/2, (self.window.height-BALL_RADIUS)/2)
        self.__dx = 0
        self.__dy = 0

    def game_end(self):
        self.window.remove(self.ball)
        if self.count == 0:
            win_label = GLabel('Well Done! You Win! ')
            win_label.font = '-70'
            self.window.add(win_label, (self.window.width-win_label.width)/2, self.window.height/2)
        else:
            lose_label = GLabel('Game Over:( ')
            lose_label.font = '-70'
            self.window.add(lose_label, (self.window.width-lose_label.width)/2, self.window.height/2)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy
