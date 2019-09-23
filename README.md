# PiBot Motor Driver

This package contains the motor driver for my pibot. It is made for the [CamJam EduKit 3](https://camjam.me/?page_id=1035). To control the motors the [Raspberry Pi Gpio python packge](https://pypi.org/project/RPi.GPIO/) is being used. [ROS2](https://index.ros.org/doc/ros2/) as middleware is being used to communicate with the robot.

## Install

The package can be installed as [snap](https://snapcraft.io/ros2-pibot-motor-fabolhak):

```bash
snap install ros2-pibot-motor-fabolhak
```

## Usage

Snaps need [interfaces](https://snapcraft.io/docs/interface-management) in order to access ressources from outside. The following interfaces are mounted automatically:

```bash
$ snap connections
Interface            Plug                                           Slot                  Notes
network              ros2-pibot-motor-fabolhak:network              :network              -
network-bind         ros2-pibot-motor-fabolhak:network-bind         :network-bind         -

```

Both `network` and `network-bind` are required to communicate via the ROS2 (DDS) middleware with other software parts.

This package needs two additional connections in order to access the hardware GPIO. These must be manually connected via the following commands:

```bash
snap connect ros2-pibot-motor-fabolhak:hardware-observe :hardware-observe
snap connect ros2-pibot-motor-fabolhak:gpio-memory-control :gpio-memory-control
```

To start the ROS2 node run the following command:

```bash
sudo ros2-pibot-motor-fabolhak.run
```

You now can trigger the robot from an external computer within the same network:

```bash
ros2 service call /triggerMotor std_srvs/Trigger
```
