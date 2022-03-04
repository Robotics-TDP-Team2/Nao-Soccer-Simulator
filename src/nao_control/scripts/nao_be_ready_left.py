#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from nao_control.msg import Order 

def orderCallBack(msg):

        moveit_commander.roscpp_initialize(sys.argv)
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()

        display_trajectory_publisher = rospy.Publisher(
                                    '/move_group/display_planned_path',
                                    moveit_msgs.msg.DisplayTrajectory)
        left_leg = moveit_commander.MoveGroupCommander('LeftLeg')
        left_foot = moveit_commander.MoveGroupCommander('LeftFoot')
        current_poses = left_leg.get_current_pose().pose
        rospy.loginfo('Current left_leg pose [ Position: x=%s y=%s x=%s, Orientation: x=%s y=%s z=%s w=%s]' % (str(current_poses.position.x),str(current_poses.position.y), str(current_poses.position.z), str(current_poses.orientation.x), str(current_poses.orientation.y), str(current_poses.orientation.z), str(current_poses.orientation.w)))
        current_poses = left_foot.get_current_pose().pose
        rospy.loginfo('Current left_foot pose [ Position: x=%s y=%s x=%s, Orientation: x=%s y=%s z=%s w=%s]' % (str(current_poses.position.x),str(current_poses.position.y), str(current_poses.position.z), str(current_poses.orientation.x), str(current_poses.orientation.y), str(current_poses.orientation.z), str(current_poses.orientation.w)))
        rospy.loginfo('Order : %s' % msg.ord)
        pose_target = geometry_msgs.msg.Pose()
        # pose_target is initialised with zeros in all entries so let's popualate the quaternion
        pose_target.orientation.x = 0.0107219640072
        pose_target.orientation.y = 0.293979090281
        pose_target.orientation.z = 0.00329798205227
        pose_target.orientation.w = 0.955746021326

        pose_target.position.x = 0.065845535497
        pose_target.position.y = 0.0516884290698
        pose_target.position.z = -0.160243037302

        # # Now, add your Pose msg to the group's pose target
        left_leg.set_pose_target(pose_target)
        left_leg.allow_replanning(True)

        plan = left_leg.plan()
        left_leg.go(wait=True)

        pose_target.orientation.x = 0.0112546709582
        pose_target.orientation.y = 0.00900975122859
        pose_target.orientation.z = 0.000100738091812
        pose_target.orientation.w = 0.999896067907
        
        pose_target.position.x = 0.00801476685126
        pose_target.position.y = 0.0535978284379
        pose_target.position.z = -0.245333379832

        # # Now, add your Pose msg to the group's pose target
        left_foot.set_pose_target(pose_target)
        left_foot.allow_replanning(True)

        # and compute the plan!
        plan = left_foot.plan()
        left_foot.go(wait=True)

def nao_be_ready():

        # to initialize a node 
        rospy.init_node('nao_be_ready_l', anonymous=True)

        # to create a subscriber 
        person_info_sub = rospy.Subscriber('/be_ready' , Order, orderCallBack)

        rospy.loginfo('Nao is ready!')
        rospy.spin()

if __name__ == '__main__':

        nao_be_ready()