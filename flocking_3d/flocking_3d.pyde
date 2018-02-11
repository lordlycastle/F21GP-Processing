from __future__ import division
import math
from ball import Ball, Cube
from vector3 import Vector3
add_library('peasycam')



fps = 30
time_step = 1 / fps

def setup():
    global ball
    size(720, 480, P3D)
    frameRate(fps)
    lights()
    background(0)
    cam = PeasyCam(this, 400)
    cam.setWheelScale(0.1)
    cam.setYawRotationMode()


def draw():
    background(0)
    ambientLight(205, 205, 205)
    directionalLight(126, 126, 126, 0, 0, -1)

    show_stage()



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