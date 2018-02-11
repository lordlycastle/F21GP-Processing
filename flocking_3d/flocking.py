from __future__ import division
from physics_object import PhysicsObject


class Boid(object):
    def __init__(self, max_velocity=25, radius=5):
        self.physics = PhysicsObject()
        self.max_velocity = max_velocity
        self.radius = radius
        self.wandertheta = 0
        
    def update(self, time_step):
        self.physics.update(time_step)
        
        self.draw_shape(self.radius)
        
        
    def wander(self, radius=50, distance=85, delta=0.3):
        circle_center = self.physics.velocity.direction * distance
        # circle_Center += self.physics.position
        displacement = Vector3(1, 1, 1) * radius
        self.wandertheta += random(-delta, delta)
        
        wander_force = circle_center + displacement
        
        
        
    def draw_shape(r=5):
        fill(200, 100)
        stroke(255)
        
        pushMatrix()
        translate(0, 0, 0)
        rotate(0)
        
        beginShape(TRIANGLE_FAN)
        vertex(0, 0, 0)
        vertex(0, -r*2, 0)
        vertex(-r*2, -r*2, 0)
        vertex(-r*2, 0, 0)
        
        vertex(-r, -r, r*3)
        vertex(0, 0, 0)
        vertex(0, -r*2, 0)
        
        vertex(-r, -r,r*3)
        vertex(0, -r*2, 0)
        vertex(-r*2, -r*2, 0)
        
        vertex(-r, -r,r*3)
        vertex(-r*2, -r*2, 0)
        vertex(-r*2, 0, 0)
        endShape();
        
        popMatrix();

