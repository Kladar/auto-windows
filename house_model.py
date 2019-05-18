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

    def time_stepper(self):

        self.timestep = self.timestep.add(minutes=1)

    def set_outdoor_temp(self):

        # use darksky method

    def set_indoor_temp(self):

        # define mathematical adjustment

    def set_weather(self):

        # use darksky method

    def set_window_state(self):

        if:



