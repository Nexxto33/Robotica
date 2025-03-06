import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SumOfSquares(Node):
    def __init__(self):
        super().__init__('sum_of_squares')
        self.subscription_odd = self.create_subscription(Int32, 'odd', self.process_number, 10)
        self.subscription_even = self.create_subscription(Int32, 'even', self.process_number, 10)
        self.sum_of_squares = 0

    def process_number(self, msg, msgs):
        self.sum_of_squares = (msg.data**2)+(msgs.data**2)
        self.get_logger().info(f'N1: {msg.data}, N2: {msgs.data}, suma de cuadrados: {self.sum_of_squares}')

def main(args=None):
    rclpy.init(args=args)
    node = SumOfSquares()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

