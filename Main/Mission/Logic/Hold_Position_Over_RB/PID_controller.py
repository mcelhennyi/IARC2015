import time

__author__ = 'Austin'


class PIDController:

    def __init__(self, KP=0, KI=0, KD=0):
        self.KP = KP
        self.KI = KI
        self.KD = KD
        self.output_x = 0
        self.output_y = 0
        self.output_z = 0
        self.old_time = 0
        self.previous_error_x = 0
        self.previous_error_y = 0
        self.previous_error_z = 0
        self.integral_x = 0
        self.integral_y = 0
        self.integral_z = 0

    # PID correction in the X direction
    def pid_x(self, error_x, dt):
        # Sets the X integral
        self.integral_x += error_x*dt
        # Sets the X derivative
        derivative_x = (error_x - self.previous_error_x)/dt
        # Adjusts the X output by the constants KP, KI, and KD
        self.output_x = self.KP*error_x + self.KI*self.integral_x + self.KD*derivative_x
        # Sets the previous error for X
        self.previous_error_x = error_x

    # PID correction in the Y direction
    def pid_y(self, error_y, dt):
        # Sets the Y integral
        self.integral_y += error_y*dt
        # Sets the Y derivative
        derivative_y = (error_y - self.previous_error_y)/dt
        # Adjusts the Y output by the constants KP, KI, and KD
        self.output_y = self.KP*error_y + self.KI*self.integral_y + self.KD*derivative_y
        # Sets the previous error for Y
        self.previous_error_y = error_y

    # PID correction in the Z direction
    def pid_z(self, error_z, dt):
        # Sets the Z integral
        self.integral_z += error_z*dt
        # Sets the Z derivative
        derivative_z = (error_z - self.previous_error_z)/dt
        # Adjusts the Z output by the constants KP, KI, and KD
        self.output_z = self.KP*error_z + self.KI*self.integral_z + self.KD*derivative_z
        # Sets the previous error for Z
        self.previous_error_z = error_z

    # Takes the XYZ distances from the target location and returns the acceleration vector with the XYZ directions
    def get_output(self, error_x=0, error_y=0, error_z=0):
        current_time = int(round(time.time() * 1000))  # Gets the current time
        dt = current_time - self.old_time  # Gets the difference in current time and old time
        if self.old_time != 0:
            self.pid_x(error_x, dt)
            self.pid_y(error_y, dt)
            self.pid_z(error_z, dt)
        self.old_time = current_time  # Sets the old time to the current time after calling the previous functions
        # Creates the acceleration output array in the XYZ directions
        array = [self.output_x, self.output_y, self.output_z]
        return array
