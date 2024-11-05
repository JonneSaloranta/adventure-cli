import math

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return 2

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        return self / self.magnitude()

    def distance(self, other):
        return (self - other).magnitude()

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def angle(self, other):
        return math.acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def rotate(self, angle):
        return Vector2D(self.x * math.cos(angle) - self.y * math.sin(angle),
                        self.x * math.sin(angle) + self.y * math.cos(angle))

    def reflect(self, normal):
        return self - normal * 2 * self.dot(normal)