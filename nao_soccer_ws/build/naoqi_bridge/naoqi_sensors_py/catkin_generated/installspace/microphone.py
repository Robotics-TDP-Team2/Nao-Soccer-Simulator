#!/usr/bin/env python2
import rospy

from naoqi_sensors.naoqi_microphone import NaoqiMic

if __name__ == "__main__":
  ALToRosMics = NaoqiMic('ALToRosMics')
  ALToRosMics.start()
  rospy.spin()
