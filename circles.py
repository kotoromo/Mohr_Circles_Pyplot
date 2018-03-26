import matplotlib.pyplot as plt
import numpy as np
import time


class MohrCircles:
    def __init__(self):
        pass
    
    @staticmethod
    def draw(stress_tensor, planes=1000):
        start = time.time()

        for i in range(0, planes):
            r_v = np.random.random_integers(-10000, 10000, 3)
            _heta = r_v/np.sqrt(r_v.dot(r_v))
            t = MohrCircles.gen_stress_vector(stress_tensor, _heta)
            t_n = np.dot(t, _heta)
            t_s = np.sqrt(np.dot(t, t) - t_n**2)
            plt.plot(t_n, t_s, 'y*')
            plt.plot(t_n, -t_s, 'y*')

        end = time.time()
        print("Time > {}".format(start-end)) # 6 seconds

        plt.xlabel('Componente normal')
        plt.ylabel('Componente tangencial')
        plt.title('Ciculos de Mohr')
        plt.show()
    
    @staticmethod
    def gen_stress_vector(stress_tensor, plane):
        t_heta = np.array([0.0, 0.0, 0.0])
        for i in range(3):
            for j in range(3):
                t_heta[i] += stress_tensor[i, j]*plane[j]
        return t_heta

stress = np.array(
    [
        [1, 1, 0],
        [1, 2, 4],
        [0, 4, 2]
    ]
)

plane = np.array([
    1/np.sqrt(2), 1/np.sqrt(2), 0
])

MohrCircles.draw(stress)