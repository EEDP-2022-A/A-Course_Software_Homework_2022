# ask user for inputs

import time
#from reader import feed
from get_user_input import get_circle_inputs
from estimate_circumference import estimate_circ
from estimate_area import estimate_area
from plot_circle import plot_circle_points
import numpy as np


def main():
    x0, y0, r, n, choice = get_circle_inputs()
    plot_circle_points(r,n,x0,y0,choice)

    tic_circ = time.perf_counter()
    estimate_circ(r,n,choice)
    toc_circ = time.perf_counter()
    t_calc = (toc_circ - tic_circ) * 10 ** 6
    print(f"Circumference approximated in {t_calc:0.4f} microseconds")

    tic_circ = time.perf_counter()
    c = np.pi*2*r
    toc_circ = time.perf_counter()
    t_calc = (toc_circ - tic_circ)*10**6
    print(f"Actual circumference calculated in {t_calc:0.4f} microseconds")

    tic_area = time.perf_counter()
    estimate_area(r,n,choice)
    toc_area = time.perf_counter()
    t_calc = (toc_area - tic_area)*10**6
    print(f"Area approximated in {t_calc:0.4f} microseconds")

    tic_area = time.perf_counter()
    a = np.pi*r**2
    toc_area = time.perf_counter()
    t_calc = (toc_area - tic_area) * 10 ** 6
    print(f"Actual area calculated in {t_calc:0.4f} microseconds")

if __name__ == '__main__':
    main()