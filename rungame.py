import turtle
import time
from turtle import Screen
from classes import Sprite
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
    wn.bgpic("background_resized.gif")
    start_message.hideturtle()
    running = True
    start_game_fr()


# score
# draw ground
GROUND_LEVEL = -120
pen.penup()
pen.goto(-1000, GROUND_LEVEL)
pen.pendown()
pen.goto(1000, GROUND_LEVEL)
pen.penup()

# draw snail


def spawn_snail():
    snail = Sprite(-580, GROUND_LEVEL + 50, "snaill.gif")
    snail.dx = 0
    snail.dy = 1
    return snail

# draw pipe


def spawn_coins():
    coins = Sprite(0, GROUND_LEVEL+30, "coinss.gif")
    coins.set_bounding_circle(100, 100)
    coins.dx = -15
    coins.dy = 0
    return coins

# draw goal


def spawn_goal():
    goal = Sprite(500, GROUND_LEVEL + 100, "pooo.gif")
    goal.dx = -15
    goal.dy = 0
    return goal

# draw player


def spawn_player():
    player = Sprite(-400, GROUND_LEVEL + 50, "huuman.gif")
    player.set_bounding_circle(100, 100)
    player.dx = 0
    player.dy = 1
    return player


def spawn_spike():
    spike = Sprite(200, GROUND_LEVEL+30, "amongwalk.gif")
    spike.dx = -15
    spike.dy = 0
    spike.set_bounding_circle(100, 100)
    return spike


# Initialize game variables


def hide_all(actors):
    for char in actors:
        char.hideturtle()
    return


def start_game_fr():
    pen.goto(600, 170)
    pen.write("0", move=False, align="center", font=("Courier", 25, "normal"))
    player = spawn_player()
    snail = spawn_snail()
    coins = spawn_coins()
    goal = spawn_goal()
    spike = spawn_spike()
    actors = [player, snail, coins, goal, spike]
    player.score = 0

    while running:
        # Update the screen

        pen.clear()
        start_message.clear()
        wn.tracer(1, 1)

    # Add gravity
        gravity = -0.9
        player.dy += gravity

        # Move player (jump)
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
        wn.onkeypress(player.jump, "space")

    # Bottom Border
        if player.ycor() < GROUND_LEVEL + 50:
            player.dy = 0
            player.sety(GROUND_LEVEL + 50)

        # Top Border
        if player.ycor() > GROUND_LEVEL + 200:
            player.dy = 0
            player.sety(GROUND_LEVEL + 200)

        # Move Pipe 1
        if not coins.destroyed:
            coins.setx(coins.xcor() + coins.dx)
        # Move goal
        goal.setx(goal.xcor()+goal.dx)

        spike.setx(spike.xcor() + spike.dx)

        # Check for score
        player.score += 1
        pen.clear()
        pen.goto(600, 170)
        pen.write(player.score, move=False, align="center",
                  font=("Arial", 25, "normal"))

        if player.collisions(coins) and not coins.destroyed:
            player.ready = True
            coins.destroy_actor()
            player.score += 100

        if player.collisions(spike):
            time.sleep(0.1)
            end_screen(actors, False)
            break

            # highscore pen.write(player.score, move=False, align="center", font=("Arial", 70, "normal")) !!!

            # collision with goal = win
        if player.collisions(goal):
            time.sleep(0.4)
            end_screen(actors, True)
            break


def end_screen(actors, win):
    global running
    running = False
    time.sleep(0.2)
    hide_all(actors)
    pen.penup()
    pen.goto(0, 0)
    screen.listen()
    if win:
        wn.bgpic("amongus.png")
    else:
        wn.bgpic("scarysnail.png")
    screen.onkeypress(start_game, 'space')


while not running:
    screen = Screen()
    start_message = turtle.Turtle()
    start_message.hideturtle()
    start_message.penup()
    start_message.sety(160)
    start_message.write("Press SPACE to start and jump",
                        align="center", font=("Courier", 20, "bold"))

    screen.onkeypress(start_game, 'space')
    screen.listen()

wn.mainloop()
