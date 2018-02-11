from __future__ import division
from vector3 import Vector3
from physics_object import PhysicsObject

class ParticleEmitter(object):

    def __init__(self,
                 num_of_particles,
                 position,
                 lifetime,
                 velocity=Vector3(0, -100, 0),
                 acceleration=Vector3(0, 50, 0),
                 x_angle=100,
                 z_angle=100,
                 spawn_rate=5):
        self.num_of_particles = num_of_particles
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.x_angle = x_angle
        self.z_angle = z_angle
        self.lifetime = lifetime
        self.spawn_rate = spawn_rate

        self.particles = []
        for _ in range(num_of_particles):
            particle = PhysicsParticle(lifetime,
                                       velocity=velocity,
                                       acceleration=acceleration,
                                       x_angle=x_angle,
                                       z_angle=z_angle,
                                       position=position)
            self.particles.append(particle)

    def update(self, time_step):
        sphereDetail(5)
        for particle in self.particles:
            particle.update(time_step)
            if not particle.alive:
                self.particles.remove(particle)

        for _ in range(self.spawn_rate):
            particle = PhysicsParticle(self.lifetime,
                                       velocity=self.velocity,
                                       acceleration=self.acceleration,
                                       x_angle=self.x_angle,
                                       z_angle=self.z_angle,
                                       position=self.position)
            self.particles.append(particle)
        sphereDetail(30)


class ParticleExplosion(object):

    def __init__(self,
                 position,
                 lifetime,
                 velocity_factor=50,
                 acceleration=Vector3(0, 50, 0),
                 x_angle=100,
                 z_angle=100,
                 spawn_rate=5,
                 steps=20):
        self.position = position
        self.velocity_factor = velocity_factor
        self.acceleration = acceleration
        self.x_angle = x_angle
        self.z_angle = z_angle
        self.lifetime = lifetime
        self.spawn_rate = spawn_rate
        self.steps = steps

        self.directions = ParticleExplosion.get_explosion_directions(steps)
        self.particles = []
        for direction in self.directions:
            particle = PhysicsParticle(lifetime, 
                                       add_noise=False, 
                                       acceleration=acceleration)
            particle.velocity = direction*random(velocity_factor/2, velocity_factor)
            particle.position = self.position
            self.particles.append(particle)
            
    def update(self, time_step):
        sphereDetail(5)
        for particle in self.particles:
            particle.update(time_step)
            if not particle.alive:
                self.particles.remove(particle)
                
        sphereDetail(30)

    @staticmethod
    def get_explosion_directions(steps=10):
        """Find the direction particles will have
        using equation of a sphere. The particles 
        will move outwards from center.
        steps: number of particles around the 
        circumfrenece

        sphere => x^2 + y^2 + z^2 = R
        """
        directions = []
        y_step = 2 / steps
        for i in range(1, steps):
            y = y_step * i - 1
            r = 1 - y * y
            thetha_step = 360 / steps
            for j in range(steps):
                x = cos(radians(thetha_step * j)) * r
                z = sin(radians(thetha_step * j)) * r
                directions.append(Vector3(x, y, z))
        # We dont' want multiple particles on the top and bottom
        directions.append(Vector3(0, 1, 0))
        directions.append(Vector3(0, -1, 0))
        return directions


class PhysicsParticle(PhysicsObject):

    def __init__(self,
                 lifetime,
                 velocity=Vector3(),
                 acceleration=Vector3(),
                 position=Vector3(),
                 x_angle=100,
                 z_angle=100,
                 add_noise=True,
                     radius=3):
        super(PhysicsParticle, self).__init__()
        self.lifetime = lifetime
        self.time_remaining = lifetime
        self.velocity = velocity
        self.acceleration = acceleration
        self.x_angle = x_angle
        self.z_angle = z_angle
        self.radius = radius
        self.color = color(random(255), random(255), random(255))
        if add_noise:
            self.add_noise()

    def add_noise(self):
        axis = [0, 0, 0]
        limit_angles = [self.x_angle, self.velocity.y / 2, self.z_angle]
        for i in range(3):
            seed = random(1)
            r = noise(seed)
            axis[i] = limit_angles[i] * r - limit_angles[i] / 2

        self.velocity = Vector3(axis[0], axis[1], axis[2]) + self.velocity
        acceleration_limit = 10
        self.acceleration = self.acceleration + \
            Vector3(random(-acceleration_limit, acceleration_limit),
                    random(-acceleration_limit, acceleration_limit),
                    random(-acceleration_limit, acceleration_limit))

    @property
    def alive(self):
        return self.time_remaining > 0

    def update(self, time_step):
        super(PhysicsParticle, self).update(time_step)
        self.time_remaining -= time_step
        self.display()

    def display(self):
        pushMatrix()
        noStroke()
        fill(self.color,
             self.time_remaining / self.lifetime * 255 if self.alive else 0)
        translate(self.position.x,
                  self.position.y,
                  self.position.z)
        sphere(self.radius)
        popMatrix()