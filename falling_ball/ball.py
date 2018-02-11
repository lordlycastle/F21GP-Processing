

from vector3 import Vector3
from physics_object import PhysicsObject


class Ball(object):

    def __init__(self, radius, position, limit_x=300, limit_y=300, limit_z=300):
        self.radius = radius
        self.physics = PhysicsObject()
        self.physics.position = position
        self.limit_x = limit_x
        self.limit_y = limit_y
        self.limit_z = limit_z
        self.color = color(random(255), random(255), random(255))

    def update(self, time_step):
        self.update_physics(time_step)
        self.check_collisions()
        self.display()

    def update_physics(self, time_step):
        self.physics.update(time_step)

    def display(self):
        pushMatrix()
        noStroke()
        fill(self.color)
        translate(self.physics.position.x,
                  self.physics.position.y,
                  self.physics.position.z)

        sphere(int(self.radius))
        popMatrix()

    def check_collisions(self):
        # Reflect X
        if self.physics.position.x + self.radius > self.limit_x or \
           self.physics.position.x - self.radius < -self.limit_x:
            self.physics.velocity.x = -self.physics.velocity.x
        
        # Reflect y
        if self.physics.position.y+self.radius > self.limit_y or \
           self.physics.position.y-self.radius < -self.limit_y:
            self.physics.velocity.y = -self.physics.velocity.y
            
        # Reflect X
        if self.physics.position.z+self.radius > self.limit_z or \
           self.physics.position.z-self.radius < -self.limit_z:
            self.physics.velocity.z = -self.physics.velocity.z


class Cube(object):

    def __init__(self, size=50, position=Vector3(), ):
        self.size = size
        self.physics = PhysicsObject()
        self.physics.position = position
        self.x = self.size 
        self.y = self.size
        self.z = self.size

    def update(self, time_step):
        self.update_physics(time_step)
        self.display()

    def update_physics(self, time_step):
        self.physics.update(time_step)

    def display(self):
        pushMatrix()
        # noStroke()
        stroke(255)
        # fill(0, 102, 200)
        noFill()
        translate(self.physics.position.x,
                  self.physics.position.y,
                  self.physics.position.z)
        rotateX(radians(self.physics.rotation.x))
        rotateY(radians(self.physics.rotation.y))
        rotateZ(radians(self.physics.rotation.z))
        box(int(self.x), int(self.y), int(self.z))
        popMatrix()
