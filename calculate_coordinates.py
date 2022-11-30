import numpy as np
import random


def generate_theta_uniform(n: int):
    theta = 0
    step = 360/n
    theta_array = []
    for _ in range(n):
        theta += step
        theta_array.append(theta)
    return theta_array


def generate_theta_random(n: int):
    theta_array = []
    for _ in range(n):
        theta_array.append(random.randint(0, 360))
    return theta_array


def calc_xy(radius, theta: list, x0, y0) -> tuple:
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return np.array((x+x0, y+y0)).reshape(-1, 2)


def return_xy_array(r, n, x0, y0, choice=1):

    if choice == 1:
        theta_array = generate_theta_uniform(n)
    elif choice == 2:
        theta_array = generate_theta_random(n)
    else:
        theta_array = [0]

    return calc_xy(r, theta_array, x0, y0)


if __name__ == '__main__':

    # inputs
    x0 = 0
    y0 = 0
    n = 20
    r = 2
    choice = 1

    xy_array = return_xy_array(r, n, x0, y0, choice)

