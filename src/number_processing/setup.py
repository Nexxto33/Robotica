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
    description='Ejercicio 2: Publicar impares, pares y calcular suma de cuadrados',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'odd_publisher = number_processing.odd_publisher:main',
        'even_publisher = number_processing.even_publisher:main',
        'sum_of_squares = number_processing.sum_of_squares:main',
        ],
    },
)
