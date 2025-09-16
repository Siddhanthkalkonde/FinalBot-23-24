import pyfirmata
import time
import math

from CytronMotorDriver(h) import *



# class MotorControl:
#     def __init__(self, port='/dev/ttyACM0'):

#         self.board = pyfirmata.ArduinoMega(port)
#         # self.dirpin1 = self.board.get_pin('d:7:o')
#         # self.pwmpin1 = self.board.get_pin('d:6:p')
#         # self.dirpin2 = self.board.get_pin('d:4:o')
#         # self.pwmpin2 = self.board.get_pin('d:5:p')
#         # self.servopin = self.board.get_pin('d:{}:s'.format(9))

#         # 3 5 6 9 10 11  - pwm

#         #dir pins : 

#         self.front_left_dir = self.board.get_pin('d:22:o')
#         self.front_right_dir = self.board.get_pin('d:23:o')
#         self.back_left_dir = self.board.get_pin('d:24:o')
#         self.back_right_dir = self.board.get_pin('d:25:o')


#         # pwm pins: 

#         self.front_left_pwm = self.board.get_pin('d:2:p')
#         self.front_right_pwm = self.board.get_pin('d:3:p')
#         self.back_left_pwm = self.board.get_pin('d:4:p')
#         self.back_right_pwm = self.board.get_pin('d:5:p')




#         #servos ::

#         self.servo1 = self.board.get_pin('d:{}:s'.format(6))
#         self.servo2 = self.board.get_pin('d:{}:s'.format(7))



#         # ir input code
#         self.ir_in = self.board.get_pin('d:26:i')




       


       


#     # Functions for motor control
#     def forward(self, pwm):
#         # self.dirpin1.write(1)  
#         # self.pwmpin1.write(pwm)
#         # self.dirpin2.write(1)
#         # self.pwmpin2.write(pwm)"
#         self.front_left_dir.write(1)
#         self.front_right_dir.write(1)
#         self.back_left_dir.write(1)
#         self.back_right_dir.write(1)

#         self.front_left_pwm.write(pwm)
#         self.front_right_pwm.write(pwm)
#         self.back_left_pwm.write(pwm)
#         self.back_right_pwm.write(pwm)






#     def move_trigno(self, power, turn, theta):
#         # Calculate sine and cosine values
        
#         sine = math.sin(theta - 3.1413/4)
#         cose = math.cos(theta - 3.1413/4)

#         # Calculate maximum value between absolute sine and cosine
#         max_val = max(abs(sine), abs(cose))

#         # Calculate motor speeds based on parameters
#         val1 = (power * cose / max_val - turn)
#         val2 = (power * sine / max_val + turn)
#         val3 = (power * cose / max_val - turn)
#         val4 = (power * sine / max_val + turn)

#         # Set motor speeds
#         self.set_speeds(val1, val2, val3, val4)


#     def set_speeds(self  , v1, v2 ,v3, v4 ):

#         if v1<0:
#             self.front_left_dir.write(0)
#             self.front_left_pwm.write( -v1)

#         else:
#             self.front_left_dir.write(1)
#             self.front_left_pwm.write(v1)


#         if v2<0:
#             self.front_right_dir.write(0)
#             self.front_right_pwm.write( -v2)

#         else:
#             self.front_right_dir.write(1)
#             self.front_right_pwm.write(v2)


#         if v3<0:
#             self.back_left_dir.write(0)
#             self.back_left_pwm.write( -v3)

#         else:
#             self.back_left_dir.write(1)
#             self.back_left_pwm.write(v3)


#         if v4<0:
#             self.back_right_dir.write(0)
#             self.back_right_pwm.write( -v4)

#         else:
#             self.back_right_dir.write(1)
#             self.back_right_pwm.write(v4)







#     def backward(self, pwm):
#         # self.dirpin1.write(0)
#         # self.pwmpin1.write(pwm)
#         # self.dirpin2.write(0)
#         # self.pwmpin2.write(pwm)


#         self.front_left_dir.write(0)
#         self.front_right_dir.write(0)
#         self.back_left_dir.write(0)
#         self.back_right_dir.write(0)

#         self.front_left_pwm.write(pwm)
#         self.front_right_pwm.write(pwm)
#         self.back_left_pwm.write(pwm)
#         self.back_right_pwm.write(pwm)

#     def stop(self, pwm):
#         # self.pwmpin1.write(pwm)
#         # self.pwmpin2.write(pwm)

#         self.front_left_pwm.write(pwm)
#         self.front_right_pwm.write(pwm)
#         self.back_left_pwm.write(pwm)
#         self.back_right_pwm.write(pwm)

#     def left(self, pwm):
#         self.dirpin1.write(0)
#         self.pwmpin1.write(pwm)
#         self.dirpin2.write(1)
#         self.pwmpin2.write(pwm)

#     def right(self, pwm):
#         self.dirpin1.write(1)
#         self.pwmpin1.write(pwm)
#         self.dirpin2.write(0)
#         self.pwmpin2.write(pwm)


#     # def servo(self, logic):
#     #     delay_between_steps = 0.05  # Adjust this value to control the speed

