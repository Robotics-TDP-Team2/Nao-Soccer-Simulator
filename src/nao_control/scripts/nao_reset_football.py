#!/usr/bin/env python
import sys
import rospy
import tf
import math
from gazebo_msgs.msg import LinkStates
from gazebo_msgs.srv import SpawnModel,DeleteModel,DeleteModelRequest,SpawnModelRequest



footballPose = None
def delete_football():
    
        try:
                srv = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
                req = DeleteModelRequest()
                req.model_name = "football"
                resp = srv(req)
        except rospy.ServiceException as e:
                print("Service call failed: %s" % e)
                sys.exit(1)

def respawn_football():

        global footballPose
        req = SpawnModelRequest()
        req.model_name = "football"
        req.model_xml = open("/home/lucas/nao_soccer_ws/src/nao_description/models/football.sdf", "r").read()
        req.robot_namespace = ""
        req.initial_pose.position.x = 0.0
        req.initial_pose.position.y = 1.0
        req.initial_pose.position.z = 0.08
        req.initial_pose.orientation.x = 0.0
        req.initial_pose.orientation.y = 0.0
        req.initial_pose.orientation.z = 0.0
        req.initial_pose.orientation.w = 1.0
        req.reference_frame = 'map'

        try:
                srv = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
                resp = srv(req)
        except  rospy.ServiceException as e:
                print("   Service call failed: %s" % e)
                sys.exit(1)

def get_football_pose(msg):
    
        global footballPose
        for (link_idx, link_name) in enumerate(msg.name):
                modelname = link_name.split('::')[0]
                if 'football' == modelname:
                        footballPose = msg.pose[link_idx]

def main():
        global footballPose
        rospy.init_node('nao_control_move')
        listener = tf.TransformListener()
        tfBroadcaster = tf.TransformBroadcaster()
        rospy.Subscriber('gazebo/link_states', LinkStates, get_football_pose)
        
        rate = rospy.Rate(5)

        while not rospy.is_shutdown():
                if footballPose != None:
                        pos = footballPose.position
                        ori = footballPose.orientation
                        # distance_goal_1 = math.sqrt((pos.x-4)**2 + (pos.y-1)**2)
                        # distance_goal_2 = math.sqrt((pos.x+4)**2 + (pos.y-1)**2)
                        if pos.x > 4 or pos.x < -4 or pos.y < -1.8 or pos.y > 3.8:
                                delete_football()
                                respawn_football()    

                rate.sleep()
                
if __name__=='__main__':
        main()