#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class HardwareStatusPublisherNode(Node):
    def __init__(self):
        super().__init__("hardware_status_publisher")


    def main(args=None):
        rclpy.init(args=args)

        node = HardwareStatusPublisherNode()

        rclpy.spin()
        rclpy.shutdown()