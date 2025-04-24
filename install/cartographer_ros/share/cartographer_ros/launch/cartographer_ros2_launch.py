from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[{
                'use_sim_time': False
            }],
            arguments=[
                '-configuration_directory', '/home/ashish/ros2_ws/src/cartographer_ros/config',
                '-configuration_basename', 'backpack_2d.lua'
            ],
            remappings=[
                ('scan', '/scan')
            ]
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser']
        )
    ])
