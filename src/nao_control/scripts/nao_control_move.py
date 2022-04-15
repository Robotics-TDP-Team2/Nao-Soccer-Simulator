#!/usr/bin/env python
import sys
import rospy
import geometry_msgs.msg
from sensor_msgs.msg import LaserScan, Range
from tf.transformations import euler_from_quaternion
import tf
import math
from gazebo_msgs.srv import SpawnModel,DeleteModel,DeleteModelRequest,SpawnModelRequest
from gazebo_msgs.msg import LinkStates
from nav_msgs.msg import Odometry
from std_srvs.srv import Empty


naoName = ''
naoPose = None
previousState = ""
initialPose = None
footballPose = None
kickBall = False
turnBack = False
turnLeft = False
turnRight = False
resetWorld = False
speed = 1.0
distance = 0.0


def get_football_pose(msg):
        global footballPose
        for (link_idx, link_name) in enumerate(msg.name):
                modelname = link_name.split('::')[0]
                if 'football' == modelname:
                        footBallPose = msg.pose[link_idx]

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
        req.initial_pose = footballPose
        req.reference_frame = 'map'

        try:
                srv = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
                resp = srv(req)
        except  rospy.ServiceException as e:
                print("   Service call failed: %s" % e)
                sys.exit(1)


def calculate_distance():

        global naoName
        global naoPose
        global initialPose
        global turnBack
        global kickBall
        global turnLeft 
        global turnRight
        global speed
        global resetWorld
        global distance
        global previousState
        if naoPose != None and initialPose != None:
                distance = math.sqrt((naoPose.position.x-initialPose.position.x)**2 + (naoPose.position.y-initialPose.position.y)**2)
                rospy.loginfo('[{0}] Sliding Distance : {1}'.format(naoName, distance))
                if distance < 0.5:
                        kickBall = True
                        turnBack = False
                        resetWorld = False
                        speed = 1.0
                        previousState = ""
                if distance > 4:
                        turnBack = True
                        kickBall = False
                        turnLeft = False
                        turnRight = False

                
        
def check_obstacles(msg):

        global naoName
        rospy.loginfo("[{0}] Laser Distance Data: {1}".format(naoName,msg.ranges[359]))

def detect_obstacles_left(msg):
    
        global naoName
        global turnRight
        global kickBall
        global turnBack
        global turnLeft 
        global speed
        global previousState
        global distance
        rospy.loginfo("[{0}] Left Sonar Distance: {1}".format(naoName, msg.range))
        if msg.range < 1:
                
                if kickBall:
                        previousState = "kickBall"
                if turnBack:
                        previousState = "turnBack"
                turnRight = True
                kickBall = False
                turnBack = False

        else:
                turnRight = False
                if previousState == "kickBall":
                        kickBall = True
                        speed = 1
                if previousState == "turnBack" and distance > 0.5:
                        turnBack = True

def detect_obstacles_right(msg):
    
        global naoName
        global turnRight
        global kickBall
        global turnBack
        global turnLeft 
        global speed
        global previousState
        global distance
        rospy.loginfo("[{0}] Right Sonar Distance: {1}".format(naoName, msg.range))
        if msg.range < 1:
                
                if kickBall:
                        previousState = "kickBall"
                if turnBack:
                        previousState = "turnBack"
                kickBall = False
                turnBack = False
                turnLeft = True
        else:
                turnLeft = False
                if previousState == "kickBall":
                        kickBall = True
                        speed = 1
                if previousState == "turnBack" and distance > 0.5:
                        turnBack = True

def get_poses(msg):
        global naoPose
        global initialPose
        global resetWorld
        naoPose = msg.pose.pose
        orientation = naoPose.orientation
        (roll, pitch, yaw) = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
        #print("roll: {0} pitch: {1} yaw: {2}".format(roll, pitch, yaw))
        if initialPose == None:
                initialPose = naoPose
        if pitch < -1 or roll < -0.5:
                resetWorld = True

