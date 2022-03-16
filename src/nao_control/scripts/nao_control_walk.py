#!/usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from nao_control.srv import Walk

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('nao_control_walk', anonymous=True)

# The "RobotCommander" object is an interface to Baxter (or any robot) as a whole.
robot = moveit_commander.RobotCommander()

# This is an interface to the world surrounding the robot.
scene = moveit_commander.PlanningSceneInterface()

# This is an interface to one group of joints.  In our case, we want to use the "right_arm".
#We will use this to plan and execute motions
group = moveit_commander.MoveGroupCommander("LeftLeg")

display_trajectory_publisher = rospy.Publisher(
                                    '/move_group/display_planned_path',
                                    moveit_msgs.msg.DisplayTrajectory)

print('============= Reference frame %s' % group.get_planning_frame())
print("============ End effector: %s" % group.get_end_effector_link())

current_poses = group.get_current_pose().pose


print(current_poses)
# 3D point and quaternion (same as previous lab, e.g. 0.644, 0.0, 0.0 for XYZ and
# -0.381, 0.923, -0.015, 0.052 for the XYZW components of the quaternion).
# NOTE: This point might fail if it is close or in the box! Choose a different point if that's the case
# pose_target = geometry_msgs.msg.Pose()
# # pose_target is initialised with zeros in all entries so let's popualate the quaternion
# pose_target.orientation.x = 0.178653537611
# pose_target.orientation.y = 0.0400617127597
# pose_target.orientation.z = 0.00728043053154
# pose_target.orientation.w = 0.983069157283


# pose_target.position.x = -0.0132845716903
# pose_target.position.y = 0.084872243712
# pose_target.position.z = -0.177776326579

# # # Now, add your Pose msg to the group's pose target
# group.set_pose_target(pose_target)
# group.allow_replanning(True)

# # and compute the plan!
# plan = group.plan()

# display_trajectory = moveit_msgs.msg.DisplayTrajectory()

# display_trajectory.trajectory_start = robot.get_current_state()
# display_trajectory.trajectory.append(plan)
# display_trajectory_publisher.publish(display_trajectory)
# group.go(wait=True)



#ret = group.execute(plan)
# # group.get_planning_frame()

# waypoints = []

# # start with the current pose
# waypoints.append(group.get_current_pose().pose)

# # first orient gripper and move forward (+x)
# wpose = geometry_msgs.msg.Pose()
# wpose.orientation.w = 1.0
# wpose.position.x = waypoints[0].position.x + 0.1
# wpose.position.y = waypoints[0].position.y
# wpose.position.z = waypoints[0].position.z
# waypoints.append(copy.deepcopy(wpose))

# # second move down
# wpose.position.z -= 0.10
# waypoints.append(copy.deepcopy(wpose))

# # third move to the side
# wpose.position.y += 0.05
# waypoints.append(copy.deepcopy(wpose))

# # The cartesian path will be interpolated at a resolution of 1 cm (i.e. 0.01 as the second argument below
# # for the end-effector. The third argument is to disable the "jump threshold" see:
# # http://docs.ros.org/kinetic/api/moveit_commander/html/classmoveit__commander_1_1move__group_1_1MoveGroupCommander.html#a4a3cfd21dd94bcc6991797e474c4d7f3
# (plan_cartesian, fraction) = group.compute_cartesian_path(waypoints, 0.01, 0.0)

# # If everything worked out fine, execute the above plan!
# group.execute(plan_cartesian)

# print(group.get_end_effector_link())
# print(group.get_current_pose().pose)

# rospy.wait_for_service('/right_leg')
# try:
#      # a client is created
#     walk_client = rospy.ServiceProxy('/right_leg', Walk)

#     rospy.loginfo('Instructions 2 sent.')
#     response = walk_client('Legs')

# except rospy.ServiceException as e:

#     print('Service call failed: %s' % e)