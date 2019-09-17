#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

# initializa note
rospy.init_node('topics_quiz_node')

# create object publisher on cmd_vel
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
move = Twist()

def callback(msg):
    pub.publish(move)
    #rate.sleep()
    if (msg.ranges[360] > 2):
        #move forward
        move.linear.x += 0.01
        move.angular.z += 0.0
    else:
        #avoid wall
        move.linear.x += 0.0
        move.angular.z += 0.01


# create object subscriber on LaserScan
sub = rospy.Subscriber('/kobuki/laser/scan',LaserScan, callback)


rospy.spin()