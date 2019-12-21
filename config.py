# application settings and location of challenge mat image
fll_mat = 'city_shaper.png' # location of fll challenge mat
win_x = 1200                # in px (size of challenge mat)
win_y = 675                 # in px (size of challenge mat)

# location and size of robot on start
robot_size = [17, 19, 18]   # in cm (size of robot)
robot_start_pos = [4, 4]    # in cm (how far from edges does robot start)
robot_start_ang = 0         # in deg (start angle of robot)

# conversions
cmppx = float(202.0/1200.0)
pxpcm = float(1200.0/202.0)