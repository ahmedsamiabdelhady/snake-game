import sys
sys.path.append('C:\\Users\\Sami\\Desktop')
from snake import Snake

snake = Snake()
class Grow(Snake):
    def __init__(self):
        super().__init__
        self.segments = snake.segments
    
    def grow(self):
        x = self.segments[len(self.segments) - 1].xcor() - 20
        y = self.segments[len(self.segments) - 1].ycor() - 20
        seg = (x, y)
        self.segments.append(seg)
        self.move()