import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseArray


class ConeListener(Node):
    def __init__(self):
        super().__init__('cone_listener')
        self.create_subscription(PoseArray, 'cones', self.on_cones, 10)

    def on_cones(self, msg):
        first = msg.poses[0].position
        self.get_logger().info(
            f'Got {len(msg.poses)} cones, first at ({first.x}, {first.y})')


def main():
    rclpy.init()
    rclpy.spin(ConeListener())


if __name__ == '__main__':
    main()