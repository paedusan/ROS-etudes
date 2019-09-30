#! /usr/bin/env python

import rospy
#from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse # you import the service message python classes
                                                                                         # generated from MyCustomServiceMessage.srv.


rospy.init_node('bb8_move_in_circle_service_server')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
move = Twist()
move.linear.x = 0.0
move.angular.z = 0.0
pub.publish(move)
rate.sleep()

def move_straight(time):
    i=0
    # move in a straghtline for time units
    while i < time:
        move.linear.x = 0.2
        move.angular.z = 0.0
        pub.publish(move)
        rate.sleep()
        i+=1
    move.linear.x = 0.0
    pub.publish(move)
    rate.sleep()

def stop(time):
    i=0
    # move in a straghtline for time units
    while i < time:
        move.linear.x = 0.0
        move.angular.z = 0.0
        pub.publish(move)
        rate.sleep()
        i+=1

def turn(time):
    i=0
    # turn for time units
    while i < time:
        move.linear.x = 0.0
        move.angular.z = 0.2
        pub.publish(move)
        rate.sleep()
        i+=1


def my_callback(request):
    for side in range(4):
        move_straight(10.5)
        stop(5)
        turn(7)

    #while i <= request.duration:
    #    i+=1
    #    j = 0
    #    while j < 5:
    #        move.linear.x += 0.2
    #        move.angular.z += 0.0
    #        pub.publish(move)
    #        rate.sleep()

    response = MyCustomServiceMessageResponse()
    response.success = True
    move.linear.x = 0.0
    move.angular.z = 0.0
    pub.publish(move)
    rate.sleep()
    return  response # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split()))



my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) # create the Service called /move_bb8_in_circle with the defined callback
rospy.spin() # maintain the service open.   #        j+=1
