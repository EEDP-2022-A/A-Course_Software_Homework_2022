import numpy as np
from calculate_coordinates import get_theta_array
from estimate_circumference import calc_distance

def estimate_area():
    #area of isocelese traingle is b*h/2 (h = pythag using r and distance between points)
    theta_ar = get_theta_array(n, choice)
    thetas = np.sort(thetas)
    estimated_circ = 0
    for i in range(len(thetas) - 1):
        estimated_circ += calc_distance(r, thetas[i], thetas[i + 1])

    return estimated_area

if __name__ == '__main__':
    # inputs
    x0 = 0
    y0 = 0
    n = 40
    r = 1
    choice = 2  # 1=uniform, 2=random

