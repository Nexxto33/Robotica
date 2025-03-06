import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

class AverageCalculator(Node):
    def __init__(self):
        super().__init__('average_calculator')
        self.subscription = self.create_subscription(
            Int8,
            '/numbers',
            self.listener_callback,
            10)
        self.sum = 0
        self.count = 0

    def listener_callback(self, msg):
        # Asegúrate de que estamos sumando correctamente y no hay reinicios
        self.sum += msg.data
        self.count += 1
        
        # Evitar división por cero (por si count es 0)
        if self.count > 0:
            average = self.sum / self.count
        else:
            average = 0
        
        self.get_logger().info(f'suma: {self.sum}, contador: {self.count},average: {average}')

def main(args=None):
    rclpy.init(args=args)
    node = AverageCalculator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

