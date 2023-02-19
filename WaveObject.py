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
    def __init__(self, x, y, radius, amplitud_list, frequency_list, speed_list):
        
        #Center point of circle
        self.cx = x
        self.cy = y

        #Radius of circle
        self.radius = radius

        #Amplitude of wave
        self.amplitudes = amplitud_list

        #Frequencys of the wave
        self.frequencys = frequency_list

        #Speed
        self.speeds = speed_list

        
    def get_amlification_at_angel(self, angle, time):
        """
        Converts angel and time to amplification at certain angel in time
        """

        amp_at_angel=0
        for ampl,freq, speed in zip(self.amplitudes, self.frequencys, self.speeds):
            amp_at_angel += self.radius+ampl*np.sin(freq*angle+time*speed)
        return amp_at_angel

    def raial_to_2d(self, angle, time=1):
        """
        Angel to cartitian point

        TODO: Make numpy
        """
        
        x = self.cx+self.get_amlification_at_angel(angle,time)*np.cos(angle)
        y = self.cy+self.get_amlification_at_angel(angle,time)*np.sin(angle)

        return x, y

    def plot_frequency_band(self,time=1):
        ax = plt.subplot()
        amp_list = []
        
        for i in range(1,365):
            angle = i * math.pi/180
            amp = self.get_amlification_at_angel(angle,time=time)
            amp_list.append(amp)

        line1, = ax.plot(range(1,365), amp_list)

        return amp_list#, fig, ax


    def plot_in_circel(self, time=1):
        fig, ax = plt.subplots()

        x_list = []
        y_list = []
        
        for i in range(1,365):
            angle = i * math.pi/180
            x, y = self.raial_to_2d(angle,time=time)
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


wo = waveobject(0, 0, 0.05/3, [0.005,0.020,0.001], [5, 2, 30], [0.1, 0.2, 0.3])
#wo.plot()
wo.plot_frequency_band()
plt.show()