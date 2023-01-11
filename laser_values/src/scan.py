#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
def callback(msg):
    #print '45 derece: '
    #print msg.ranges[45]
    #print '0 derece: '
    #print msg.ranges[0]
    #print '315 derece: '
    #print msg.ranges[315]
    
    dosya = open("/home/test/catkin_ws/src/laser_values/src/test.txt","w")
    #dosya.write(str(msg.ranges[0])+"\n")
    #dosya.write(str(msg.ranges[0])+"\n")
    #dosya.write(str(msg.ranges[315]))
    
    for i in range(45,0,-1):
        dosya.write(str(msg.ranges[i])+"\n")

    for i in range(359,315,-1):
        dosya.write(str(msg.ranges[i])+"\n")


rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
