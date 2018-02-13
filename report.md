# Games Programming Report

### Bouncing Ball
The physics is calculated in `PhysicsObject` class which uses the _suvat_ equation to calculate position, velocity, and acceleration every update. The update frequency is set to match the frame rate. The `Ball` class has a `PhysicsObject` variable for keeping track of the physic properties of the ball. In the `update` function for `Ball` it calls the `PhysicsObject`'s update function first. After it has the new position, it calls `display` which draws a `Sphere` at the current position of the ball. 


### Particles System
The `ParticleEmitter` and `ParticleExplosion` classes keep track of `PhysicsParticle` objects. In every update both the classes loop over all the particles to call update in each. The `PhysicsParticle` class inherits all its physic behaviour from `PhysicsObject`. It updated in the same manner i.e. using _suvat_ equations. It also defined a `display` function which is called after it update the physics. The `display` function draws a low-poly sphere at the position calculated in physics update. The important distinction between 'PhysicsParticle' and 'Ball' is that the former has a lifetime. After which the particle is removed from the particle system and no longer updated. 

### Flocking
Flocking is accomplished by creating several `Boid` class objects in the scene. Similar to other classes the object has a physics update then a draw call. The physics update is done using the `PhysicsObject` class, except for the effects of separation, cohesion, and alignment. Those effects are calculated in `Boid` class with their own function and they change the `velcotiy` property of the `PhysicsObject` component. After all the physics calculation have been complete, a sphere is draw in the `PhysicsObjects`'s current position. 

### A* Search
A* search algorithm uses the movement costs to find path to target. It uses a modified Dijkstra's algorithm. Where Dijkstra only keeps track of movement cost so far i.e. cost to start, A* also records an estimated cost to destination. To explore next move options A* finds the F-cost, i.e. sum of movement cost to start and target, of all the neighbouring nodes. It then moves to the node with lowest F-cost and repeat the process until destination has been reached. 

The algorithm is visualised below. A random maze was generated where player can go on green blocks and not on red. The starting and end points are small blue circle and large purple circle, respectively. In this search the algorithm explored all the orange blocks to find a path and the pink blocks are the frontier blocks i.e. the list potential blocks that can be explored next; it will select the one with lowest F-cost as mentioned. The blue blocks show the path found found, note that diagonal movement is allowed. The algorithm did not have to explore all the blocks on the maze to find a path. This is an advantage of using A* over other algorithms such as Breadth First Search

![a-star-example](./a_star/a_star.png)