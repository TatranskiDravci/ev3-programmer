from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

# Definície

left = Motor(Port.B)
right = Motor(Port.C)
sLeft = Motor(Port.D)
sRight = Motor(Port.A)
gyro = GyroSensor(Port.S1)
color = ColorSensor(Port.S4)
gyro.reset_angle(0)
robot = DriveBase(left, right, 44, 180)
watch = StopWatch()

# Kalibrácia gyroskopu

def recal():
    gyro.speed()
    gyro.angle()
    time.sleep(1)

# Reset motorov a gyroskopu na 0 hodnotu

def reset():
    left.reset_angle(0)
    right.reset_angle(0)
    sLeft.reset_angle(0)
    sRight.reset_angle(0)
    gyro.reset_angle(0)

# Rotácia robota (na mieste)

def rot(spd=40, ang=0):
    b = 0
    while(True):
        if(gyro.angle() > ang and b == 0): 
            right.run(spd)
            left.run(spd * -1)
        if(gyro.angle() < ang and b == 0):
            left.run(spd)
            right.run(spd * -1)
        if(gyro.angle() > ang and b == 1): 
            right.run(40)
            left.run(-40)
        if(gyro.angle() < ang and b == 1):
            left.run(40)
            right.run(-40)
        if(gyro.angle() == ang):
            left.stop(Stop.HOLD)
            right.stop(Stop.HOLD)
            time.sleep(0.5)
            if(gyro.angle() == ang):
                gyro.reset_angle(0)
                break
            if(gyro.angle() != ang):
                b = 1

# Pohyb modul aktívna tyčka

def stick(spd=200, ang=0):
    sLeft.run_target(spd, ang * -1, Stop.BRAKE)
    sLeft.stop()
    sLeft.reset_angle(0)

# Pohyb zaklápacím modulom (čeluste)

def claw(spd=200, ang=0):
    sRight.run_target(spd, ang, Stop.BRAKE)
    sLeft.run_target(spd, ang * -1, Stop.BRAKE)
    sRight.stop()
    sLeft.stop()
    sLeft.reset_angle(0)
    sRight.reset_angle(0)

# Pohyb vpred

def fd(spd=40, ang=360, turn=True):
    while(1):
        if(((left.angle() + right.angle())/2) < ang and ((left.angle() + right.angle())/2) < (ang - 120)):
            robot.drive(spd, gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) < ang and ((left.angle() + right.angle())/2) >= (ang - 120)):
            if(((left.angle() + right.angle())/2) >= (ang - 60)):
                robot.drive(spd/2, gyro.angle() * -1)
            else:
                robot.drive(spd/(3/2), gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) >= ang):
            robot.stop(Stop.BRAKE)
            break
    robot.stop()
    if(turn == True):
        rot(60, 0)
    reset()
        
# Pohyb vzad

def bw(spd=40, ang=360, turn=True):
    while(1):
        if(((left.angle() + right.angle())/2) > -ang and ((left.angle() + right.angle())/2) > (-ang + 120)):
            robot.drive(-spd, gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) > -ang and ((left.angle() + right.angle())/2) <= (-ang + 120)):
            if(((left.angle() + right.angle())/2) <= (-ang + 60)):
                robot.drive((spd/2)*-1, gyro.angle() * -1)
            else:
                robot.drive((spd/(3/2))*-1, gyro.angle() * -1)
        if(((left.angle() + right.angle())/2) <= -ang):
            robot.stop(Stop.BRAKE)
            break
    robot.stop()
    if(turn == True):
        rot(60, 0)
    reset()


def lfd(spd=40, til=None):
    if(til != None):
        while(color.color() != til):
            if(gyro.angle() > 0 and color.color() != Color.BLACK):
                right.run(spd)
                left.run(spd * (1.5/2))
            if(gyro.angle() < 0 and color.color() != Color.BLACK):
                left.run(spd)
                right.run(spd * (1.5/2))
            if(color.color() == Color.BLACK):
                left.run(spd)
                right.run(spd)
        right.stop()
        left.stop()
    if(til == None):
        while(1):
            if(gyro.angle() > 0 and color.color() != Color.BLACK):
                right.run(spd)
                left.run(spd * (1.5/2))
            if(gyro.angle() < 0 and color.color() != Color.BLACK):
                left.run(spd)
                right.run(spd * (1.5/2))
            if(color.color() == Color.BLACK):
                left.run(spd)
                right.run(spd)