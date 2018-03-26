import matplotlib.pyplot as plt
import numpy as np


class MohrCircles:
    def __init__(self):
        pass
    
    @staticmethod
    def draw(stress_tensor, planes=1000):
        for i in range(0, planes):
            r_v = np.random.random_integers(-10000, 10000, 3)
            _heta = r_v/np.sqrt(r_v.dot(r_v))
            t = _heta@stress_tensor
            t_n = np.dot(t, _heta)
            t_s = np.sqrt(np.dot(t, t) - t_n**2)
            plt.plot(t_n, t_s, 'y*')
            plt.plot(t_n, -t_s, 'y*')

        plt.xlabel('Componente normal')
        plt.ylabel('Componente tangencial')
        plt.title('Ciculos de Mohr')
        plt.show()
