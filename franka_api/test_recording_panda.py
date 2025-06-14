from lerobot.common.teleoperators.panda_leader import PandaTeleoperatorConfig, PandaTeleoperator
from lerobot.common.robots.panda_follower import PandaConfig, PandaRobot
import logging
IP_LEADER = "127.0.0.1:50051" # '192.168.178.52:50051'
IP_FOLLOWER = "127.0.0.1:50051" # "192.168.178.186:50051"


robot_config = PandaConfig(ip=IP_FOLLOWER)

teleop_config = PandaTeleoperatorConfig(ip=IP_LEADER)

robot = PandaRobot(robot_config)
teleop_device = PandaTeleoperator(teleop_config)
robot.connect()
teleop_device.connect()

while True:
    action = teleop_device.get_action()
    #robot.send_action(action)
    # current_postion = robot.get_pose()
    # logging.info(current_postion)
    robot.send_cart_pose_action([0.61, -0.01, 0.62, 0.93, -0.34, 0.02, -0.04])
    # home pose:   [0.61, -0.01, 0.52, 0.93, -0.34, 0.02, -0.04]


