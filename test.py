import turtle
import time
from turtle import Screen

# window
wn = turtle.Screen()
wn.title("Molluscophobia: How to Defeat the Immortal Snail")
wn.bgcolor("black")
wn.bgpic("background_resized.gif")
wn.setup(width=1500, height=700)
wn.tracer()

# pen settings
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("black")

running = False


def start_game():
    global running

    start_message.clear()
    running = True


while not running:
    screen = Screen()
    start_message = turtle.Turtle()
    start_message.hideturtle()
    start_message.penup()
    start_message.sety(160)
    start_message.write("Press SPACE to start and jump", align="center", font=("Courier", 20, "bold"))

    screen.onkeypress(start_game, 'space')
    screen.listen()

# score
pen.goto(600, 170)
pen.write("0", move=False, align="center", font=("Courier", 25, "normal"))

# draw ground
GROUND_LEVEL = -120
pen.penup()
pen.goto(-1000, GROUND_LEVEL)
pen.pendown()
pen.goto(1000, GROUND_LEVEL)
pen.penup()

# draw snail
snail = turtle.Turtle()
snail.speed(0)
snail.penup()
turtle.register_shape("snaill.gif")
snail.shape("snaill.gif")
snail.goto(-580, GROUND_LEVEL + 50)
snail.dx = 0
snail.dy = 1

# draw pipe
pipe = turtle.Turtle()
pipe.speed(0)
pipe.penup()
turtle.register_shape("coinss.gif")
pipe.shape("coinss.gif")
pipe.goto(0, GROUND_LEVEL + 30)
pipe.dx = -15
pipe.dy = 0

# draw goal
goal = turtle.Turtle()
goal.speed(0)
goal.penup()
turtle.register_shape("pooo.gif")
goal.shape("pooo.gif")
goal.goto(500, GROUND_LEVEL + 100)
goal.dx = -15
goal.dy = 0

# draw player
player = turtle.Turtle()
player.speed(0)
player.penup()
turtle.register_shape("huuman.gif")
player.shape("huuman.gif")
player.goto(-400, GROUND_LEVEL + 50)
player.dx = 0
player.dy = 1


# Initialize game variables
player.score = 0

def hide_all():
    pen.clear()
    pen.hideturtle()
    player.hideturtle()
    pipe.hideturtle()
    goal.hideturtle()
    snail.hideturtle()
    start_message.hideturtle()

while running:
    # Update the screen

    pen.clear()
    start_message.clear()
    wn.update()

    # Add gravity
    gravity = -0.9
    player.dy += gravity

    # Move player
    y = player.ycor()
    y += player.dy
    player.sety(y)

    if GROUND_LEVEL - 10 < player.ycor() < GROUND_LEVEL + 60:
        def go_up():
            player.dy += 20
            if player.dy > 20:
                player.dy = 20


        # Keyboard binding
        wn.listen()
        wn.onkeypress(go_up, "space")

    # Bottom Border
    if player.ycor() < GROUND_LEVEL + 50:
        player.dy = 0
        player.sety(GROUND_LEVEL + 50)

    # Top Border
    if player.ycor() > GROUND_LEVEL + 200:
        player.dy = 0
        player.sety(GROUND_LEVEL + 200)

    # Move Pipe 1
    x = pipe.xcor()
    x += pipe.dx
    pipe.setx(x)

    # Move goal
    x = goal.xcor()
    x += goal.dx
    goal.setx(x)

    # Check for score
    player.score += 1
    pen.clear()
    pen.goto(600, 170)
    pen.write(player.score, move=False, align="center", font=("Arial", 25, "normal"))
    #    high_score = player.score !!!

    # collision with pipe = game over
    if (abs(pipe.xcor() - player.xcor()) < 100) and (player.ycor() - pipe.ycor() < 100):
        time.sleep(0.2)
        hide_all()
        wn.bgpic("scarysnail.png")
        pen.penup()
        pen.goto(0, 0)
    #highscore pen.write(player.score, move=False, align="center", font=("Arial", 70, "normal")) !!!

    # collision with goal = win
    if (abs(goal.xcor() - player.xcor()) < 20) and (player.ycor() - goal.ycor() < 100):
        time.sleep(0.4)
        hide_all()
        start_message.hideturtle()
        wn.bgpic("amongus.png")

wn.mainloop()
