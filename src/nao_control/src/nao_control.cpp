#include <moveit/move_group_interface/move_group_interface.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "nao_control", ros::init_options::AnonymousName);
  // create a spinning thread
  ros::AsyncSpinner spinner(1);
  spinner.start();
  // connect to a group
  moveit::planning_interface::MoveGroupInterface group1("LeftArm");
  // set a random target
  group1.setRandomTarget();
  //geometry_msgs::Pose target_pose;
  // target_pose.orientation.w = 0.726282;
  // target_pose.orientation.x= 4.04423e-07;
  // target_pose.orientation.y = -0.687396;
  // target_pose.orientation.z = 4.81813e-07;

  // target_pose.position.x = 0.0;
  // target_pose.position.y = 0.0;
  // target_pose.position.z = 0.0;
  // group.setPoseTarget(target_pose);
  // start to plan and move
  group1.move();

}