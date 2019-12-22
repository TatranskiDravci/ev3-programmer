import math
import pyglet
from pyglet.window import key
from pyglet.window import mouse
from config import *

def pxtocm(px):
    return float(px * cmppx)

def cmtopx(cm):
    return float(cm * pxpcm)

pyglet.gl.glLineWidth(8)
window = pyglet.window.Window(win_x, win_y)
mat = pyglet.resource.image(fll_mat)
rpos = [cmtopx(robot_start_pos[0] + robot_gyro_pos[0]), cmtopx(robot_start_pos[1] + robot_gyro_pos[1])]
rangle = robot_start_ang
rsize = [cmtopx(robot_size[0]), cmtopx(robot_size[1]), cmtopx(robot_size[2])]

@window.event
def on_mouse_press(x, y, button, modifiers):
    Δx = abs(x - rpos[0])
    Δy = abs(y - rpos[1])
    l = math.sqrt((Δx**2) + (Δy**2))
    
    if(rpos[0] == 0):
        ix = 2
    else:
        ix = 2 * rpos[0]
    if(rangle == 0):
        iy = rpos[1]
    else:
        iy = math.sin(rangle) * (ix/math.cos(rangle))

    angle = math.degrees(
                        math.acos(
                                ((ix-rpos[0])*(x-rpos[0]) + (iy-rpos[1])*(y-rpos[1])) /
                                ((math.sqrt(((rpos[0]-ix)**2) + ((rpos[1]-iy)**2))) * 
                                (math.sqrt(((x-rpos[0])**2) + ((y-rpos[1])**2))))  
                        )
                    )

    print("angle: ", angle)
    print("distance: ", pxtocm(l))

@window.event
def on_draw():
    window.clear()
    mat.blit(0,0)

pyglet.app.run()  