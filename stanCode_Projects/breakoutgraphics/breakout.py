"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    while graphics.count < NUM_LIVES:
        graphics.ball_move()
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        graphics.ball.move(vx, vy)
        pause(FRAME_RATE)
    else:
        graphics.game_end()


if __name__ == '__main__':
    main()
