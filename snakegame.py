import random
import turtle
import time


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawself(self, turtle):
        # draw a black box at its coordinates, leaving a small gap between cubes
        turtle.goto(self.x - 9, self.y - 9)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(18)
            turtle.left(90)
        turtle.end_fill()


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "ON"

    def changelocation(self):
        # I haven't programmed it to spawn outside the snake's body yet
        self.x = random.randint(0, 20)*20 - 200
        self.y = random.randint(0, 20)*20 - 200

    def drawself(self, turtle):
        # similar to the Square drawself, but blinks on and off
        if self.state == "ON":
            turtle.goto(self.x - 9, self.y - 9)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(18)
                turtle.left(90)
            turtle.end_fill()

    def changestate(self):
        # controls the blinking
        self.state = "OFF" if self.state == "ON" else "ON"


class Snake:
    def __init__(self):
        self.headposition = [20, 0] # keeps track of where it needs to go next
        self.body = [Square(-20, 0), Square(0, 0), Square(20, 0)] # body is a list of squares
        self.nextX = 1 # tells the snake which way it's going next
        self.nextY = 0
        self.crashed = False # I'll use this when I get around to collision detection
        self.nextposition = [self.headposition[0] + 20*self.nextX,
                             self.headposition[1] + 20*self.nextY]
        # prepares the next location to add to the snake

    def moveOneStep(self):
        if Square(self.nextposition[0], self.nextposition[1]) not in self.body: 
            # attempt (unsuccessful) at collision detection
            self.body.append(Square(self.nextposition[0], self.nextposition[1])) 
            # moves the snake head to the next spot, deleting the tail
            del self.body[0]
            self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y 
        # resets the head and nextposition
            self.nextposition = [self.headposition[0] + 20*self.nextX,
                                 self.headposition[1] + 20*self.nextY]
        else:
            self.crashed = True # more unsuccessful collision detection

    def moveup(self): # pretty obvious what these do
        self.nextX = 0
        self.nextY = 1

    def moveleft(self):
        self.nextX = -1
        self.nextY = 0

    def moveright(self):
        self.nextX = 1
        self.nextY = 0

    def movedown(self):
        self.nextX = 0
        self.nextY = -1

    def eatFood(self):
        # adds the next spot without deleting the tail, extending the snake by 1
        self.body.append(Square(self.nextposition[0], self.nextposition[1]))
        self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
        self.nextposition = [self.headposition[0] + 20*self.nextX,
                             self.headposition[1] + 20*self.nextY]

    def drawself(self, turtle): # draws the whole snake when called
        for segment in self.body:
            segment.drawself(turtle)


class Game:
    def __init__(self):
        # game object has a screen, a turtle, a basic snake and a food
        self.screen = turtle.Screen()
        self.artist = turtle.Turtle()
        self.artist.up()
        self.artist.hideturtle()
        self.snake = Snake()
        self.food = Food(100, 0)
        self.counter = 0 # this will be used later
        self.commandpending = False # as will this

    def nextFrame(self):
        while True: # now here's where it gets fiddly...
            game.screen.listen()
            game.screen.onkey(game.snakedown, "Down")
            game.screen.onkey(game.snakeup, "Up")
            game.screen.onkey(game.snakeleft, "Left")
            game.screen.onkey(game.snakeright, "Right")
            turtle.tracer(0) # follow it so far?
            self.artist.clear()
            if self.counter == 5: 
            # only moves to next frame every 5 loops, this was an attempt to get rid of the turning delay
                if (self.snake.nextposition[0], self.snake.nextposition[1]) == (self.food.x, self.food.y):
                    self.snake.eatFood()
                    self.food.changelocation()
                else:
                    self.snake.moveOneStep()
                self.counter = 0
            else:
                self.counter += 1
            self.food.changestate() # makes the food flash
            self.food.drawself(self.artist) # show the food and snake
            self.snake.drawself(self.artist)
            turtle.update()
            self.commandpending = False
            time.sleep(0.05)

    def snakeup(self):
        print("going up") # put this in for debugging purposes
        if not self.commandpending: 
        # should allow only one turn each frame; I don't think it's working
            self.snake.moveup()
            self.commandpending = True

    def snakedown(self):
        print("going down")
        if not self.commandpending:
            self.snake.movedown()
            self.commandpending = True

    def snakeleft(self):
        print("going left")
        if not self.commandpending:
            self.snake.moveleft()
            self.commandpending = True

    def snakeright(self):
        print("going right")
        if not self.commandpending:
            self.snake.moveright()
            self.commandpending = True


game = Game()
game.nextFrame()
print("game over!")

game.screen.mainloop()