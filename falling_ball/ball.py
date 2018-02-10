

from vector3 import Vector3
from physics_object import PhysicsObject


class Ball(object):

    def __init__(self, radius, position):
        self.radius = radius
        self.physics = PhysicsObject()
        self.physics.position = position
        
    def update(self, time_step):
        self.update_physics(time_step)
        self.display()
        
    def update_physics(self, time_step):
        self.physics.update(time_step)
        
    def display(self):
        pushMatrix()
        noStroke()
        fill(204, 102, 0)
        translate(self.physics.position.x, 
                  self.physics.position.y, 
                  self.physics.position.z)
        
        sphere(int(self.radius))
        popMatrix()


class Cube(object):

    def __init__(self, size, position):
        self.size = size
        self.physics = PhysicsObject()
        self.physics.position = position
        
    def update(self, time_step):
        self.update_physics(time_step)
        self.display()
        
    def update_physics(self, time_step):
        self.physics.update(time_step)
        
    def display(self):
        pushMatrix()
        noStroke()
        fill(0, 102, 200)
        translate(self.physics.position.x, 
                  self.physics.position.y, 
                  self.physics.position.z)
        rotateX(radians(self.physics.rotation.x))
        rotateY(radians(self.physics.rotation.y))
        rotateZ(radians(self.physics.rotation.z))
        box(int(self.size))
        popMatrix()