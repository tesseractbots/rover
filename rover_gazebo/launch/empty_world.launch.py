#!/usr/bin/python3
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

package_name = 'gazebo_ros'
world_file = 'empty.world'

def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_rover_simulation = get_package_share_directory(package_name)

    # launch Gazebo by including its definition
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        )
    )

    # load the world file
    world_arg = DeclareLaunchArgument(
          'world',
          default_value=[os.path.join(pkg_rover_simulation, 'worlds', world_file), ''],
          description='SDF world file')

    return LaunchDescription([
        gazebo,
        world_arg
    ])
