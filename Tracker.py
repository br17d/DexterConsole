__title__ = "agvTrack.py"
__author__ = "Bryant Rodriguez"
__copyright__ = "Copyright (C) 2022, Bryant Rodriguez"
__license__ = "MIT License"
__version__ = "v0.7"
__email__ = "bryant1.rodriguez@famu.edu"
__status__ = "Prototype"

class Tracker():
    pass

class Controller():
    pass

class ViveTracker(Tracker):
    def __init__(self, name, vr):
        self.name = name
        self.vr = vr
        self.pose = self.vr.devices[self.name].get_pose_euler()
        self.pose_quaternion = self.vr.devices[self.name].get_pose_quaternion()
        self.pose_matrix = self.vr.devices[self.name].get_pose_matrix()
        self.pose_velocity = self.vr.devices[self.name].get_pose_velocity()
        self.pose_angular_velocity = self.vr.devices[self.name].get_pose_angular_velocity()
        self.pose_linear_acceleration = self.vr.devices[self.name].get_pose_linear_acceleration()
        self.pose_angular_acceleration = self.vr.devices[self.name].c
        self.pose_euler = self.vr.devices[self.name].get_pose_euler()
        self.pose_quaternion = self.vr.devices[self.name].get_pose_quaternion()
        self.pose_matrix = self.vr.devices[self.name].get_pose_matrix()
        self.pose_velocity = self.vr.devices[self.name].get_pose_velocity()
        self.pose_angular_velocity = self.vr.devices[self.name].get_pose_angular_velocity()
        self.pose_linear_acceleration = self.vr.devices[self.name].get_pose_linear_acceleration()
        self.pose_angular_acceleration = self.vr.devices[self.name].get_pose_angular_acceleration()
        self.pose_euler = self.vr.devices[self.name].get_pose_euler()
        self.pose_quaternion = self.vr.devices[self.name].get_pose_quaternion()

    def get_pose_euler(self):
        return self.pose_euler

