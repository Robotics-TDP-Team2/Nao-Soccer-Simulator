execute_process(COMMAND "/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_tools/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_tools/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
