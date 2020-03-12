#!/usr/bin/env python

import serial
import rospy
from geometry_msgs.msg import Wrench

class simpleForceSensor():
  def __init__(self):
    rospy.init_node('simpleForceSensor')

    port = rospy.get_param('~port', '/dev/ttyUSB0')
    baud = rospy.get_param('~baud', 115200)

    self.publ = rospy.Publisher('force', Wrench, queue_size=10)
    self.srl = serial.Serial(port=port, baudrate=baud, timeout=1.0)

  def run(self):
    while not rospy.is_shutdown():
      line = self.srl.readline()
      if len(line) > 0:
        w = Wrench()
        w.force.x = float(line)
        self.publ.publish(w)
        
if __name__ == "__main__":
  simpleForceSensor().run()

#eof
