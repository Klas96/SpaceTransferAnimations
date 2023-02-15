import numpy as np
from matplotlib import pyplot as plt 
"""
Lite grejs me tid o rum

Closed objects going thrugh time

colors difusing over time...


Mapps a space with n+k dimesnions and mapps it on a n dimensional object thrugh the k dimensions as time dimensions

The object draws a line thrugh a space and projects its constrained dimension on time dimensions
"""

# Är vi ett 3 dimitionelt rum som rör oss i tid?
# rum tid?

class WaveObject:
    """ Wave Object """

    def __init__(self, amplitudes, offsets, frequenzies) -> None:
        
        mass = 0
        speed = 0
        color = 0

        # Have to be equal lengths
        self.amplitudes = amplitudes
        self.offsets = offsets
        self.frequenzies = frequenzies


    """
    def get_wave_state(self, time, radius):
        Agreagte the vaves at position x
        return: agregate_wave         
        
        agregate_wave = 0

        for amplitude, frequenzies, offset in zip(self.amplitudes, self.frequenzies, self.offsets):
            agregate_wave += radius*np.sin(frequenzies*time) + offset

        return agregate_wave
    """


class NDimentionalSpaceObject:
    """ N Dimensional Space Object """

    number_of_dimensions = 2


#inner circel
class inner:
    """
    Inner Circel
    """

    def plot_inner():
        """
        Plots object
        """


    def find_if_inner(x,y):
        """
        Returns boolean
        """

# Integration

# Outer circel
class outer:
    """
    Outer circel
    """

class OuterVoid:
    """
    Outer Void
    """
    

def map_between_wave_to_2D_space(wave_obj, space_x_cord, space_y_cord, time):
    """
    Maps wave object to 2D object thrugh time

    Calculates the distance between the wave object to the space object thrugh time? 

    return: TRUE / FALSE
    """

    #That is all waves that are pointing in this direction at this momenmt 
    wave_to_x_cord_1 = 0
    wave_to_x_cord_2 = 0

    wave_to_y_cord_1 = 0
    wave_to_y_cord_2 = 0

    
    for amplitude, frequenzies, offset in zip(wave_obj.amplitudes, wave_obj.frequenzies, wave_obj.offsets):
        #breakpoint()
        wave_to_x_cord_1 += amplitude*np.cos(frequenzies*time)
        wave_to_x_cord_2 += -amplitude*np.cos(frequenzies*time)

        wave_to_y_cord_1 += amplitude*np.sin(frequenzies*time)
        wave_to_y_cord_2 += amplitude*np.sin(np.pi-frequenzies*time)


    x_interior = False
    if wave_to_x_cord_1 < wave_to_x_cord_2:
        if wave_to_x_cord_1 < space_x_cord and space_x_cord < wave_to_x_cord_2: 
            x_interior = True
    else:
        if wave_to_x_cord_1 > space_x_cord and space_x_cord > wave_to_x_cord_2: 
            x_interior = True

    y_interior = False
    if wave_to_y_cord_1 < wave_to_y_cord_2:
        if wave_to_y_cord_1 < space_y_cord and space_y_cord < wave_to_y_cord_2: 
            y_interior = True
    else:
        if wave_to_y_cord_1 > space_y_cord and space_y_cord > wave_to_y_cord_2: 
            y_interior = True
    
    print(f"x:{x} y:{y} xi1:{wave_to_x_cord_1} yi2: {wave_to_x_cord_2}")
    print(f"boolean: {y_interior and x_interior}")
    if y_interior and x_interior:
        #breakpoint()
        pass
    
    return y_interior and x_interior


if __name__ == "__main__":
    amplitudes = [1]
    offsets = [0]
    frequenzies = [1]
    wave_object = WaveObject(amplitudes, offsets, frequenzies)
    time = 1

    #map = np.zeros((100,100))
    map = []
    
    #TODO loop thrugh time ass well
    for y in np.linspace(-2, 2, 100):
        x_row = []
        for x in np.linspace(-2, 2, 100):
            x_row.append(
                map_between_wave_to_2D_space(wave_object, x, y, time)
            )
        map.append(x_row)
    
    #print(map)
    plt.imshow(map)
    plt.show()
    plt.savefig("wave_object.png")

