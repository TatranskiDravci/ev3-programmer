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
r = [cmtopx(robot_start_pos[0]), cmtopx(robot_start_pos[1])]
rra = robot_start_ang
rsize = [cmtopx(robot_size[0]), cmtopx(robot_size[1]), cmtopx(robot_size[2])]

@window.event
def on_mouse_press(x, y, button, modifiers):
    Δx = abs(x - r[0])
    Δy = abs(y - r[1])
    l = math.sqrt((Δx**2) + (Δy**2))
    
    if(r[0] == 0):
        ix = 2
    else:
        ix = 2 * r[0]
    if(rra == 0):
        iy = r[1]
    else:
        iy = math.sin(rra) * (ix/math.cos(rra))

    ang = math.degrees(
                        math.acos(
                                ((ix-r[0])*(x-r[0]) + (iy-r[1])*(y-r[1])) /
                                ((math.sqrt(((r[0]-ix)**2) + ((r[1]-iy)**2))) * 
                                (math.sqrt(((x-r[0])**2) + ((y-r[1])**2))))  
                        )
                    )

    print("angle: ", ang)
    print("distance: ", pxtocm(l))

@window.event
def on_draw():
    window.clear()
    mat.blit(0,0)

pyglet.app.run()  