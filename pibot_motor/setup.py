# SPDX-FileCopyrightText: 2023 fabolhak
#
# SPDX-License-Identifier: MIT

from setuptools import setup

package_name = 'ros2_pibot_motor'

setup(
    name=package_name,
    version='0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Fa Dev',
    author_email='dev-faha@t-online.de',
    maintainer='Fa Dev',
    maintainer_email='dev-faha@t-online.de',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Motor driver of my little pibot.',
    license='Apache License, Version 2.0',
    entry_points={
        'console_scripts': [
            'service = ros2_pibot_motor.service:main'
        ],
    },
)
