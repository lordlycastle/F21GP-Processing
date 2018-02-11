from __future__ import division
import math
# from ball import Ball, Cube
from vector3 import Vector3
from particle_emitter import ParticleEmitter, PhysicsParticle, ParticleExplosion
add_library('peasycam')

emitter = ParticleEmitter(num_of_particles=200,
                          position=Vector3(),
                          lifetime=5)

explosion = ParticleExplosion(position=Vector3(),
                              lifetime=5,
                              steps=36,
                              velocity_factor=100,
                              acceleration=Vector3(0, 100, 0))

explosions = [explosion]

fps = 24
time_step = 1 / fps


def setup():
    size(720, 480, P3D)
    frameRate(fps)
    lights()
    background(0)
    cam = PeasyCam(this, 400)
    cam.setWheelScale(0.1)
    cam.setYawRotationMode()
    

seed = 0
def draw():
    global seed, explosions
    background(0)
    ambientLight(205, 205, 205)
    directionalLight(126, 126, 126, 0, 0, -1)

    emitter.update(time_step)
    # randomSeed(seed)
    seed += 1
    # x, y = 0, 0
    emitter.velocity.x = random(sin(radians(seed)) * -100, -50)
    emitter.velocity.z = random(cos(radians(seed)) * -100, -50)
    # print(len(emitter.particles))

    # explosion.update(time_step)
    # print(len(explosion.directions))
    for explosion in explosions:
        if len(explosion.particles) == 0:
            explosions.remove(explosion)
        else:
            explosion.update(time_step)


def keyPressed():

    if key == 'e':
        explode()

def explode():
    explosion = ParticleExplosion(position=Vector3(random(-width / 2, width / 2),
                                                   random(-height / 2,
                                                          height / 2),
                                                   random(-50, 50)),
                                  lifetime=5,
                                  steps=int(random(10, 40)),
                                  velocity_factor=random(100, 300),
                                  acceleration=Vector3(0, random(0, 200), 0))
    explosions.append(explosion)