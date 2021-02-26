#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool

class publish_carre:
	def __init__(self,dist,init_x=0,init_y=0):
		self.pub= rospy.Publisher('trajet_carre',PoseStamped, queue_size=10)
        	rospy.init_node('talker')
        	self.rate = rospy.Rate(15)
		self.distance = dist
        	self.x = init_x
		self.y = init_y
		self.go = False
        	
	def run(self):
	
		my_msg = PoseStamped()
                my_msg.header.frame_id = "map"
                my_msg.pose.position.x = self.x
		my_msg.pose.position.y = self.y
		
		sur_x = True
		compteur = 0
		i = 0
		vitesse = 1 # entre ]0;1]
		while not rospy.is_shutdown():
			
			
			if (compteur % 2 == 0):
				vitesse *= -1

			while (i < self.distance):
				if rospy.is_shutdown():
						break
					
				self.listener(Bool,'button_state')
				if (not self.go):
					continue
				self.mouvement_droit(sur_x,vitesse)
				my_msg.pose.position.x = self.x
				my_msg.pose.position.y = self.y
				self.pub.publish(my_msg)
				i += 1
				self.rate.sleep()
				
				
			else:
				i = 0
				sur_x = not sur_x
				compteur += 1
			

			

				
			

	def mouvement_droit(self,sur_x, distance):

		if(sur_x):
			
			self.x += distance
		else:
			self.y += distance


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
		talk = publish_carre(4)
		talk.run()
	except rospy.ROSInterruptException:
		pass
