import numpy as np
import random
from calculate_coordinates import get_theta_array


def calc_distance(r, theta1, theta2):
    return np.sqrt(2 * (r**2) * (1 - np.cos(np.radians(theta1) - np.radians(theta2))))


def estimate_circ(r, thetas: list):
    thetas = np.sort(thetas)
    estimated_circ = 0
    for i in range(len(thetas) - 1):
        estimated_circ += calc_distance(r, thetas[i], thetas[i+1])

    return estimated_circ


if __name__ == '__main__':

    # inputs
    x0 = 0
    y0 = 0
    n = 40
    r = 2
    choice = 2  # 1=uniform, 2=random

    theta_ar = get_theta_array(n, choice)
    estimate = estimate_circ(r, list(theta_ar))

    print(f'Estimated Circumference using {n} points: {estimate_circ(r, list(theta_ar))}')
    print(f'True Circumference = {2 * np.pi * r}')
