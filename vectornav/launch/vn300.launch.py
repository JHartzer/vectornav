import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    this_dir = get_package_share_directory('vectornav')

    # Vectornav
    start_vectornav_cmd = Node(
        package='vectornav', 
        executable='vectornav',
        output='screen',
        name='vn300',
        parameters=[os.path.join(this_dir, 'config', 'vn300.yaml')])
    
    start_vectornav_sensor_msgs_cmd = Node(
        package='vectornav', 
        executable='vn_sensor_msgs',
        output='screen',
        name='vn300',
        parameters=[os.path.join(this_dir, 'config', 'vn300.yaml')])

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(start_vectornav_cmd)
    ld.add_action(start_vectornav_sensor_msgs_cmd)

    return ld