def main():
        global naoPose
        global initialPose
        global kickBall 
        global turnBack 
        global turnLeft 
        global turnRight 
        global naoName
        global speed
        global resetWorld
        naoName = sys.argv[1]
        rospy.init_node('nao_control_move')
        nao_vel_l = rospy.Publisher('%s/left/cmd_vel' % naoName, geometry_msgs.msg.Twist, queue_size=1)
        nao_vel_r = rospy.Publisher('%s/right/cmd_vel' % naoName, geometry_msgs.msg.Twist, queue_size=1)
        listener = tf.TransformListener()
        tfBroadcaster = tf.TransformBroadcaster()
        rospy.Subscriber("%s/odom" % naoName, Odometry, get_poses)
        rospy.Subscriber('%s/scan'% naoName , LaserScan, check_obstacles)
        rospy.Subscriber("%s/sonar_left" % naoName, Range, detect_obstacles_left)
        rospy.Subscriber("%s/sonar_right" % naoName, Range, detect_obstacles_right)
        reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)
        rate = rospy.Rate(5)

        while not rospy.is_shutdown():

                vel_msg_l = geometry_msgs.msg.Twist()
                vel_msg_r = geometry_msgs.msg.Twist()

                calculate_distance()

                if resetWorld:
                        kickBall = True
                        turnBack = False
                        turnLeft = False
                        turnRight = False
                        reset_world()
                        resetWorld = False

                if initialPose != None:

                        pos = initialPose.position
                        ori = initialPose.orientation

                        tfBroadcaster.sendTransform((pos.x, pos.y, 0), (ori.x, ori.y, ori.z, ori.w), rospy.Time.now(), "%s/initial_spot" % naoName, "map")


                if kickBall:

                        rospy.loginfo("[{0}] State: Going to kick the ball...".format(naoName))

                        try:
                                (trans, rot) = listener.lookupTransform('%s/base_link' % naoName, 'football', rospy.Time(0))
                        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                                continue
                                
                        
                        angular = math.atan2(trans[1], trans[0])
                        linear = math.sqrt(trans[1]**2 + trans[0]**2)    

                        vel_msg = geometry_msgs.msg.Twist()

                        vel_msg.linear.x = speed
                        vel_msg.angular.z = 4 * angular
                        
                        nao_vel_l.publish(vel_msg)
                        nao_vel_r.publish(vel_msg)

                if turnBack:
                        rospy.loginfo("[{0}] State: Going back...".format(naoName))
                        try:
                                (trans, rot) = listener.lookupTransform('%s/base_link' % naoName, '%s/initial_spot' % naoName, rospy.Time(0))
                        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                                continue
                                
                        angular = math.atan2(trans[1], trans[0])
                        linear = math.sqrt(trans[1]**2 + trans[0]**2)    
                        print(angular)
                        
                        if speed > 0.0:
                                speed = speed - 0.1
                                vel_msg_l.linear.x = speed
                                vel_msg_l.angular.z = 0.0
                                vel_msg_r.linear.x = speed
                                vel_msg_r.angular.z = 0.0
                                nao_vel_l.publish(vel_msg_l)
                                nao_vel_r.publish(vel_msg_r)
                                
                        
                        elif abs(angular) > 0.3:
                                vel_msg_l.linear.x = 1.7
                                vel_msg_l.angular.z = 0.0
                                vel_msg_r.linear.x = 0.0
                                vel_msg_r.angular.z = 0.0
                                nao_vel_l.publish(vel_msg_l)
                                nao_vel_r.publish(vel_msg_r)
                        else:
                                vel_msg_l.linear.x = 1
                                vel_msg_l.angular.z = 0.0
                                vel_msg_l.linear.x = 1
                                vel_msg_l.angular.z = 0.0
                                nao_vel_l.publish(vel_msg_l)
                                nao_vel_r.publish(vel_msg_l)

                if turnLeft and not turnRight:

                        rospy.loginfo("[{0}] State: Turning left...".format(naoName))
                        
                        vel_msg_l.linear.x = 0.5
                        vel_msg_l.angular.z = 0.0
                        vel_msg_r.linear.x = 1.0
                        vel_msg_r.angular.z = 0.0
                        nao_vel_l.publish(vel_msg_l)
                        nao_vel_r.publish(vel_msg_r)
                        

                if turnRight and not turnLeft:

                        rospy.loginfo("[{0}] Turning right...".format(naoName))

                        vel_msg_l.linear.x = 1.0
                        vel_msg_l.angular.z = 0.0
                        vel_msg_r.linear.x = 0.5
                        vel_msg_r.angular.z = 0.0
                        nao_vel_l.publish(vel_msg_l)
                        nao_vel_r.publish(vel_msg_r)

                if turnRight and turnLeft:
    
                        rospy.loginfo("[{0}] Going backward...".format(naoName))
                        
                        if speed > 0.0:
                                speed = speed - 0.2
                                vel_msg_l.linear.x = speed
                                vel_msg_l.angular.z = 0.0
                                vel_msg_r.linear.x = speed
                                vel_msg_r.angular.z = 0.0
                                nao_vel_l.publish(vel_msg_l)
                                nao_vel_r.publish(vel_msg_r)
                        else:
                                count = 10
                                while(count > 0):
                                        vel_msg_l.linear.x = -0.3
                                        vel_msg_l.angular.z = 0.0
                                        vel_msg_r.linear.x = -0.3
                                        vel_msg_r.angular.z = 0.0
                                        nao_vel_l.publish(vel_msg_l)
                                        nao_vel_r.publish(vel_msg_r)
                                        count = count -1
                                
                rate.sleep()
                
if __name__=='__main__':
        main()