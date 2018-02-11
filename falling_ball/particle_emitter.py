from vector3 import Vector3
from physice_object import PhysicsObject

class ParticleEmitter(object):
    
    def __init__(self, num_of_particles, position, lifetime):
        self.num_of_particles = num_of_particles
        self.position = position
        self.particles = [PhysicsParticle() for _ in range(num_of_particles)]
        
           
   def update(self, time_step):
       for particle in self.particles:
           particle.update(time_step) 
    
    
    
class PhysicsParticle(PhysicsObject):
    
    def __init__(self, lifetime):
        super.__init__()
        self.lifetime = lifetime
        
    @property
    def alive(self):
        return lifetime > 0
    