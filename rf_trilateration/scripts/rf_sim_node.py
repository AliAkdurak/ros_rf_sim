#!/usr/bin/env python

import rospy


def start_node():
    rospy.init_node("rf_node", anonymous=True)
    rospy.loginfo("Testing logging")
    rospy.spin()

if __name__ == "__main__":
    start_node()