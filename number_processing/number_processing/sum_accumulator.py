import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

class SumAccumulator(Node):
    def __init__(self):
        super().__init__('sum_accumulator')
        self.subscription = self.create_subscription(Int8, '/numbers', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Int8, 'sum', 10)
        self.total_sum = 0

    def listener_callback(self, msg):
        self.total_sum += msg.data
        sum_msg = Int8()
        sum_msg.data = self.total_sum
        self.publisher_.publish(sum_msg)
        self.get_logger().info(f'Suma acumulada: {self.total_sum}')
    

def main(args=None):
    rclpy.init(args=args)
    node = SumAccumulator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
