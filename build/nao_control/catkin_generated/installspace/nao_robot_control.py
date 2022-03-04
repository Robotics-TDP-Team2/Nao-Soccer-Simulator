#!/usr/bin/env python2

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from nao_control.srv import Walk

# class MoveNao:
#     def __init__(self):

        #moveit_commander.roscpp_initialize(sys.argv)

        #rospy.init_node('nao_robot_control', anonymous=True)

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

        # pose_target.orientation.x = 0.10346811826
        # pose_target.orientation.y = -0.696553976065
        # pose_target.orientation.z = 0.0715257116466
        # pose_target.orientation.w = 0.706392935628

        # pose_target.position.x = 0.0288798123835
        # pose_target.position.y = -0.170451373433
        # pose_target.position.z = 0.230531954703

        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)

        # pose_target.orientation.x = 0.0614875093238
        # pose_target.orientation.y = -0.635996614857
        # pose_target.orientation.z = 0.236744975631
        # pose_target.orientation.w = 0.731901228719

        # pose_target.position.x = 0.0665088184804
        # pose_target.position.y = -0.133700136626
        # pose_target.position.z = 0.223161578898
        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)


        # pose_target.orientation.x = 0.10346811826
        # pose_target.orientation.y = -0.696553976065
        # pose_target.orientation.z = 0.0715257116466
        # pose_target.orientation.w = 0.706392935628

        # pose_target.position.x = 0.0288798123835
        # pose_target.position.y = -0.170451373433
        # pose_target.position.z = 0.230531954703

        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)

        # pose_target.orientation.x = -0.118762295773
        # pose_target.orientation.y = -0.694580886345
        # pose_target.orientation.z = 0.285775561755
        # pose_target.orientation.w = 0.649449950135

        # pose_target.position.x = 0.022614832161
        # pose_target.position.y = -0.116364667938
        # pose_target.position.z = 0.236254276921

        # # # Now, add your Pose msg to the group's pose target
        # right_arm.set_pose_target(pose_target)
        # right_arm.allow_replanning(True)

        # # and compute the plan!
        # plan = right_arm.plan()
        # right_arm.go(wait=True)

        # pose_target.orientation.x = 0.10346811826
        # pose_target.orientation.y = -0.696553976065
        # pose_target.orientation.z = 0.0715257116466
        # pose_target.orientation.w = 0.706392935628

        # pose_target.position.x = 0.0288798123835
        # pose_target.position.y = -0.170451373433
        # pose_target.position.z = 0.230531954703


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

        # pose_target.orientation.x = 0.00284929034644
        # pose_target.orientation.y = -0.00304924081012
        # pose_target.orientation.z = -8.99317740741e-06
        # pose_target.orientation.w = 0.999991001828


        # pose_target.position.x = 0.0545011530493
        # pose_target.position.y = 0.0504945539934
        # pose_target.position.z = -0.168841396295

        # # # Now, add your Pose msg to the group's pose target
        # left_leg.set_pose_target(pose_target)
        # left_leg.allow_replanning(True)

        # # and compute the plan!
        # plan = left_leg.plan()
        # left_leg.go(wait=True)
        

        # pose_target.orientation.x = -0.0114209498345
        # pose_target.orientation.y = 0.00162804611345
        # pose_target.orientation.z = -1.85950704306e-05
        # pose_target.orientation.w = 0.999933453298


        # pose_target.position.x =  0.0653464107172
        # pose_target.position.y = -0.0517289242543
        # pose_target.position.z = -0.160676002982

        # # # Now, add your Pose msg to the group's pose target
        # right_leg.set_pose_target(pose_target)
        # right_leg.allow_replanning(True)

        # # and compute the plan!
        # plan = right_leg.plan()
        # right_leg.go(wait=True)


        # moveit_commander.roscpp_shutdown()
        # moveit_commander.os._exit(0)


        # rospy.wait_for_service('/walk')
        # try:
        #         # a client is created
        #         person_client = rospy.ServiceProxy('/walk', Walk)

        #         rospy.loginfo('Instructions sent.')
        #         response = person_client('Legs')
        #         return response.result

        # except rospy.ServiceException as e:

        #         print('Service call failed: %s' % e)

def move_client():
    rospy.init_node('nao_robot_control', anonymous=True)

if __name__ == "__main__":
    move_client()