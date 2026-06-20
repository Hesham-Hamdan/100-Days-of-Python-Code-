STARTING_X = [0, -20, -40]
MOVING_DISTANCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for x in STARTING_X:
            self.add_segment((x, 0))
