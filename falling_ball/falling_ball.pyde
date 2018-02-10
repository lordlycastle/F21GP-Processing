from __future__ import division
import math
from ball import Ball, Cube
from vector3 import Vector3
add_library('peasycam')


ball = Ball(radius=50, position=Vector3())
ball.physics.acceleration = Vector3(0, 9.81, 0)
cube = Cube(size=50, position=Vector3(-250, 0, 0))


fps = 24
time_step = 1/fps

def setup():
    size(720, 480, P3D)
    frameRate(fps)
    lights()
    background(0)
    cam = PeasyCam(this, 400)
    cam.setWheelScale(0.1)
    cam.setYawRotationMode()
    # Vector3._test_class()
    
    
def draw():
    background(0)
    ambientLight(205, 205, 205)
    directionalLight(126, 126, 126, 0, 0, -1)
    
    ball.update(time_step)
    if ball.physics.position.y > height/2:
        ball.physics.position.y = -height/2
        
    cube.physics.rotation.y += 1
    cube.update(time_step)
    
def keyPressed():
    if key == 'u':
        ball.physics.apply_acceleration(Vector3(0, -20, 0), 1)
    
    if key == 'r':
        ball.physics.position = Vector3(0, -height/2, 0)
                
