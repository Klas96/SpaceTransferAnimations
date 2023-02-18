import numpy as np
import math
import matplotlib.pyplot as plt

"""
Closed objects going thrugh time

colors difusing over time...

Mapps a space with n+k dimesnions and mapps it on a n dimensional object thrugh the k dimensions as time dimensions

The object draws a line thrugh a space and projects its constrained dimension on time dimensions
"""

class waveobject:
    """
    Wave form object
    """
    def __init__(self, x, y, radius, amp, frequency):
        
        #Center point of circle
        self.cx = x
        self.cy = y

        #Radius of circle
        self.radius = radius

        #Amplitude of wave
        self.amplitude = amp

        #Frequency of the wave
        self.frequency = frequency

        
    def sineAroundCircle(self, angle):
        """
        Angel to cartitian point

        TODO: Make numpy
        """
        x = self.cx+(self.radius+self.amplitude*np.sin(self.frequency*angle))*np.cos(angle)
        y = self.cy+(self.radius+self.amplitude*np.sin(self.frequency*angle))*np.sin(angle)
        return x, y

    def plot(self):
        fig, ax = plt.subplots()

        for i in range(1,360):
            angle = i * math.pi/180
            x, y = wo.sineAroundCircle(angle)
            line1, = ax.plot(x, y, 'x')
        return fig, ax


wo = waveobject(0, 0, 100, 30, 8)

fig = wo.plot()

plt.show()