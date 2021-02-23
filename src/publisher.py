#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool

class publish_carre:
	def __init__(self,dist,x=0,y=0):
		self.pub= rospy.Publisher('trajet_carre',PoseStamped, queue_size=10)
        	rospy.init_node('talker')
        	self.rate = rospy.Rate(15)
		self.distance = dist
        	self.x = 0
		self.y = 0
		self.go = False
        	
	def run(self):
	
		my_msg = PoseStamped()
                my_msg.header.frame_id = "map"
                my_msg.pose.position.x = self.x
		my_msg.pose.position.y = self.y
		
		sur_x = True
		compteur = 0
		en_avant = True
		i = 0
		while not rospy.is_shutdown():
			
			
			if (compteur % 2 == 0 and self.go):
				en_avant = not en_avant	

			while (i < self.distance):
				if rospy.is_shutdown():
						break
					
				self.listener(Bool,'button_state')
				if (not self.go):
					break
				self.mouvement_droit(sur_x,en_avant,1)
				my_msg.pose.position.x = self.x
				my_msg.pose.position.y = self.y
				self.pub.publish(my_msg)
				self.rate.sleep()
				i += 1
				
			else:
				i = 0

						
			if (not self.go):
				continue		
			sur_x = not sur_x
			compteur += 1
			

			

				
			

	def mouvement_droit(self,sur_x, en_avant, distance):

		if(en_avant):		
			if(sur_x):
				self.x += distance
			else:
				self.y += distance
		else:
			if(sur_x):
				self.x -= distance
			else:
				self.y -= distance

	def callback(self,data):
		self.go = data.data
			

	def listener(self,type_msg,topic):	
		rospy.Subscriber(topic,type_msg,self.callback)
		









""" 
def talker_func():
	pub= rospy.Publisher('chatter',PoseStamped, queue_size=10)
	rospy.init_node('talker')
	rate = rospy.Rate(10)
	my_msg = PoseStamped()
	my_msg.header.frame_id = "map"
	teta = 0
	dt = 0.1
	while not rospy.is_shutdown():
		teta = teta + dt
		my_msg.pose.position.x = math.sin(teta)
		my_msg.pose.position.y = math.cos(teta)

		#print sur le terminal,log,rosout
		rospy.loginfo(my_msg)

		#publier sur le topic chatter
		pub.publish(my_msg)
		rate.sleep()
"""
if __name__ == '__main__':
	try:
		talk = publish_carre(5)
		talk.run()
	except rospy.ROSInterruptException:
		pass