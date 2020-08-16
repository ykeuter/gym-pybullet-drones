import os
import time
from datetime import datetime
import pdb
import math
import numpy as np
import pybullet as p
import pybullet_data
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import xml.etree.ElementTree as etxml

from gym_pybullet_drones.envs.SingleDroneEnv import DroneModel


######################################################################################################################################################
#### Multi drone environment class ###################################################################################################################
######################################################################################################################################################
class MultiDroneEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    ####################################################################################################
    #### TBD ###########################################################################################
    ####################################################################################################
    def __init__(self, drone_model=DroneModel.CF2X, gui=False):
        super(MultiDroneEnv, self).__init__()

    ####################################################################################################
    #### TBD ###########################################################################################
    ####################################################################################################
    def reset(self):
        pass

    ####################################################################################################
    #### TBD ###########################################################################################
    ####################################################################################################
    def step(self, action):
        pass

    ####################################################################################################
    #### TBD ###########################################################################################
    ####################################################################################################
    def render(self, mode='human', close=False):
        pass

    ####################################################################################################
    #### TBD ###########################################################################################
    ####################################################################################################
    def close(self):
        pass


######################################################################################################################################################
#### Internals #######################################################################################################################################
######################################################################################################################################################

    ####################################################################################################
    #### TBD ###########################################################################################
    ####################################################################################################
    def getPyBulletClient(self):
        pass

    ####################################################################################################
    #### TBD ###########################################################################################
    ####################################################################################################
    def getDroneIds(self):
        pass

    ####################################################################################################
    #### TBD ###########################################################################################
    ####################################################################################################
    def _housekeeping(self):
        pass

    ####################################################################################################
    #### TBD ###########################################################################################
    ####################################################################################################
    def _physics(self, forces, z_torque):
        pass
