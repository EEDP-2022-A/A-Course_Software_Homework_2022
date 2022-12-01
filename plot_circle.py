import matplotlib.pyplot as plt
import numpy as np
import calculate_coordinates

def plot_circle_points(xy_array):
    fig, ax = plt.subplots()
    ax.scatter(xy_array.reshape(2, -1)[0], xy_array.reshape(2, -1)[1])
    plt.show()


if __name__ == '__main__':

    # inputs
    x0 = 0
    y0 = 0
    n = 40
    r = 1
    choice = 2  # 1=uniform, 2=random

    xy_array = calculate_coordinates.get_xy_array(r, n, x0, y0, choice)   # Returns array of x, y points -> [[x0, y0], [x1, y1], ... [xn, yn]]
    #theta_array = get_theta_array(n, choice)    # Returns list array of angles
    plot_circle_points(xy_array)




