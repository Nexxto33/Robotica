import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
import random

class NumberGenerator(Node):
    def __init__(self):
        super().__init__('number_generator')
        self.publisher_ = self.create_publisher(Int8, '/numbers', 10)
        self.timer = self.create_timer(1.0, self.publish_random_number)

    def publish_random_number(self):
        msg = Int8()
        msg.data = random.randint(1, 100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando número: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberGenerator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
