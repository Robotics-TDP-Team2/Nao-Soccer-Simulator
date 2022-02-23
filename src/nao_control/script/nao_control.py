#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('nao_control', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group1 = moveit_commander.MoveGroupCommander("LeftArm")
print("============ Reference frame: %s" % group1.get_planning_frame())
print("============ Reference frame: %s" % group1.get_end_effector_link())

group1.set_random_target()

plan = group1.go()
print(plan)
group1.clear_pose_targets()

group2 = moveit_commander.MoveGroupCommander("RightArm")
print("============ Reference frame: %s" % group2.get_planning_frame())
print("============ Reference frame: %s" % group2.get_end_effector_link())
print("============ Robot Groups:")

group2.set_random_target()

plan = group2.go()
print(plan)

group2.clear_pose_targets()

group3 = moveit_commander.MoveGroupCommander("Head")
print("============ Reference frame: %s" % group3.get_planning_frame())
print("============ Reference frame: %s" % group3.get_end_effector_link())
#print("============ Robot Groups:")
#print(robot.get_group_names())
#print("============ Printing robot state")
#print("============ Generating plan")
# pose_target = geometry_msgs.msg.Pose()
# pose_target.orientation.w = 0.999140170114
# pose_target.orientation.x = 0.00870820429358
# pose_target.orientation.y = 0.0387639416505
# pose_target.orientation.z = -0.0118509270157

# pose_target.position.x = 0.159910126981
# pose_target.position.y = 0.115082506439
# pose_target.position.z = 0.0874946336454

# group.set_goal_position_tolerance(0.1)
# group.set_goal_orientation_tolerance(0.1)
# group.set_pose_target(pose_target)
group3.set_random_target()

plan = group3.go()
print(plan)

group3.clear_pose_targets()

group4 = moveit_commander.MoveGroupCommander("LeftLeg")
print("============ Reference frame: %s" % group4.get_planning_frame())
print("============ Reference frame: %s" % group4.get_end_effector_link())

group4.set_random_target()

plan = group4.go()
print(plan)

group4.clear_pose_targets()