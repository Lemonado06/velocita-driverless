import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseArray, Pose


class ConePublisher(Node):
    def __init__(self):
        super().__init__('cone_publisher')
        self.pub = self.create_publisher(PoseArray, 'cones', 10)
        self.create_timer(1.0, self.publish_cones)

    def publish_cones(self):
        msg = PoseArray()
        msg.header.frame_id = 'base_link'
        msg.header.stamp = self.get_clock().now().to_msg()
        for i in range(5):
            for y in (-1.5, 1.5):
                p = Pose()
                p.position.x = 3.0 * (i + 1)
                p.position.y = y
                msg.poses.append(p)
        self.pub.publish(msg)
        self.get_logger().info(f'Published {len(msg.poses)} cones')


def main():
    rclpy.init()
    rclpy.spin(ConePublisher())


if __name__ == '__main__':
    main()