"""
File: bouncing_ball.py
Name: Alice Chiu
-------------------------
The file shows how to simulate the ball bouncing.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
n = 0  # click counts

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
window.add(ball, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(click)


def bouncing_ball():
    global n
    vy = 0
    while True:
        ball.move(VX, vy)
        vy += GRAVITY
        if ball.y + SIZE >= window.height:
            vy = -vy*REDUCE
            ball.y = window.height - SIZE
        if ball.x + SIZE >= window.width:
            window.clear()
            window.add(ball, START_X, START_Y)
            break
        pause(DELAY)


def click(mouse):
    global n
    n += 1
    if n <= 3:
        bouncing_ball()


if __name__ == "__main__":
    main()
