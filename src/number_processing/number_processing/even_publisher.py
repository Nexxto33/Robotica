import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenPublisher(Node):
    def __init__(self):
        super().__init__('even_publisher')
        self.publisher_ = self.create_publisher(Int32, 'even', 10)
        self.counter = 2
        self.timer = self.create_timer(1.0, self.publish_even)

    def publish_even(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando número par: {msg.data}')
        self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

