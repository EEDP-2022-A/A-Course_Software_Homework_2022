# ask user for inputs

import time
#from reader import feed
from get_user_input import get_circle_inputs, print_inputs, check_satisfaction
from estimate_circumference import estimate_circ
from estimate_area import estimate_area
from plot_circle import plot_circle_points
import numpy as np


def main():
    # Obtaining User Inputs
    tic_user_inputs = time.perf_counter()
    while True:
        x0, y0, r, n, choice = get_circle_inputs() # ask user for inputs
        print_inputs(x0, y0, r, n, choice)  # print out values
        if check_satisfaction(): # repeat entries if desired
            break
        continue
    toc_user_inputs = time.perf_counter()
    t_user = (toc_user_inputs - tic_user_inputs)
    if t_user > 30:
        print(f"Wow, you took forever choosing inputs! A whole {t_user:0.2f} seconds--that's more than half a minute!")
    else:
        print(f"Wow, you chose those values quick! Did you even think about what you were entering? It only took you {t_user:0.2f} seconds!")
    title = "A Circle" # choose title for plot
    plot_circle_points(r,n,x0,y0,choice, title) # plotting circle

    # Estimate circle circumference using numerical methods
    tic_circ = time.perf_counter()
    estimate_circ(r,n,choice)
    toc_circ = time.perf_counter()
    t_calc = (toc_circ - tic_circ) * 10 ** 6
    print(f"Circumference approximated in {t_calc:0.4f} microseconds")

    # Calculate actual circle circumference
    tic_circ = time.perf_counter()
    c = np.pi*2*r
    toc_circ = time.perf_counter()
    t_calc = (toc_circ - tic_circ)*10**6
    print(f"Actual circumference calculated in {t_calc:0.4f} microseconds")

    # Estimate circle circumference using numerical methods
    tic_area = time.perf_counter()
    estimate_area(r,n,choice)
    toc_area = time.perf_counter()
    t_calc = (toc_area - tic_area)*10**6
    print(f"Area approximated in {t_calc:0.4f} microseconds")

    # Calculate actual circl area
    tic_area = time.perf_counter()
    a = np.pi*r**2
    toc_area = time.perf_counter()
    t_calc = (toc_area - tic_area) * 10 ** 6
    print(f"Actual area calculated in {t_calc:0.4f} microseconds")

if __name__ == '__main__':
    main()