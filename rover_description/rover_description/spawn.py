#!/usr/bin/python3
import os 
import sys
import rclpy
from gazebo_msgs.srv import SpawnEntity
from ament_index_python.packages import get_package_share_directory

package_name = 'rover_description'

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('minimal_client')
    cli = node.create_client(SpawnEntity, '/spawn_entity')

    sdf_file_path = (os.path.join(get_package_share_directory(package_name), 'urdf', 'rover.urdf')),
    model = open(sdf_file_path[0], 'r').read()

    print("MODEL %s" %model)
    
    req = SpawnEntity.Request(
        name = "rover",
        xml = model,
        robot_namespace = "1",
        reference_frame = "world",
    )

    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        node.get_logger().info(
            'Result ' + str(future.result().success) + " " + future.result().status_message)
    else:
        node.get_logger().info('Service call failed %r' % (future.exception(),))

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

