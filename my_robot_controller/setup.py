from setuptools import find_packages, setup

package_name = 'my_robot_controller'

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
    maintainer='harsh',
    maintainer_email='harshvardhan.shah43@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard_sender = my_robot_controller.keyboard_sender:main',  # Publisher

            # Entry for subscriber node (command_receiver)
            'command_receiver = my_robot_controller.command_receiver:main',

            'pwm_publisher = my_robot_controller.pygame_pwm_publisher:main',

            'pwm_subscriber = my_robot_controller.pwm_command_receiver:main'
        ],
    },
)
