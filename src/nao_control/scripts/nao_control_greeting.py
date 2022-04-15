#!/usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from nao_control.srv import Walk
import time

def main():

    controlled_robot = sys.argv[1]

    joint_state_topic = ['joint_states:=/%s/joint_states' % controlled_robot]
    moveit_commander.roscpp_initialize(joint_state_topic)
    rospy.init_node('nao_control_bend', anonymous=True)

    # The "RobotCommander" object is an interface to Baxter (or any robot) as a whole.
    robot = moveit_commander.RobotCommander(robot_description="/%s/robot_description" % controlled_robot)

    # This is an interface to the world surrounding the robot.
    scene = moveit_commander.PlanningSceneInterface(ns="%s" % controlled_robot)

    # This is an interface to one group of joints.  In our case, we want to use the "right_arm".
    #We will use this to plan and execute motions
    # dual_legs = moveit_commander.MoveGroupCommander("DualLegs")
    # dual_ankles = moveit_commander.MoveGroupCommander("DualAnkles")
    dual_arms = moveit_commander.MoveGroupCommander(robot_description="%s/robot_description" % controlled_robot, ns="%s" % controlled_robot, name="DualArms", wait_for_servers=15)
    right_arm = moveit_commander.MoveGroupCommander(robot_description="%s/robot_description" % controlled_robot, ns="%s" % controlled_robot, name="RightArm")
    # right_leg = moveit_commander.MoveGroupCommander("RightLeg")
    # left_foot = moveit_commander.MoveGroupCommander("LeftFoot")
    # right_foot = moveit_commander.MoveGroupCommander("RightFoot")
    # dual_leg_and_foot = moveit_commander.MoveGroupCommander(robot_description="%s/robot_description" % controlled_robot, ns="%s" % controlled_robot, name="DualLegNFoot")
    # left_leg_and_foot = moveit_commander.MoveGroupCommander("LeftLegNFoot")
    # right_leg_and_foot = moveit_commander.MoveGroupCommander("RightLegNFoot")
    display_trajectory_publisher = rospy.Publisher(
                                        '/move_group/display_planned_path',
                                        moveit_msgs.msg.DisplayTrajectory, queue_size=100)

    # print(left_poses)
    # print('==========================')
    # print(right_leg.get_current_joint_values())
    # print('==========================')
    # print(dual_arm.get_end_effector_link())
    # print('==========================')
    # print(left_leg.get_current_joint_values())
    # print('==========================')
    # print(dual_leg_and_foot.get_current_joint_values())
    # print('==========================')
    # print(left_leg_and_foot.get_current_joint_values())
    # print('==========================')
    # print(right_leg_and_foot.get_current_joint_values())
    # print('==========================')
    # print(right_leg.get_current_joint_values())
    # print('==========================')
    # print(dual_ankles.get_current_joint_values())
    # print('==========================')
    # print(dual_arms.get_current_joint_values())
    # print('==========================')

    # print('==========================')
    # print(left_foot.get_current_joint_values())
    # print('==========================')
    # print(right_foot.get_current_joint_values())
    # # print('==========================')


    dual_arms_goal = dual_arms.get_current_joint_values()
    dual_arms_goal[0] = 1.4994440768657593
    dual_arms_goal[1] = 0.23722563326939208
    dual_arms_goal[2] = -0.9354478151953253
    dual_arms_goal[3] = -0.4205305517881314
    dual_arms_goal[4] = 0.1684904781196155
    dual_arms_goal[5] = -0.6838118363196566
    dual_arms_goal[6] = -0.6328537993805452
    dual_arms_goal[7] = 0.47689642577743097
    dual_arms_goal[8] = 1.0748462329989668
    dual_arms_goal[9] = 0.2600176749475124
    dual_arms.go(dual_arms_goal, wait=True)

    joint_goal = right_arm.get_current_joint_values()
    joint_goal[0] = -0.7338076240370404
    joint_goal[1] = -0.44186343867907935
    joint_goal[2] = 0.6175222959372497
    joint_goal[3] = 1.544561373090613
    joint_goal[4] = 0.16218639430498863
    right_arm.go(joint_goal, wait=True)

    joint_goal = right_arm.get_current_joint_values()
    joint_goal[0] = -0.9806499945523408
    joint_goal[1] = -0.3629140529645366
    joint_goal[2] = 0.14231459158892942
    joint_goal[3] = 0.6519053880662526
    joint_goal[4] = 0.5211683936975348
    right_arm.go(joint_goal, wait=True)

    # joint_goal = right_arm.get_current_joint_values()
    # joint_goal[0] = -0.7338076240370404
    # joint_goal[1] = -0.44186343867907935
    # joint_goal[2] = 0.6175222959372497
    # joint_goal[3] = 1.544561373090613
    # joint_goal[4] = 0.16218639430498863
    # right_arm.go(joint_goal, wait=True)

    # joint_goal = right_arm.get_current_joint_values()
    # joint_goal[0] = -0.9806499945523408
    # joint_goal[1] = -0.3629140529645366
    # joint_goal[2] = 0.14231459158892942
    # joint_goal[3] = 0.6519053880662526
    # joint_goal[4] = 0.5211683936975348
    # right_arm.go(joint_goal, wait=True)

    dual_arms_goal = dual_arms.get_current_joint_values()
    dual_arms_goal[0] = 1.6661409253563078
    dual_arms_goal[1] = 0.16918605302427497
    dual_arms_goal[2] = -1.8956445092320382
    dual_arms_goal[3] = -1.1654296798327675
    dual_arms_goal[4] = 0.7506141786483534
    dual_arms_goal[5] = 1.7445967392373751
    dual_arms_goal[6] = -0.11417208635315783
    dual_arms_goal[7] = 1.8326646874132184
    dual_arms_goal[8] = 1.3430789457271364
    dual_arms_goal[9] = -0.7049685143930738
    dual_arms.go(dual_arms_goal, wait=True)

    # joint_goal = dual_leg_and_foot.get_current_joint_values()
    # joint_goal[0] = 0.025956484147903625
    # joint_goal[1] = -0.45158705312292935
    # joint_goal[2] = 0.996779919665135
    # joint_goal[3] = -0.5180285241
    # joint_goal[4] = 0.005652164285017625
    # joint_goal[5] = -0.45158705312292935
    # joint_goal[6] = 0.996779919665135
    # joint_goal[7] = -0.5180285241
    # dual_leg_and_foot.go(joint_goal, wait=True)



if __name__ == "__main__":
    main()

