#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "odometry_publisher");

  ros::NodeHandle n;
  ros::Publisher odom_pub = n.advertise<nav_msgs::Odometry>("odom", 50);
  tf::TransformBroadcaster odom_broadcaster;

  double x = 0.0;
  double y = 0.0;
  double th = 0.0;

  double vx = 0.1;
  double vy = -0.1;
  double vth = 0.1;

  ros::Time current_time, last_time;
  current_time = ros::Time::now();
  last_time = ros::Time::now();

  ros::Rate r(1.0);
  while(n.ok()){

    ros::spinOnce();               // check for incoming messages
    current_time = ros::Time::now();

    //compute odometry in a typical way given the velocities of the robot
    double dt = (current_time - last_time).toSec();
    double delta_x = (vx * cos(th) - vy * sin(th)) * dt;
    double delta_y = (vx * sin(th) + vy * cos(th)) * dt;
    double delta_th = vth * dt;

    x += delta_x;
    y += delta_y;
    th += delta_th;

    //since all odometry is 6DOF we'll need a quaternion created from yaw
    geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(th);

    //first, we'll publish the transform over tf
    geometry_msgs::TransformStamped odom_trans;
    odom_trans.header.stamp = current_time;
    odom_trans.header.frame_id = "odom";
    odom_trans.child_frame_id = "nao_1/base_link";

    odom_trans.transform.translation.x = x;
    odom_trans.transform.translation.y = y;
    odom_trans.transform.translation.z = 0.0;
    odom_trans.transform.rotation = odom_quat;

    //send the transform
    odom_broadcaster.sendTransform(odom_trans);

    //first, we'll publish the transform over tf
    geometry_msgs::TransformStamped odom_trans1;
    odom_trans1.header.stamp = current_time;
    odom_trans1.header.frame_id = "odom";
    odom_trans1.child_frame_id = "nao_2/base_link";

    odom_trans1.transform.translation.x = x;
    odom_trans1.transform.translation.y = y;
    odom_trans1.transform.translation.z = 0.0;
    odom_trans1.transform.rotation = odom_quat;

    //send the transform
    odom_broadcaster.sendTransform(odom_trans1);

    //next, we'll publish the odometry message over ROS
    nav_msgs::Odometry odom;
    odom.header.stamp = current_time;
    odom.header.frame_id = "odom";

    //set the position
    odom.pose.pose.position.x = x;
    odom.pose.pose.position.y = y;
    odom.pose.pose.position.z = 0.0;
    odom.pose.pose.orientation = odom_quat;

    //set the velocity
    odom.child_frame_id = "nao_1/base_link";
    odom.twist.twist.linear.x = vx;
    odom.twist.twist.linear.y = vy;
    odom.twist.twist.angular.z = vth;

    //publish the message
    odom_pub.publish(odom);

    //next, we'll publish the odometry message over ROS
    nav_msgs::Odometry odom1;
    odom1.header.stamp = current_time;
    odom1.header.frame_id = "odom";

    //set the position
    odom1.pose.pose.position.x = x;
    odom1.pose.pose.position.y = y;
    odom1.pose.pose.position.z = 0.0;
    odom1.pose.pose.orientation = odom_quat;

    //set the velocity
    odom1.child_frame_id = "nao_2/base_link";
    odom1.twist.twist.linear.x = vx;
    odom1.twist.twist.linear.y = vy;
    odom1.twist.twist.angular.z = vth;

    //publish the message
    odom_pub.publish(odom1);

    last_time = current_time;
    r.sleep();
  }
}