import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

        
    def sineAroundCircle(self, angle, time=1):
        """
        Angel to cartitian point

        TODO: Make numpy
        """
        x = self.cx+(self.radius+self.amplitude*np.sin(self.frequency*angle+time))*np.cos(angle)
        y = self.cy+(self.radius+self.amplitude*np.sin(self.frequency*angle+time))*np.sin(angle)

        return x, y

    def plot(self, time=1):
        fig, ax = plt.subplots()

        x_list = []
        y_list = []
        
        for i in range(1,365):
            angle = i * math.pi/180
            x, y = wo.sineAroundCircle(angle,time=time)
            x_list.append(x)
            y_list.append(y)

        line1, = ax.plot(x_list, y_list)

        return x_list, y_list#, fig, ax

    def animate(self):
        fig, ax = plt.subplots()
        line, = ax.plot([], [])

        def update(t):
            x, y = self.plot(time=t)
            x = np.array(x)
            y = np.array(y)
            line.set_data(x, y)
            return line,

        anim = FuncAnimation(fig, update, frames=np.arange(0, 365, 1), interval=50, blit=True)
        return anim


wo = waveobject(0, 0, 0.05, 0.005, 5)
#wo.plot()
anim = wo.animate()
anim.save('animation.mp4')
