from setuptools import find_packages, setup

package_name = 'number_processing'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nelson',
    maintainer_email='nelson.ramirez@ucb.edu.bo',
    description='Paquete para generación, acumulación y promedio de números en ROS 2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
 'number_generator = number_processing.number_generator:main',
            'sum_accumulator = number_processing.sum_accumulator:main',
            'average_calculator = number_processing.average_calculator:main',

        ],
    },
)
