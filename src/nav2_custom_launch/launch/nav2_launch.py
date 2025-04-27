from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': '/home/ashish/ros2_ws/src/nav2_custom_launch/maps/map_home.yaml',
            'use_sim_time': 'false',
            'autostart': 'true',
            'params_file': '/home/ashish/ros2_ws/src/nav2_custom_launch/params/nav2_params.yaml'
        }.items()
    )

    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': open('/home/ashish/ros2_ws/src/my_robot_description/urdf/my_robot.urdf').read()
        }]
    )

    return LaunchDescription([
        robot_state_pub,
        nav2_launch
    ])

