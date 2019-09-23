#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

rospy.init_node('bb8_move_in_circle_service_server')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
move = Twist()

def my_callback(request):
    move.linear.x += 0.2
    move.angular.z += 0.2
    pub.publish(move)
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split()))


my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called /move_bb8_in_circle with the defined callback
rospy.spin() # maintain the service open.