import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OddPublisher(Node):
    def __init__(self):
        super().__init__('odd_publisher')
        self.publisher_ = self.create_publisher(Int32, 'odd', 10)
        self.counter = 1
        self.timer = self.create_timer(1.0, self.publish_odd)

    def publish_odd(self):
        msgs = Int32()
        msgs.data = self.counter
        self.publisher_.publish(msgs)
        self.get_logger().info(f'Publicando número impar: {msgs.data}')
        self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = OddPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

