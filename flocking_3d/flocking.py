from __future__ import division



class Boid(object):
    def __init__(self):
        pass
        
        
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

