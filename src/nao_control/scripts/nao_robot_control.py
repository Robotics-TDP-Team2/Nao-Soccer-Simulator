#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
Control mrobot!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly

CTRL-C to quit
"""

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

speedBindings={
        'q':(1.1,1.1),
        # 'z':(.9,.9),
        # 'w':(1.1,1),
        # 'x':(.9,1),
        # 'e':(1,1.1),
        # 'c':(1,.9),
          }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = .2
turn = 1

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('nao_teleop1')
    pub = rospy.Publisher('nao_2/left/cmd_vel', Twist, queue_size=5)
    pub1 = rospy.Publisher('nao_2/right/cmd_vel', Twist, queue_size=5)

    x = 0
    th = 0
    x1 = 0
    th1 = 0
    status = 0
    count = 0
    count1 = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    target1_speed = 0
    target1_turn = 0
    control_speed = 0
    control_turn = 0
    control1_speed = 0
    control1_turn = 0
    try:
        print (msg)
        print (vels(speed,turn))
        while(1):
            key = getKey()
            # 运动控制方向键（1：正方向，-1负方向）
            if key  == 'i':
                x = 1
                th = 0
                x1 = 1
                th1 = 0
                count = 0
            elif key  == 'j':
                x = 0
                th = 0
                x1 = 1
                th1 = 0
                count = 0
            elif key  == 'l':
                x =  1
                th = 0
                x1 = 0
                th1 = 0
                count = 0
            elif key  == 'k':
                x =  -1
                th = 0
                x1 = -1
                th1 = 0
                count = 0
            # 速度修改键
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]  # 线速度增加0.1倍
                turn = turn * speedBindings[key][1]    # 角速度增加0.1倍
                count = 0

                print (vels(speed,turn))
                if (status == 14):
                    print (msg)
                status = (status + 1) % 15
            else:
                count = count + 1
                if count > 4:
                    x = 0
                    th = 0
                    x1 = 0
                    th1 = 0
                if (key == '\x03'):
                    break

            # 目标速度=速度值*方向值
            target_speed = speed * x
            target_turn = turn * th
            target1_speed = speed * x1
            target1_turn = turn * th1
            # 速度限位，防止速度增减过快
            if target_speed > control_speed:
                control_speed = min( target_speed, control_speed + 0.02 )
            elif target_speed < control_speed:
                control_speed = max( target_speed, control_speed - 0.02 )
            else:
                control_speed = target_speed

            if target_turn > control_turn:
                control_turn = min( target_turn, control_turn + 0.1 )
            elif target_turn < control_turn:
                control_turn = max( target_turn, control_turn - 0.1 )
            else:
                control_turn = target_turn



            if target1_speed > control1_speed:
                control1_speed = min( target1_speed, control1_speed + 0.02 )
            elif target1_speed < control1_speed:
                control1_speed = max( target1_speed, 1 - 0.02 )
            else:
                control1_speed = target1_speed

            if target1_turn > control1_turn:
                control1_turn = min( target1_turn, control1_turn + 0.1 )
            elif target1_turn < control1_turn:
                control1_turn = max( target1_turn, control1_turn - 0.1 )
            else:
                control1_turn = target1_turn

            # 创建并发布twist消息
            twist1 = Twist()
            twist1.linear.x = control_speed; 
            twist1.linear.y = 0; 
            twist1.linear.z = 0
            twist1.angular.x = 0; 
            twist1.angular.y = 0; 
            twist1.angular.z = control_turn
            pub.publish(twist1)

            twist2 = Twist()
            twist2.linear.x = control1_speed; 
            twist2.linear.y = 0; 
            twist2.linear.z = 0
            twist2.angular.x = 0; 
            twist2.angular.y = 0; 
            twist2.angular.z = control1_turn
            pub1.publish(twist2)


    finally:
        twist1 = Twist()
        twist1.linear.x = 0; twist1.linear.y = 0; twist1.linear.z = 0
        twist1.angular.x = 0; twist1.angular.y = 0; twist1.angular.z = 0
        pub.publish(twist1)

        twist2 = Twist()
        twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = 0
        twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
        pub1.publish(twist2)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)