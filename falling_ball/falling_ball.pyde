from __future__ import division
import math
from ball import Ball, Cube
from vector3 import Vector3
add_library('peasycam')

gravity = Vector3(0, 50, 0)
apply_gravity = True

ball = Ball(radius=25, position=Vector3())
ball.physics.acceleration = gravity
ball.physics.velocity = Vector3(5, 100, -10)
cube = Cube()

balls = [ball]

fps = 60
time_step = 1 / fps

def setup():
    global ball
    size(720, 480, P3D)
    frameRate(fps)
    lights()
    background(0)
    cam = PeasyCam(this, 400)
    cam.setWheelScale(0.1)
    # cam.setYawRotationMode()

    ball.limit_x = width / 2
    ball.limit_y = height / 2
    ball.limit_z = width / 2
    cube.x = width
    cube.y = height
    cube.z = width


def draw():
    background(0)
    ambientLight(205, 205, 205)
    directionalLight(126, 126, 126, 0, 0, -1)
    
    for ball in balls:
        ball.update(time_step)

    cube.update(time_step)

alternate = 1
def keyPressed():
    global alternate
    if key == 'u':
        ball.physics.apply_acceleration(Vector3(0, -20, 0), 1)

    if key == 'r':
        ball.physics.position = Vector3(0, 0, 0)

    if key == 'a':
        add_ball()
        alternate = -alternate


def add_ball():
    global gravity, apply_gravity
    ball = Ball(radius=random(10, 30),
                position=Vector3(random(-width / 2+100, width / 2-100),
                                 random(-height / 2+100, height / 2-100),
                                 random(-width / 2+100, width / 2-100)),
                limit_x=width / 2,
                limit_y=height / 2,
                limit_z=width / 2)
    ball.physics.velocity = Vector3(random(50, 150) * alternate,
                                    random(-200, 200) * alternate,
                                    random(-150, -50) * alternate)
    if apply_gravity:
        ball.acceleration = Vector3(0, 50, 0)
    balls.append(ball)
    