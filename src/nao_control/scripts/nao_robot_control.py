#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from nao_control.srv import Walk
from nao_control.msg import Order

class MoveNao:
    def __init__(self):

        #moveit_commander.roscpp_initialize(sys.argv)

        rospy.init_node('nao_robot_control', anonymous=True)

        # robot = moveit_commander.RobotCommander()
        # scene = moveit_commander.PlanningSceneInterface()

        # display_trajectory_publisher = rospy.Publisher(
        #                             '/move_group/display_planned_path',
        #                             moveit_msgs.msg.DisplayTrajectory)
 
        # left_arm = moveit_commander.MoveGroupCommander('LeftArm')
        # right_arm = moveit_commander.MoveGroupCommander('RightArm')
        # left_leg = moveit_commander.MoveGroupCommander('LeftLeg')
        # right_leg = moveit_commander.MoveGroupCommander('RightLeg')
        # left_foot = moveit_commander.MoveGroupCommander('LeftFoot')
        # right_foot = moveit_commander.MoveGroupCommander('RightFoot')
        # head = moveit_commander.MoveGroupCommander('Head')
        
        # left_arm.set_goal_joint_tolerance(0.001)

        # current_poses = left_leg.get_current_pose().pose
        # print(current_poses)
        
        # pose_target = geometry_msgs.msg.Pose()
        # # pose_target is initialised with zeros in all entries so let's popualate the quaternion
        # pose_target.orientation.x = 0.128761653652
        # pose_target.orientation.y = 0.460521377745
        # pose_target.orientation.z = 0.0306687165539
        # pose_target.orientation.w = 0.877724288722


        # pose_target.position.x = 0.0288076175054
        # pose_target.position.y = -0.146631854204
        # pose_target.position.z = -0.0333476474659

        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)
        # #rospy.sleep(1)

        # # pose_target is initialised with zeros in all entries so let's popualate the quaternion
        # pose_target.orientation.x = -0.393929391889
        # pose_target.orientation.y = 0.494490327579
        # pose_target.orientation.z = 0.188152830885
        # pose_target.orientation.w = 0.751596608805


        # pose_target.position.x = 0.0548172319199
        # pose_target.position.y = 0.155008768815
        # pose_target.position.z = -0.0297059843191

        # # # Now, add your Pose msg to the group's pose target
        # left_arm.set_pose_target(pose_target)
        # left_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = left_arm.plan()
        # left_arm.go(wait=True)

        # pose_target.orientation.x = 0.128761653652
        # pose_target.orientation.y = 0.460521377745
        # pose_target.orientation.z = 0.0306687165539
        # pose_target.orientation.w = 0.877724288722

        # pose_target.position.x = 0.0288076175054
        # pose_target.position.y = -0.146631854204
        # pose_target.position.z = -0.0333476474659

        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)

        # pose_target.orientation.x = -0.0702701051184
        # pose_target.orientation.y = -0.635015723738
        # pose_target.orientation.z = 0.381828164662
        # pose_target.orientation.w = 0.6678505788

        # pose_target.position.x = 0.0545689639379
        # pose_target.position.y = -0.122208417204
        # pose_target.position.z = 0.210102367925
        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)

        # pose_target.orientation.x = 0.268557988797
        # pose_target.orientation.y = -0.580738788353
        # pose_target.orientation.z = -0.00305407833283
        # pose_target.orientation.w = 0.76851137855

        # pose_target.position.x = 0.0811987106801
        # pose_target.position.y = -0.17772088289
        # pose_target.position.z = 0.208481125557

        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)

        # pose_target.orientation.x = -0.0702701051184
        # pose_target.orientation.y = -0.635015723738
        # pose_target.orientation.z = 0.381828164662
        # pose_target.orientation.w = 0.6678505788

        # pose_target.position.x = 0.0545689639379
        # pose_target.position.y = -0.122208417204
        # pose_target.position.z = 0.210102367925
        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)


        # pose_target.orientation.x = 0.268557988797
        # pose_target.orientation.y = -0.580738788353
        # pose_target.orientation.z = -0.00305407833283
        # pose_target.orientation.w = 0.76851137855

        # pose_target.position.x = 0.0811987106801
        # pose_target.position.y = -0.17772088289
        # pose_target.position.z = 0.208481125557

        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)


        # pose_target.orientation.x = 0.128761653652
        # pose_target.orientation.y = 0.460521377745
        # pose_target.orientation.z = 0.0306687165539
        # pose_target.orientation.w = 0.877724288722


        # pose_target.position.x = 0.0288076175054
        # pose_target.position.y = -0.146631854204
        # pose_target.position.z = -0.0333476474659

        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)
        # #rospy.sleep(1) 

        # moveit_commander.roscpp_shutdown()
        # moveit_commander.os._exit(0)

        # while not rospy.is_shutdown():

        #     rospy.wait_for_service('/right_leg')
        #     try:
        #             # a client is created
        #             walk_client = rospy.ServiceProxy('/left_leg', Walk)

        #             rospy.loginfo('Instructions 1 sent.')
        #             response = walk_client('Legs')

        #     except rospy.ServiceException as e:

        #             print('Service call failed: %s' % e)

        #     rospy.wait_for_service('/left_leg')
        #     try:
        #             # a client is created
        #             walk_client = rospy.ServiceProxy('/right_leg', Walk)

        #             rospy.loginfo('Instructions 2 sent.')
        #             response = walk_client('Legs')

        #     except rospy.ServiceException as e:

        #             print('Service call failed: %s' % e)


        #to create a publisher
        order_info_pub = rospy.Publisher('/be_ready', Order, queue_size = 1)
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
    
                order_msg = Order()
                order_msg.ord = 'move'
                
                order_info_pub.publish(order_msg)

                rospy.loginfo('Publish Order Info: %s', order_msg.ord)

                rate.sleep()
        

if __name__ == "__main__":
    MoveNao()