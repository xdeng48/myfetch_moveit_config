#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)


group_variable_values = group.get_current_joint_values()
group_variable_values[5] = -1.5
group.set_joint_value_target(group_variable_values)

plan = group.plan()

rospy.sleep(5)
group.go(wait=True)

# Do at least two motions

group_variable_values[3] = 1.0
group_variable_values[5] = 0.0
group.set_joint_value_target(group_variable_values)
plan = group.plan()
group.go(wait=True)

group_variable_values = [-0.75, -0.7675, 0.0174, 1.9188, -0.64544, -1.67466, -0.13955]
group.set_joint_value_target(group_variable_values)
plan = group.plan()
group.go(wait=True)


moveit_commander.roscpp_shutdown()




