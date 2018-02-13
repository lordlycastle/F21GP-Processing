from __future__ import division
import math
from ball import Ball, Cube
from vector3 import Vector3
from physics_object import PhysicsObject
from flocking import Boid
add_library('peasycam')


height_ = 720
width_ = 480
fps = 30
time_step = 1 / fps
wrap_stage = False

boid = Boid(max_velocity=100, radius=5, distance=10, theta=1, max_force=100)
boids = [boid]

random_spawn_points = False
starting_velocity_factor = 0.3
for _ in range(100):
    b = Boid(max_velocity=100, 
             radius=5, 
             distance=10, 
             theta=1, 
             max_force=300, 
             starting_velocity_factor=starting_velocity_factor)
    if random_spawn_points:
        b.physics.position = Vector3(random(-1, 1) * width_/2,
                                     random(-1, 1) * height_/2,
                                     random(-1, 1) * width_/2)
    boids.append(b)


def setup():
    global ball, height_, width_
    size(height_, width_, P3D)
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
    
    for boid in boids:
        if wrap_stage:
            if abs(boid.physics.position.x) > width/2:
                boid.physics.position.x = -boid.physics.position.x
            if abs(boid.physics.position.z) > width/2:
                boid.physics.position.z = -boid.physics.position.z
            if abs(boid.physics.position.y) > height/2:
                boid.physics.position.y = -boid.physics.position.y
        boid.update(time_step,
                    boids=boids,
                    seek=Vector3(1,1,1)
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


























