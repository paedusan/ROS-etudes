#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
var = Twist()
var.linear.x = 0
#count = Int32()
#count.data = 0

while not rospy.is_shutdown():
  pub.publish(var)
  var.linear.x += 0.1
  rate.sleep()