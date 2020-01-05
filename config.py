# application settings and location of challenge mat image
fll_mat = 'city_shaper.png'         # location of fll challenge mat
win_x = 1196                        # in px (size of challenge mat)
win_y = 672                         # in px (size of challenge mat)

# location and size of robot on start
robot_size = [16.0, 18, 18.0]       # in cm (size of robot)
robot_start_pos = [5, 4]            # in cm (how far from edges does robot start)
robot_start_ang = 0                 # in deg (start angle of robot)
robot_gyro_pos = [12.7, 9]          # in cm (position of gyroscope)

# conversions
cmppx = float(202.0/1196.0)
pxpcm = float(1196.0/202.0)
