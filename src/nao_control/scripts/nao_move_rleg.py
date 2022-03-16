#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from nao_control.srv import Walk, WalkResponse

def walkCallBack(req):

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
        rospy.loginfo('Walk [ joint: %s]' % req.joint)
        pose_target = geometry_msgs.msg.Pose()
        # pose_target is initialised with zeros in all entries so let's popualate the quaternion
        pose_target.orientation.x = 0.0018683934445
        pose_target.orientation.y = 0.043572293367
        pose_target.orientation.z = 8.14877207193e-05
        pose_target.orientation.w = 0.999048526207

        pose_target.position.x = 0.0336765011852
        pose_target.position.y = -0.0496478144951
        pose_target.position.z = -0.179158213839

        # # Now, add your Pose msg to the group's pose target
        right_leg.set_pose_target(pose_target)
        right_leg.allow_replanning(True)

        plan = right_leg.plan()
        right_leg.go(wait=True)

        # pose_target.orientation.x = -0.0247439390094
        # pose_target.orientation.y = 0.026011652899
        # pose_target.orientation.z = -0.000646447356712
        # pose_target.orientation.w = 0.999355148834

        # pose_target.position.x = 0.00946540881125
        # pose_target.position.y = -0.0580514947048
        # pose_target.position.z = -0.24718898117

        # # # Now, add your Pose msg to the group's pose target
        # right_foot.set_pose_target(pose_target)
        # right_foot.allow_replanning(True)

        # and compute the plan!
        # plan = right_foot.plan()
        # right_foot.go(wait=True)
        return WalkResponse('Done')

def move_right_leg():

        # to initialize a node 
        rospy.init_node('nao_move_rleg', anonymous=True)

        # to create a server
        rospy.Service('/right_leg', Walk, walkCallBack)

        rospy.loginfo('Ready to walk!')
        rospy.spin()

if __name__ == '__main__':

        move_right_leg()