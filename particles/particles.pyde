from __future__ import division
import math
from ball import Ball, Cube
from vector3 import Vector3
from particle_emitter import ParticleEmitter, PhysicsParticle
add_library('peasycam')


cube = Cube(size=50, position=Vector3(-250, 0, 0))

emitter = ParticleEmitter(num_of_particles=200,
                          position=Vector3(),
                          lifetime=5)

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
        
    cube.physics.rotation.y += 1
    cube.update(time_step)
    
    emitter.update(time_step)
    # print(len(emitter.particles))
    
def keyPressed():
    
    if key == 'r':
        return
                
