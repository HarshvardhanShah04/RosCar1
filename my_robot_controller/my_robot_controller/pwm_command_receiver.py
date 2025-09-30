#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

import socket
import struct

class MinimalSubscriber(Node):
    DEF_ESP_IP = "192.168.4.1"
    DEF_ESP_PORT = 3333

    def __init__(self, ESP_IP = DEF_ESP_IP, ESP_PORT = DEF_ESP_PORT):
        super().__init__('command_receiver')
        self.subscription = self.create_subscription(
            Int32MultiArray,
            'topic',
            self.listener_callback,
            10
        )
        self.ESP_IP = ESP_IP
        self.ESP_PORT = ESP_PORT
        self.setup_socket()


    def setup_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(2.0)
        try:
            self.sock.connect((self.ESP_IP, self.ESP_PORT))
            self.get_logger().info(f"[INFO] Connected to ESP32 at {self.ESP_IP}:{self.ESP_PORT}")
        except Exception as e:
            self.get_logger().error(f"[ERROR] Could not connect to ESP32: {e}")
            self.sock = None  # So we can check later if connection failed

    

    def listener_callback(self, msg):
        key = msg.data
        self.get_logger().info(f'Received pwm values: "{key[0]}"')

        if not key:
            return

        if self.sock is None:
            self.get_logger().warn("Socket is disconnected...")
            self.get_logger().info("Attempting to reconnect..")
            self.setup_socket()
            if self.sock is None:
                self.get_logger().error("Reconnection Failed.")
                return

        try:
            data = struct.pack('<2i', *key)
            self.sock.sendall(data)
            self.get_logger().info(f'Sent to ESP: "{key[0]}"')
        except Exception as e:
            self.get_logger().error(f"Socket send error: {e}")
            if self.sock is not None:
                self.sock.close()
                self.sock = None

def main(args=None):
    rclpy.init(args=args)
    node = MinimalSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        if node.sock:
            node.sock.close()
            print("[INFO] Socket closed")


if __name__ == '__main__':
    main()
