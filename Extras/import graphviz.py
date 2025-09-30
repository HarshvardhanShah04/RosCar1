import graphviz

# Create a flowchart using Graphviz
dot = graphviz.Digraph(format='png')
dot.attr(rankdir='TB', size='15,25')

# Main nodes
dot.node('Sensors', 'Sensors\n(IMU, Encoders, IR, Bumpers)', shape='box', style='filled', fillcolor='lightgray')
dot.node('Create3', 'Create 3 Base\n(Runs ROS 2 Nodes)', shape='box', style='filled', fillcolor='lightblue')
dot.node('USB', 'USB-C / Virtual Network\n(DDS Communication)', shape='oval', style='filled', fillcolor='white')
dot.node('RPI4', 'Raspberry Pi 4 B\n(ROS 2 App Layer)', shape='box', style='filled', fillcolor='lightgreen')
dot.node('User', 'User Apps\n(SLAM, Nav2, Teleop)', shape='box', style='filled', fillcolor='yellow')

# Edges for sensor data to Create3
dot.edge('Sensors', 'Create3', label='Sensor data\n(IMU, Odometry, Buttons, etc.)')

# Create3 to RPI4 communication
dot.edge('Create3', 'USB', label='ROS 2 Topics/Actions\n(e.g., /odom, /imu, /cmd_vel)')
dot.edge('USB', 'RPI4')

# RPI4 to user apps
dot.edge('RPI4', 'User', label='High-level ROS 2 nodes\n(Nav, SLAM, Behavior)')

# Command flow from User to Create3
dot.edge('User', 'RPI4', label='/cmd_vel, /dock\nor other actions')
dot.edge('RPI4', 'USB')
dot.edge('USB', 'Create3', label='Velocity & Action Commands')

# Render the file
dot.attr(dpi='600')  # or 600 for very high quality
dot.render('turtlebot4_data_flow', cleanup=True)
