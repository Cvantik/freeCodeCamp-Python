class Rectangle:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for row in range(self.height):
            picture += f"{'*' * self.width}\n"
        return picture
    
    def get_amount_inside(self, shape):
        width_count = self.width // shape.width
        height_count = self.height // shape.height
        return width_count * height_count

class Square(Rectangle):

    def __init__(self, side: int):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
    set_width = set_side
    set_height = set_side
