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
        right_leg = moveit_commander.MoveGroupCommander('RightLeg')
        right_foot = moveit_commander.MoveGroupCommander('RightFoot')
        current_poses = right_leg.get_current_pose().pose
        rospy.loginfo('Current left_leg pose [ Position: x=%s y=%s x=%s, Orientation: x=%s y=%s z=%s w=%s]' % (str(current_poses.position.x),str(current_poses.position.y), str(current_poses.position.z), str(current_poses.orientation.x), str(current_poses.orientation.y), str(current_poses.orientation.z), str(current_poses.orientation.w)))
        current_poses = right_foot.get_current_pose().pose
        rospy.loginfo('Current left_foot pose [ Position: x=%s y=%s x=%s, Orientation: x=%s y=%s z=%s w=%s]' % (str(current_poses.position.x),str(current_poses.position.y), str(current_poses.position.z), str(current_poses.orientation.x), str(current_poses.orientation.y), str(current_poses.orientation.z), str(current_poses.orientation.w)))
        rospy.loginfo('Order : %s' % msg.ord)
        pose_target = geometry_msgs.msg.Pose()
        # pose_target is initialised with zeros in all entries so let's popualate the quaternion
        pose_target.orientation.x = -0.0237916017623
        pose_target.orientation.y = 0.281964539703
        pose_target.orientation.z = -0.00699443024184
        pose_target.orientation.w = 0.959104288376

        pose_target.position.x = 0.0651548492766
        pose_target.position.y = -0.0537612961234
        pose_target.position.z = -0.160767395806

        # # Now, add your Pose msg to the group's pose target
        right_leg.set_pose_target(pose_target)
        right_leg.allow_replanning(True)

        plan = right_leg.plan()
        right_leg.go(wait=True)

        pose_target.orientation.x = -0.0247439390094
        pose_target.orientation.y = 0.026011652899
        pose_target.orientation.z = -0.000646447356712
        pose_target.orientation.w = 0.999355148834

        pose_target.position.x = 0.00946540881125
        pose_target.position.y = -0.0580514947048
        pose_target.position.z = -0.24718898117

        # # Now, add your Pose msg to the group's pose target
        right_foot.set_pose_target(pose_target)
        right_foot.allow_replanning(True)

        # and compute the plan!
        plan = right_foot.plan()
        right_foot.go(wait=True)

def nao_be_ready():

        # to initialize a node 
        rospy.init_node('nao_be_ready_r', anonymous=True)

        # to create a subscriber 
        person_info_sub = rospy.Subscriber('/be_ready' , Order, orderCallBack)

        rospy.loginfo('Nao is ready!')
        rospy.spin()

if __name__ == '__main__':

        nao_be_ready()