#!/usr/bin/env pybricks-micropython

from evicka import *

global switch
switch = 0

recal()
brick.sound.beep(1500, 500, 100)

while(1):
    if(Button.UP in brick.buttons()):
        switch = 1
    if(Button.LEFT in brick.buttons()):
        switch = 2
    if(Button.DOWN in brick.buttons()):
        switch = 3
    if(Button.RIGHT in brick.buttons()):
        switch = 4

    if(switch == 1):
        reset()
        recal()
        rot(130, -14)
        fd(300, 2726)
        rot(120, -10)
        fd(280, 1820)
        bw(120, 700)
        rot(120, -100)
        fd(250, 470)
        claw(350, 150)
        bw(120, 500)
        claw(350, -150)
        rot(120, -60)
        fd(450, 4620, False)

    if(switch == 2):
        reset()
        stick(500, 480)
        rot(120, -38)
        fd(200, 2200)
        stick(500, -260)
        bw(100, 1060)
        stick(300, 340)
        rot(120, -49)
        fd(250, 960)
        stick(300, -530)
        bw(200, 240)
        rot(120, -22)
        fd(250, 260)
        stick(300, 220)
        wait(1000)
        bw(250, 1000)
        rot(120, 90)
        bw(320, 2500, False)


    if(switch == 3):
        reset()
        rot(150, -18)
        fd(250, 2250)
        bw(220, 380)
        rot(120, 40)
        fd(250, 780)
        rot(120, -50)
        fd(220, 1405)
        rot(120, 22)
        fd(220, 420)
        rot(120, 100)
        fd(250, 490)
        rot(120, -90)
        bw(220, 1400)
        rot(100, -8)
        bw(350, 3000, False)

    if(switch == 4):
        lfd(220, (Color.BROWN or Color.GREEN))

    switch = 0
