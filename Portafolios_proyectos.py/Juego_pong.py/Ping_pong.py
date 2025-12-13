'''Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para 
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los 
jugadores.También puedes definir una serie de asignaciones de teclas para establecer los 
controles del usuario para las paletas de los jugadores izquierda y derecha. '''

# Código base para la creación del juego Pong, estructurado y comentado en español.
# Edificación de un juego Pong simple usando el módulo turtle en Python.

import turtle
import os
import random

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Pong por raionhato")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Marcadores
score_a = 0
score_b = 0
high_score = 0
try:
    with open("high_score.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = 0

# Paleta A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paleta B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 * random.choice([-1, 1])
ball.dy = 0.2 * random.choice([-1, 1])
ball_speed_increment = 0.01
max_ball_speed = 0.5
ball_speed = 0.2
def reset_ball():
    global ball_speed
    ball.goto(0, 0)
    ball.dx = ball_speed * random.choice([-1, 1])
    ball.dy = ball_speed * random.choice([-1, 1])
    ball_speed = 0.2
reset_ball()

# Lápiz para el marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0  Jugador B: 0  Máximo: 0", align="center", font=("Courier", 24, "normal"))

# Funciones
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
    paddle_b.sety(y)

# Asignar teclas
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Bucle principal del juego
while True:
    wn.update()
    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Colisiones con los bordes
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        score_a += 1
        if score_a > high_score:
            high_score = score_a
        pen.clear()
        pen.write(f"Jugador A: {score_a}  Jugador B: {score_b}  Máximo: {high_score}", align="center", font=("Courier", 24, "normal"))
        reset_ball()
    if ball.xcor() < -390:
        score_b += 1
        if score_b > high_score:
            high_score = score_b
        pen.clear()
        pen.write(f"Jugador A: {score_a}  Jugador B: {score_b}  Máximo: {high_score}", align="center", font=("Courier", 24, "normal"))
        reset_ball()

    # Colisiones con las paletas
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        if abs(ball.dx) < max_ball_speed:
            ball.dx += ball_speed_increment * (1 if ball.dx > 0 else -1)
            ball.dy += ball_speed_increment * (1 if ball.dy > 0 else -1)
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        if abs(ball.dx) < max_ball_speed:
            ball.dx += ball_speed_increment * (1 if ball.dx > 0 else -1)
            ball.dy += ball_speed_increment * (1 if ball.dy > 0 else -1)

# Guardar el récord al salir
try:
    with open("high_score.txt", "w") as f:
        f.write(str(high_score))
except:
    pass

wn.mainloop()
