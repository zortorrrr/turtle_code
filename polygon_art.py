import turtle
import random

def draw_polygon(t, num_sides, size, orientation, location, color, border_size):
    t.penup()
    t.goto(location[0], location[1])
    t.setheading(orientation)
    t.color(color)
    t.pensize(border_size)
    t.pendown()
    for _ in range(num_sides):
        t.forward(size)
        t.left(360 / num_sides)
    t.penup()

def get_new_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

class ArtGenerator:
    def __init__(self, t):
        self.t = t
        turtle.colormode(255)
        turtle.bgcolor("black")


    def random_polygon_once(self, sides):
        size = random.randint(40, 150)
        orientation = random.randint(0, 360)
        location = [random.randint(-300, 300), random.randint(-250, 250)]
        color = get_new_color()
        border_size = random.randint(1, 5)
        draw_polygon(self.t, sides, size, orientation, location, color, border_size)

    def nested_polygon(self, sides):
        num_sides = sides
        size = random.randint(60, 150)
        orientation = random.randint(0, 360)
        location = [random.randint(-300, 300), random.randint(-250, 250)]
        border_size = random.randint(1, 5)


        draw_polygon(self.t, num_sides, size, orientation, location, get_new_color(), border_size)

        reduction_ratio = 0.618
        depth = random.randint(2, 5)

        for _ in range(depth - 1):

            self.t.penup()
            self.t.goto(location[0], location[1])
            self.t.setheading(orientation)
            self.t.forward(size * (1 - reduction_ratio) / 2)
            self.t.left(90)
            self.t.forward(size * (1 - reduction_ratio) / 2)
            self.t.right(90)

            location[0], location[1] = self.t.pos()
            size *= reduction_ratio

            draw_polygon(self.t, num_sides, size, orientation, location, get_new_color(), border_size)

    def art1(self):
        for _ in range(40):
            self.random_polygon_once(3)

    def art2(self):
        for _ in range(40):
            self.random_polygon_once(4)

    def art3(self):
        for _ in range(40):
            self.random_polygon_once(5)

    def art4(self):
        for _ in range(50):
            sides = random.choice([3, 4, 5])
            self.random_polygon_once(sides)

    def art5(self):
        for _ in range(30):
            self.nested_polygon(3)

    def art6(self):
        for _ in range(30):
            self.nested_polygon(4)

    def art7(self):
        for _ in range(30):
            self.nested_polygon(5)

    def art8(self):
        for _ in range(35):
            sides = random.choice([3, 4, 5])
            self.nested_polygon(sides)

    def art9(self):
        for _ in range(30):
            radchoice = random.choice(['nes','once'])
            sides = random.choice([3, 4, 5])
            if radchoice == 'nes':
                self.nested_polygon(sides)
            elif radchoice == "once":
                self.random_polygon_once(sides)


class MainProgram:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.gen = ArtGenerator(self.t)

    def run(self):
        choice = int(input("Which art do you want to generate? Enter 1-9: "))
        turtle.tracer(0)

        if 1 <= choice <= 9:
            getattr(self.gen, f"art{choice}")()
        else:
            print("Invalid choice (1-9 only).")

        turtle.update()
        turtle.done()


if __name__ == "__main__":
    app = MainProgram()
    app.run()
