import pandas as pd
import requests
import darksky
import pendulum


class HouseModel(object):
    def __init__(self):

        self.timestep = pendulum.parse(0)
        self.indoor_temp = 22
        self.outdoor_temp = 15
        self.weather = None


        self.furnace_condition = False #either on or off
        self.ac_condition = True # either on or off
        self.window_condition = 0 # gradient for 0, 0.5, 1

    def time_stepper(self):

        self.timestep = self.timestep.add(minutes=1)

    def set_outdoor_temp(self):

        # use darksky method

    def set_indoor_temp(self):

        if

    def set_weather(self):

        # use darksky method

    def set_window_state(self):

        if:



