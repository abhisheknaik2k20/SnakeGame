class Position:
    def __init__(self, x, y, size=None) : self.x, self.y, self.size = x, y, size

    def is_overlapping(self, object1, object2):
        x_overlap = object1.x < object2.x + object2.size and object1.x + object1.size > object2.x
        y_overlap = object1.y < object2.y + object2.size and object1.y + object1.size > object2.y
        return x_overlap and y_overlap