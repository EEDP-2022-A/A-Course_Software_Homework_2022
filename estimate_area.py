import numpy as np
from calculate_coordinates import get_theta_array
from estimate_circumference import calc_distance

def estimate_area(r,n,choice):
    #area of isocelese traingle is b*h/2 (h = pythag using r and distance between points)
    theta_ar = get_theta_array(n, choice)
    thetas = list(theta_ar)
    thetas = np.sort(thetas)
    estimated_area = 0
    for i in range(len(thetas) - 1):
        b = calc_distance(r, thetas[i], thetas[i + 1])
        h = np.sqrt(r**2 - (b/2)**2)
        estimated_area += b*h/2

    last_el = len(thetas) - 1
    b_last = calc_distance(r, thetas[last_el], thetas[0])
    h_last = np.sqrt(r**2 - (b_last/2)**2)
    estimated_area += b_last*h_last/2

    return estimated_area

if __name__ == '__main__':
    # inputs
    x0 = 0
    y0 = 0
    n = 1000
    r = 1
    choice = 2  # 1=uniform, 2=random

    area_est = estimate_area(r,n,choice)

    print(f'Estimated Area using {n} points: {estimate_area(r,n,choice)}')
    print(f'True Area: {np.pi*r**2}')

