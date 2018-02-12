from __future__ import division
import math
from ball import Ball, Cube
from vector3 import Vector3
from physics_object import PhysicsObject
from flocking import Boid
add_library('peasycam')



fps = 30
time_step = 1 / fps

boid = Boid(max_velocity=50, radius=5, distance=10, theta=1, max_force=100)
boids = [boid]


def setup():
    global ball
    size(720, 480, P3D)
    frameRate(fps)
    lights()
    background(0)
    cam = PeasyCam(this, 400)
    cam.setWheelScale(0.1)
    # cam.setYawRotationMode()
    sphereDetail(5)


def draw():
    global time_step, boids
    background(0)
    ambientLight(255, 255, 255)
    # directionalLight(255, 255, 255, 0, 0, -1)
    # directionalLight(255, 255, 255, 0, -1, 0)
    # directionalLight(255, 255, 255, -1, 0, 0)

    show_stage()
    r=50
    for boid in boids:
        boid.update(time_step, 
                    seek=Vector3(width/2, height/2, width/2)
                    )
        
        


def keyPressed():
    pass


def show_stage():
    pushMatrix()
    # noStroke()
    stroke(255)
    # fill(0, 102, 200)
    noFill()
    translate(0, 0, 0)
    box(width, height, width)
    popMatrix()



