#     #     if logic == 2:
#     #         for i in range(180):
#     #             self.servopin.write(i)

#     #     elif logic == 1:
#     #         for i in range(180, -1, -1):
#     #             self.servopin.write(i)
#     #     elif logic == 0:
#     #         self.servopin.write(self.servopin.read())  # Stop at current position



#     def servo_lock(self , state):

#         if state == 1:
#             self.servo1.write(90)
#             self.servo2.write(90)



#         elif state == 0:
#             self.servo1.write(0)
#             self.servo2.write(0)


#     def angle(self, angle):

#         if angle > 0:
#             self.dirpin2.write(1)  # Set motor controller to 1
#             self.pwmpin2.write(0.2)
#             self.dirpin1.write(0)  # Set motor controller to 0
#             self.pwmpin1.write(0.2)
#         else :
#             self.dirpin2.write(0)  # Set motor controller to 1
#             self.pwmpin2.write(0.2)
#             self.dirpin1.write(1)  # Set motor controller to 0
#             self.pwmpin1.write(0.2) # Set motor controller to 0


#     def angle_M(self, angle ,pwm):

#         if angle == 1:                         # for left
#             self.front_left_dir.write(1)
#             self.front_right_dir.write(0)
#             self.back_left_dir.write(0)
#             self.back_right_dir.write(1)

#             self.front_left_pwm.write(pwm)
#             self.front_right_pwm.write(pwm)
#             self.back_left_pwm.write(pwm)
#             self.back_right_pwm.write(pwm)
#         else :                                  #for right
#             self.front_left_dir.write(0)
#             self.front_right_dir.write(1)
#             self.back_left_dir.write(1)
#             self.back_right_dir.write(0)

 
#             self.front_left_pwm.write(pwm)
#             self.front_right_pwm.write(pwm)
#             self.back_left_pwm.write(pwm)
#             self.back_right_pwm.write(pwm)



#     def rotate(self ,dir,  pwm):

#         if(dir==1):


#             self.front_left_dir.write(0)
#             self.front_right_dir.write(1)
#             self.back_left_dir.write(0)
#             self.back_right_dir.write(1)


#             self.front_left_pwm.write(pwm)
#             self.front_right_pwm.write(pwm)
#             self.back_left_pwm.write(pwm)
#             self.back_right_pwm.write(pwm)

#         else:

#             self.front_left_dir.write(1)
#             self.front_right_dir.write(0)
#             self.back_left_dir.write(1)
#             self.back_right_dir.write(0)


#             self.front_left_pwm.write(pwm)
#             self.front_right_pwm.write(pwm)
#             self.back_left_pwm.write(pwm)
#             self.back_right_pwm.write(pwm)



#     def ir_input(self):
#         val = self.ir_in.read()

#         if(val == 1):
#             self.servo_lock(1)
#         else:
#             self.servo_lock(0)
  


 


 
#     def cammotor(self, logic):
#         if logic == 1 :
#             self.dirpin1.write(1)
#             self.pwmpin1.write(0.15)
#             if logic ==0 :
#                 self.pwmpin1.write(0)
#         elif logic ==2 :
#             self.dirpin1.write(0)
#             self.pwmpin1.write(0.15)
#             if logic == 0:
#                 self.pwmpin1.write(0)


#     def control(self):
#         while True:
#             val = input("Write directions: ")
#             if 'w' in val:
#                 self.forward(0.6)
#             elif 's' in val:
#                 self.backward(1)
#             elif 'a' in val:
#                 self.left(0.4)
#             elif 'd' in val:
#                 self.right(0.4)
#             else:
#                 self.stop(0)



class Cytron_driver:

    def __init__(self):
        self.front_left_motor = Motor(2, 22)
        self.front_right_motor = Motor(3, 23)
        self.back_left_motor = Motor(4, 24)
        self.back_right_motor = Motor( 5, 25)



    def forward(self , pwm):
        self.front_left_motor.setSpeed(pwm)
        self.front_right_motor.setSpeed(pwm)
        self.back_left_motor.setSpeed(pwm)
        self.back_right_motor.setSpeed(pwm)


    def backward(self , pwm):

        self.front_left_motor.setSpeed(-pwm)
        self.front_right_motor.setSpeed(-pwm)
        self.back_left_motor.setSpeed(-pwm)
        self.back_right_motor.setSpeed(-pwm)



    
    def angle_M(self, angle ,pwm):

        if angle == 1:                         # for left
        self.front_left_motor.setSpeed(pwm)
        self.front_right_motor.setSpeed(-pwm)
        self.back_left_motor.setSpeed(-pwm)
        self.back_right_motor.setSpeed(pwm)

        else :                                  #for right
        self.front_left_motor.setSpeed(-pwm)
        self.front_right_motor.setSpeed(pwm)
        self.back_left_motor.setSpeed(pwm)
        self.back_right_motor.setSpeed(-pwm)


    def stop(self, pwm):
        self.front_left_motor.setSpeed(0)
        self.front_right_motor.setSpeed(0)
        self.back_left_motor.setSpeed(0)
        self.back_right_motor.setSpeed(0)




    

# if __name__ == '__main__':
#     motor_controller = MotorControl()
#     motor_controller.control()
