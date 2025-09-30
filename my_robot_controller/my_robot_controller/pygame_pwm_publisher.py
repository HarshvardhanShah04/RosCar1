#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray 

import pygame
import math
# import threading

class pwmPublisher(Node):

    def __init__(self):
        super().__init__('pwm_publisher')
        self.publisher = self.create_publisher(Int32MultiArray, 'topic', 10)
        if self.publisher:
            self.get_logger().info("Publisher established")
        else:
            self.get_logger().warn("UNABLE TO ESTABLISH PUBLISHER")

        self.left_pwm = 0
        self.right_pwm = 0


    def publish_pwm_values(self):

        array = [self.left_pwm, self.right_pwm]
        self.pwm_msg = Int32MultiArray(data = array)

        self.publisher.publish(self.pwm_msg)


    def pygame_mouse(self):
        pygame.init()

        dimension = 500
        radius = 64
        centre = dimension/2        
        screen = pygame.display.set_mode((dimension, dimension))
        pygame.display.set_caption('JoyStick')
        clock = pygame.time.Clock()

        pygame.draw.circle(screen, (0,255,0), (centre, centre), 64, 2)
        pygame.draw.circle(screen, (255,255,255), (centre, centre), 5, )

        loop = True
        while loop:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
            
            pygame.display.update()
            
            pos = pygame.mouse.get_pos()

            dx = pos[0] - centre
            dy = pos[1] - centre
            
            check_inside_circle = True if math.sqrt(dx*dx + dy*dy) < radius + 6 else False
            
            click = True if pygame.mouse.get_pressed()[0] and check_inside_circle else False
            if click:
                pygame.mouse.set_cursor(pygame.cursors.diamond)


                x_coord = min(radius, max(-1*radius, pos[0] - centre))
                y_coord = min(radius, max(-1*radius, centre - pos[1]))

                x_value = x_coord/radius
                y_value = y_coord/radius

                diff_setter = max(-80, min(80, 80* x_coord/radius))
                forward = 200 * y_coord/radius

                self.left_pwm = forward + diff_setter 
                self.right_pwm = forward - diff_setter

                self.left_pwm = 5 * round(self.left_pwm/5) 
                self.right_pwm = 5 * round(self.right_pwm/5)

                if y_value < 0:
                    holder = self.left_pwm
                    self.left_pwm = self.right_pwm
                    self.right_pwm = holder



            if click == False:
                pygame.mouse.set_cursor()
                if abs(self.left_pwm)>20 or abs(self.right_pwm)>20:
                    self.left_pwm -= int(self.left_pwm/8)
                    self.right_pwm -= int(self.right_pwm/8)

                else:
                    self.left_pwm = 0
                    self.right_pwm = 0

            self.publish_pwm_values()
            print(f"left pwm: {self.left_pwm}", f" right pwm: {self.right_pwm}")
            rclpy.spin_once(self, timeout_sec = 0.01)
            clock.tick(30)

        pygame.quit()



def main(args = None):
    rclpy.init()
    node = pwmPublisher()

    try:
        print("Togle the joystick to move the bot")
        node.pygame_mouse()

    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()