#! /usr/bin/env python
import rospkg
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest # you import the service message python classes

rospy.init_node('service_move_bb8_in_square_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_square_custom') # Wait for the service client /move_bb8_in_square_custom to be running
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage) # Create the connection to the service
move_bb8_in_square_request_object = BB8CustomServiceMessageRequest() # Create an object of type EmptyRequest

# move in a small square twice
move_bb8_in_square_request_object.side = 5
move_bb8_in_square_request_object.repetitions = 1

# move in a small square once
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object) # Send through the connection the path to the trajectory file to be executed

move_bb8_in_square_request_object.side = 10
move_bb8_in_square_request_object.repetitions = 0

result = move_bb8_in_square_service_client(move_bb8_in_square_request_object)

print result # Print the result given by the service called