#!/usr/bin/env python 
# -*- coding: utf-8 -*-
 
import roslib
import rospy  
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math 


class NavTest():  

    def cheak_obstacles(msg):
        print msg.ranges[360]
        if msg.ranges[360] < 1:
                self.left_move.linear.x = 1
                self.right_move.linear.x = 0
                self.stop = True
        else:
                self.left_move.linear.x = 2
                self.right_move.linear.x = 2
                self.stop = False

        self.left_vel_cmd_pub.publish(self.left_move)
        self.right_vel_cmd_pub.publish(self.right_move)


    def get_links_gazebo(link_states_msg):
        # Call back to retrieve the object you are interested in

        poses = {'map': link_states_msg.pose[0]} # get world link
        for (link_idx, link_name) in enumerate(link_states_msg.name):
                modelname = link_name.split('::')[0]
                for input_linkname in models:
                        if input_linkname == modelname:
                                poses[modelname] = link_states_msg.pose[link_idx]

        for key in poses:
                if key == "football":
                        self.footballPose = poses[key]

    def __init__(self):  
        rospy.init_node('find_football', anonymous=True)  
        rospy.on_shutdown(self.shutdown)  
        
        self.name = 'nao_1'
        self.models = ["%s" % self.name,"football"]
        self.naoPose = None
        self.footballPose = None
        self.stop = False
        rospy.Subscriber('gazebo/link_states', LinkStates, get_links_gazebo)
        rospy.Subscriber('%s/scan' % self.name, LaserScan, cheak_obstacles)

        self.left_cmd_vel_pub = rospy.Publisher('%s/left/cmd_vel' % self.name, Twist, queue_size=5)  
        self.right_cmd_vel_pub = rospy.Publisher('%s/right/cmd_vel' % self.name, Twist, queue_size=5)

        self.left_move = Twist()
        
        rate = rospy.Rate(20)
        while not rospy.is_shutdown(): 

                linear = None
                angular = None 

                if self.naoPose != None and self.footballPose != None:
                        naoPos = naoPose.position
                        naoOri = naoPose.orientation
                        ballPos = footballPose.position
                        ballOri = footballPose.orientation
                        print(naoPos.x)
                        print(naoPos.y)
                        print(naoPos.z)
                        linear = math.sqrt((naoPos.x-ballPos.x)**2 + (naoPos.y-ballPos.y)**2)
                        angular = math.atan2(trans3[1], trans3[0])

                if !self.stop:

                        self.left_move.linear.x = 2
                        self.left_move.angular.z = 4 * angular
                        self.right_move.linear.x = 2
                        self.right_move.angular.z = 4 * angular

                        self.left_cmd_vel_pub.publish(self.left_move)
                        self.right_cmd_vel_pub.publish(self.right_move)

                rate.sleep()


if __name__ == '__main__':    
        NavTest() 