from __future__ import division
from physics_object import PhysicsObject
from vector3 import Vector3

class Boid(object):
    """Individual agent class. Create multiple for fun times.
    Note: I wouldn't trust this code too much.
    """
    def __init__(self,
                 max_velocity=25,
                 radius=50,
                 distance=10,  # Controls how much random velocity is added when in a flock
                 theta=0.3,
                 max_force=5,
                 seperation_distance=500,
                 starting_velocity_factor=0.5):
        self.physics = PhysicsObject()
        self.max_velocity = max_velocity
        self.radius = radius
        self.wandertheta = Vector3()
        self.flocking = False
        self.distance = distance
        self.delta = theta
        self.radius = radius
        # self.physics.velocity = Vector3(3, 3, 0)
        self.starting_velocity_factor = starting_velocity_factor
        self.physics.velocity = Vector3(random(-starting_velocity_factor,
                                               starting_velocity_factor) * self.max_velocity,
                                        random(-starting_velocity_factor,
                                               starting_velocity_factor) * self.max_velocity,
                                        random(-starting_velocity_factor,
                                               starting_velocity_factor) * self.max_velocity)
        self.steering_foce = 0
        self.desired_velocity = 0
        self.max_force = max_force
        self.seperation_distance = seperation_distance
        self.align_weight = self.max_velocity
        self.cohere_weight = self.max_velocity*self.starting_velocity_factor*2
        self.separate_weight = self.max_velocity * self.starting_velocity_factor
        self.color = color(random(255), random(255), random(255))

    def update(self, time_step, boids, seek=Vector3(1, 1, 1)):
        # self.wander()
        # self.seek(seek)
        neighbour_boids = []
        count = 0
        for boid in boids:
            if boid is not self:
                if (boid.physics.position - self.physics.position).magnitude > self.seperation_distance:
                    count += 1
                    neighbour_boids.append(boid)

        alignment = Vector3()
        cohesion = Vector3()
        separation = Vector3()
        if count > 0:
            alignment = self.get_alignment(neighbour_boids,
                                           distance=self.seperation_distance,
                                           count=count)
            cohesion = self.get_cohesion(neighbour_boids,
                                         distance=self.seperation_distance,
                                         count=count)
            separation = self.get_separation(neighbour_boids,
                                             distance=self.seperation_distance,
                                             count=count)

        velocity = self.physics.velocity
        

        velocity += self.align_weight * alignment + \
            self.cohere_weight * cohesion + \
            self.separate_weight * separation
        if velocity.magnitude > self.max_velocity:
            velocity = velocity.direction * self.max_velocity*0.6
        self.physics.velocity = velocity
        # print(separation)

        self.physics.velocity += Vector3(random(-self.distance, self.distance),
                                        random(-self.distance, self.distance),
                                        random(-self.distance, self.distance))
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

        new_velocity = (
            self.physics.velocity.direction + wander_force).direction
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
                (desired_velocity.magnitude / 100 * self.max_velocity)
        else:
            desired_velocity = desired_velocity.direction * self.max_velocity

        steer = desired_velocity - self.physics.velocity
        if steer.magnitude > self.max_force:
            steer = steer.direction * self.max_force
        # print('Steer' + str(steer))
        self.physics.apply_force(steer)

    def get_alignment(self, boids, distance=100, count=1):
        align = Vector3()
        for boid in boids:
            align += boid.physics.velocity

        align = align / count
        return align.direction

    def get_cohesion(self, boids, distance=100, count=1):
        cohere = Vector3()
        for boid in boids:
            cohere += boid.physics.velocity

        cohere = cohere / count
        cohere = cohere - self.physics.position
        return cohere.direction

    def get_separation(self, boids, distance=100, count=1):
        seperate = Vector3()
        for boid in boids:
            seperate += (boid.physics.position - self.physics.position)

        seperate = seperate / count
        seperate = seperate * -1
        return seperate.direction

    def draw_shape(self, r=5):
        fill(self.color)
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
        # print(x,y,z)
        # rotateX(x)
        # rotateY(y)
        # rotateZ(z)

        # v = direction.cross(facing)
        # s = direction.dot(facing) / (direction.magnitude * facing.magnitude)
        # thetha = acos(s)

        # beginShape(TRIANGLE_FAN)
        # Base of the pyramid
        # vertex(0, 0, 0)
        # vertex(0, -r * 2, 0)
        # vertex(-r * 2, -r * 2, 0)
        # vertex(-r * 2, 0, 0)

        # 4 Sides of the pyramid
        # See how the bottom two are a combination of the base
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

        sphere(2)

        popMatrix()