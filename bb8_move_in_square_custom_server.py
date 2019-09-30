#! /usr/bin/env python

import rospy
#from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse # you import the service message python classes


rospy.init_node('bb8_move_in_square_service_server')
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


def cube(side):
    for s in range(4):
        move_straight(side)
        stop(5)
        turn(7)


def my_callback(request):
    i = 0
    while i <= request.repetitions:
        cube(request.side)
        i+=1

    response = BB8CustomServiceMessageResponse()
    response.success = True
    move.linear.x = 0.0
    move.angular.z = 0.0
    pub.publish(move)
    rate.sleep()
    return  response # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split()))



my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback) # create the Service called /move_bb8_in_circle with the defined callback
rospy.spin() # maintain the service open.   #        j+=1
