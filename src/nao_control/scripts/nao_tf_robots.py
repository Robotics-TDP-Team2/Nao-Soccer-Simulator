#!/usr/bin/env python

import rospy
import tf
from gazebo_msgs.msg import LinkStates

# This is hard-coded to block for this exercise, yet you can make the script general by adding cmd line arguments
models = ["nao_1", "nao_2", "football"]

# Global variable where the object's pose is stored
nao1Pose = None
nao2Pose = None
footballPose = None


def get_links_gazebo(link_states_msg):
    # Call back to retrieve the object you are interested in
    global models
    global nao1Pose
    global nao2Pose
    global footballPose
    poses = {'map': link_states_msg.pose[0]} # get world link
    for (link_idx, link_name) in enumerate(link_states_msg.name):
        modelname = link_name.split('::')[0]
        for input_linkname in models:
            if input_linkname == modelname:
                poses[modelname] = link_states_msg.pose[link_idx]

    for key in poses:
        if key == "nao_1":
            nao1Pose = poses["nao_1"]
        if key == "nao_2":
            nao2Pose = poses["nao_2"]
        if key == "football":
            footballPose = poses["football"]



def main():
    rospy.init_node('nao_tf_robots')

    # Create TF broadcaster -- this will publish a frame give a pose
    tfBroadcaster = tf.TransformBroadcaster()
    # SUbscribe to Gazebo's topic where all links and objects poses within the simulation are published
    rospy.Subscriber('gazebo/link_states', LinkStates, get_links_gazebo)

    rospy.loginfo('Spinning')
    global nao1Pose
    global nao2Pose
    global footballPose
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():

        if nao1Pose is not None:
            pos = nao1Pose.position
            ori = nao1Pose.orientation
            #rospy.loginfo(pos)
            # Publish transformation given in nao1Pose
            tfBroadcaster.sendTransform((pos.x, pos.y, pos.z), (ori.x, ori.y, ori.z, ori.w), rospy.Time.now(), "nao_1/base_link", 'nao_1/odom')
            rate.sleep()

        if nao2Pose is not None:
            pos = nao2Pose.position
            ori = nao2Pose.orientation
            #rospy.loginfo(pos)
            # Publish transformation given in nao2Pose
            tfBroadcaster.sendTransform((pos.x, pos.y, pos.z), (ori.x, ori.y, ori.z, ori.w), rospy.Time.now(), "nao_2/base_link", 'nao_2/odom')
            rate.sleep()

        if footballPose is not None:
            pos = footballPose.position
            ori = footballPose.orientation
            #rospy.loginfo(pos)
            # Publish transformation given in footballPose
            tfBroadcaster.sendTransform((pos.x, pos.y, pos.z), (ori.x, ori.y, ori.z, ori.w), rospy.Time.now(), "football", 'map')
            rate.sleep()
    
    rospy.spin()


if __name__ == '__main__':
    main()