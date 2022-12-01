import matplotlib.pyplot as plt
import numpy as np
from calculate_coordinates import get_xy_array

def plot_circle_points(r,n,x0,y0,choice):
    xy_array = get_xy_array(r, n, x0, y0, choice) #create xy array
    fig, ax = plt.subplots()
    ax.scatter(xy_array.reshape(2, -1)[0], xy_array.reshape(2, -1)[1]) #reshape
    plt.show()


if __name__ == '__main__':

    # inputs
    x0 = 0
    y0 = 0
    n = 40
    r = 1
    choice = 2  # 1=uniform, 2=random
    plot_circle_points(r,n,x0,y0,choice)




