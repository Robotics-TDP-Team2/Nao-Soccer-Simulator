# Install script for directory: /home/lucas/myrobot_ws/src/naoqi_bridge/naoqi_sensors_py

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/lucas/myrobot_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_sensors_py/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/naoqi_sensors_py" TYPE FILE FILES "/home/lucas/myrobot_ws/devel/include/naoqi_sensors_py/NaoqiCameraConfig.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/naoqi_sensors_py" TYPE FILE FILES "/home/lucas/myrobot_ws/devel/include/naoqi_sensors_py/NaoqiMicrophoneConfig.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/naoqi_sensors_py" TYPE FILE FILES "/home/lucas/myrobot_ws/devel/lib/python2.7/dist-packages/naoqi_sensors_py/__init__.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/lucas/myrobot_ws/devel/lib/python2.7/dist-packages/naoqi_sensors_py/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/naoqi_sensors_py" TYPE DIRECTORY FILES "/home/lucas/myrobot_ws/devel/lib/python2.7/dist-packages/naoqi_sensors_py/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_sensors_py/catkin_generated/installspace/naoqi_sensors_py.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/naoqi_sensors_py/cmake" TYPE FILE FILES
    "/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_sensors_py/catkin_generated/installspace/naoqi_sensors_pyConfig.cmake"
    "/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_sensors_py/catkin_generated/installspace/naoqi_sensors_pyConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/naoqi_sensors_py" TYPE FILE FILES "/home/lucas/myrobot_ws/src/naoqi_bridge/naoqi_sensors_py/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/naoqi_sensors_py" TYPE PROGRAM FILES "/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_sensors_py/catkin_generated/installspace/camera.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/naoqi_sensors_py" TYPE PROGRAM FILES "/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_sensors_py/catkin_generated/installspace/microphone.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/naoqi_sensors_py" TYPE PROGRAM FILES "/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_sensors_py/catkin_generated/installspace/octomap.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/naoqi_sensors_py" TYPE PROGRAM FILES "/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_sensors_py/catkin_generated/installspace/sonar.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/naoqi_sensors_py/launch" TYPE FILE FILES
    "/home/lucas/myrobot_ws/src/naoqi_bridge/naoqi_sensors_py/launch/camera.launch"
    "/home/lucas/myrobot_ws/src/naoqi_bridge/naoqi_sensors_py/launch/microphone.launch"
    "/home/lucas/myrobot_ws/src/naoqi_bridge/naoqi_sensors_py/launch/octomap.launch"
    "/home/lucas/myrobot_ws/src/naoqi_bridge/naoqi_sensors_py/launch/sonar.launch"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/naoqi_sensors_py" TYPE DIRECTORY FILES "/home/lucas/myrobot_ws/src/naoqi_bridge/naoqi_sensors_py/share")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/lucas/myrobot_ws/build/naoqi_bridge/naoqi_sensors_py/src/cmake_install.cmake")

endif()

