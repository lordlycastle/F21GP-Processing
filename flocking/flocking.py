from __future__ import division
from physics_object import PhysicsObject
from vector3 import Vector3

class Boid(object):

    def __init__(self, 
                     max_velocity=25, 
                         radius=50, 
                             distance=10, 
                                 theta=0.3,
                                     max_force=5):
        self.physics = PhysicsObject()
        self.max_velocity = max_velocity
        self.radius = radius
        self.wandertheta = Vector3()
        self.flocking = False
        self.distance = distance
        self.delta = theta
        self.radius = radius
        self.physics.velocity = Vector3(3, 3,0)
        # self.physics.velocity = Vector3(random(1) * self.max_velocity,
        #                                 random(1) * self.max_velocity,
        #                                 random(1) * self.max_velocity)
        self.steering_foce = 0
        self.desired_velocity = 0
        self.max_force = max_force

    def update(self, time_step, seek=Vector3(1,1,1)):
        # self.wander()
        self.arrive(seek)
        self.physics.update(time_step)

        self.draw_shape(self.radius)

    def wander(self):
        # Circle approach... not working
        # circle_center = self.physics.velocity.direction * distance
        # circle_Center += self.physics.position
        # displacement = Vector3(1, 1, 1) * radius
        # self.wandertheta += random(-delta, delta)

        # wander_force = circle_center + displacement

        # circle_center = self.physics.velocity.direction * distance
        # displacement = Vector3(1, 1, 1) * radius
        # self.wandertheta.x += randomGaussian() * delta
        # displacement.x = cos(self.wandertheta.x)
        # displacement.y = sin(self.wandertheta.x)
        # self.wandertheta.z += randomGaussian() * delta
        # displacement.z = cos(self.wandertheata.z)
        # displacement.y += sing(self.wanderthata.z)

        # Just random functions
        wander_force = Vector3(random(-self.delta, self.delta),
                               random(-self.delta, self.delta),
                               random(-self.delta, self.delta))

        new_velocity = (self.physics.velocity.direction + wander_force).direction
        new_velocity = new_velocity * self.distance
        self.physics.velocity = new_velocity
        
        
    def seek(self, target):
        desired_velocity = target - self.physics.position
        desired_velocity = desired_velocity.direction * self.max_velocity
        
        steer = desired_velocity - self.physics.velocity
        if steer.magnitude > self.max_force:
            steer = steer.direction * self.max_force
        
        self.physics.apply_force(steer)
        
    def arrive(self, target):
        desired_velocity = target - self.physics.position
        
        if desired_velocity.magnitude < 100:
            desired_velocity = desired_velocity.direction * \
                                (desired_velocity.magnitude/100*self.max_velocity)
        else:
            desired_velocity = desired_velocity.direction * self.max_velocity
        
        steer = desired_velocity - self.physics.velocity
        if steer.magnitude > self.max_force:
            steer = steer.direction * self.max_force
        
        self.physics.apply_force(steer)
        
    def draw_shape(self,r=5):
        fill(255)
        # stroke(255)
        noStroke()

        pushMatrix()
        translate(self.physics.position.x,
                  self.physics.position.y,
                  self.physics.position.z)
        
        # direction = self.physics.velocity.direction
        # facing = direction - Vector3(0, 0, -1)
        
        # x = atan2(self.physics.velocity.y, self.physics.velocity.z)
        # y = atan2(self.physics.velocity.x * cos(x), self.physics.velocity.z) +PI
        # z = atan2(cos(x), sin(x) * sin(y))
        # # print(x,y,z)
        # rotateX(x)
        # rotateY(y)
        # rotateZ(z)
        
        # v = direction.cross(facing)
        # s = direction.dot(facing) / (direction.magnitude * facing.magnitude)
        # thetha = acos(s)
        

        # beginShape(TRIANGLE_FAN)
        # # Base of the pyramid
        # vertex(0, 0, 0)
        # vertex(0, -r * 2, 0)
        # vertex(-r * 2, -r * 2, 0)
        # vertex(-r * 2, 0, 0)

        # # 4 Sides of the pyramid
        # # See how the bottom two are a combination of the base
        # vertex(-r, -r, -r * 3)
        # vertex(0, 0, 0)
        # vertex(0, -r * 2, 0)

        # vertex(-r, -r, -r * 3)
        # vertex(0, -r * 2, 0)
        # vertex(-r * 2, -r * 2, 0)

        # vertex(-r, -r, -r * 3)
        # vertex(-r * 2, -r * 2, 0)
        # vertex(-r * 2, 0, 0)

        # vertex(-r, -r, -r * 3)
        # vertex(-r * 2, 0, 0)
        # vertex(0, 0, 0)
        # endShape()
        
        sphere(3)

        popMatrix()
