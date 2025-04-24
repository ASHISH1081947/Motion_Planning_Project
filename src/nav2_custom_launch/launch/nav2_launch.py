from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            name='nav2_bringup',
            output='screen',
            parameters=['/home/ashish/ros2_ws/src/nav2_custom_launch/params/nav2_params.yaml'],
            arguments=['map:=/home/ashish/ros2_ws/src/nav2_custom_launch/maps/map_home.yaml', 'use_sim_time:=false']
        )
    ])
