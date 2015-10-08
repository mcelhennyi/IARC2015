import PID_controller
import random
import time
__author__ = 'Austin'

# generate random distance

# loop
    # send distances to pid
    # get correction
    # calculate new distance
    # wait 10Hz
    # go till about 0
        # get new random distance
# go to top

plot_array_x = []
plot_array_y = []
i = 0

# distance_x = random.uniform(5, 20)
distance_x = 15
distance_y = random.uniform(5, 20)
vel_0_x = 0
vel_0_y = 0
pid = PID_controller.PIDController(KP=10, KI=.00001, KD=10)
d_time = .1

# loop
# while distance_x > .0001 and distance_y > .0001:
while True:
    # i += 1
    # plot_array_x[i] = distance_x
    # plot_array_y[i] = distance_y
    array = pid.get_output(error_x=distance_x, error_y=distance_y, error_z=0)
    print "X distance"
    print distance_x
    print "X acceleration"
    print array[0]
    # print "Y distance"
    # print distance_y
    # print array[1]
    # x = v0t + .5at2
    # v0 = x/t - .5at
    #
    traveled_x = vel_0_x*d_time + .5*array[0]*d_time*d_time
    # vel_0_x = traveled_x/d_time - .5*array[0]*d_time
    distance_x -= traveled_x
    #
    traveled_y = vel_0_y*d_time + .5*array[1]*d_time*d_time
    # vel_0_y = traveled_y/d_time - .5*array[1]*d_time
    distance_y -= traveled_y

    time.sleep(d_time)
