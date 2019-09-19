#! /usr/bin/env python

import rospy
# Import the service message used by the service /gazebo/delete_model
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys

import rospkg
rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')
# Create the connection to the service
trajectory_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
# Create an object of type ExecTrajRequest()
trajectory_object = ExecTrajRequest()
# Fill the variable model_name of this object with the desired value
trajectory_object.file = traj
result = trajectory_service(trajectory_object)
print result

# LAUNCH FILE
#<launch>

#  <include file="$(find iri_wam_reproduce_trajectory)/launch/start_service.launch"/>


#  <node pkg ="unit_3_services"
#        type="exercise_3_1.py"
#        name="service_client"
#        output="screen">
#  </node>


#</launch>