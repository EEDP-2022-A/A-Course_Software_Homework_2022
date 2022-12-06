import matplotlib.pyplot as plt
import numpy as np
from calculate_coordinates import get_xy_array

def plot_circle_points(r,n,x0,y0,choice,title):
    xy_array = get_xy_array(r, n, x0, y0, choice) #create xy array
    fig, ax = plt.subplots()
    ax.scatter(xy_array.reshape(2, -1)[0], xy_array.reshape(2, -1)[1], marker="x",color='green') #reshape
    plt.title(title,fontdict={'family':'serif',
                              'color':'pink',
                              'weight':'bold',
                              'size': 20,
    })
    plt.xlabel("X Coordinates", fontdict={'family':'serif',
                              'color':'purple',
                              'weight':'bold',
                              'size': 12,
    })
    plt.ylabel("Y Coordinates", fontdict={'family':'serif',
                              'color':'purple',
                              'weight':'bold',
                              'size': 12,
    })
    ax.axis('equal') # formatting axes to be equally scaled
    plt.show()



if __name__ == '__main__':

    # inputs
    x0 = 0
    y0 = 0
    n = 40
    r = 1
    title = "Plot of Circle"
    choice = 2  # 1=uniform, 2=random
    plot_circle_points(r,n,x0,y0,choice,title)




