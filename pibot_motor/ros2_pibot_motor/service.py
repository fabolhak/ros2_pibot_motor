# Copyright 2016 Open Source Robotics Foundation, Inc.
# SPDX-FileCopyrightText: 2016 Open Source Robotics Foundation, Inc.
#
# SPDX-License-Identifier: Apache-2.0

from std_srvs.srv import Trigger
import rclpy
import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library


g_node = None


def triggerMotor(request, response):
    global g_node

    g_node.get_logger().info('Trigger Motor!')

    # Turn the right motor forwards
    GPIO.output(9, 0)
    GPIO.output(10, 1)

    # Turn the left motor forwards
    GPIO.output(7, 0)
    GPIO.output(8, 1)
    # Wait for 1 seconds
    time.sleep(1)

    # Turn all motors off
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(9, 0)
    GPIO.output(10, 0)

    response.success = True
    response.message = "Sucess!"

    return response


def main(args=None):
    global g_node
    rclpy.init(args=args)

    # Set the GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Set the GPIO Pin mode
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    # Turn all motors off
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(9, 0)
    GPIO.output(10, 0)

    g_node = rclpy.create_node('motor')

    srv = g_node.create_service(Trigger, 'triggerMotor', triggerMotor)
    while rclpy.ok():
        rclpy.spin_once(g_node)

    # Reset the GPIO pins (turns off motors too)
    GPIO.cleanup()

    # Destroy the service attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    g_node.destroy_service(srv)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
