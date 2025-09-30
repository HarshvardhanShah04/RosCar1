import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy

def generate_launch_description():

    # Define the QoS profile for BEST_EFFORT reliability
    best_effort_qos = QoSProfile(
        reliability=ReliabilityPolicy.BEST_EFFORT,
        history=HistoryPolicy.KEEP_LAST,
        depth=1  # Only need the latest command
    )

    teleop_node = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard',
        output='screen',
        # Apply the QoS profile to the node's topics
        qos_profile=best_effort_qos,
        # No need for --ros-args --remap cmd_vel:=/cmd_vel if it's the default.
        # If you *do* need to remap (e.g., to /custom_cmd_vel), add:
        # remappings=[('/cmd_vel', '/custom_cmd_vel')]
    )

    return LaunchDescription([
        teleop_node
    ])
