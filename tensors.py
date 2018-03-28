import numpy as np


class Tensors:

    @staticmethod
    def get_first_invariant(tensor):
        result = None
        result = np.trace(tensor)

        return result

    @staticmethod
    def get_second_invariant(tensor):
        result = 0.0

        for i in range(3):
            for j in range(3):
                result += (
                    tensor[i, i]*tensor[j, j] - tensor[i, j]*tensor[j, i]
                )

        return result/2

    @staticmethod
    def get_third_invariant(tensor):
        result = 0.0
        result = np.linalg.det(tensor)

        return result

    @staticmethod
    def principal_stresses(tensor):
        coeff = [
            1,
            -Tensors.get_first_invariant(tensor),
            Tensors.get_second_invariant(tensor),
            -Tensors.get_third_invariant(tensor)
        ]

        sol = np.roots(coeff)

        return sol

    @staticmethod
    def principal_directions(tensor):
        eigenvect = np.linalg.eig(tensor)[0]

        return eigenvect
