
from vector3 import Vector3


class PhysicsObject(object):

    def __init__(self,
                 mass=1,
                 position=Vector3(),
                 velocity=Vector3(),
                 rotation=Vector3(),
                 acceleration=Vector3()):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.rotation = rotation
        self.acceleration = acceleration
        
    def update(self, time_step):
        newPosition = Vector3()
        newPosition = self.position + \
                      self.velocity*time_step + \
                      self.acceleration*time_step*time_step*0.5
        self.position = newPosition
        self.velocity = self.velocity + self.acceleration*time_step

    def apply_acceleration(self, acceleration, duration):
        self.velocity = self.velocity + acceleration*duration
        

