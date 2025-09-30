#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

import sys
import tty
import termios

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String,'topic', 10)
        if self.publisher_:
            self.get_logger().info("Self.publisher created successfully")
        else:
            self.get_logger().warn("Self.publisher is not created")

    def get_char_raw(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch

    def publish_key(self, key):
        msg = String()
        msg.data = key
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher()

    try:
        print("Press keys (press 'q' to quit):")
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.1)
            key = node.get_char_raw()
            if key == 'q':
                print("Exiting...")
                break
            else:
                node.publish_key(key)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
