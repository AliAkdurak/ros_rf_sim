#!/usr/bin/env python

import rospy


def start_server():
    rospy.init_node("rf_trilateration_service")
    rospy.spin()

if __name__ == "__main__":
    start_server()