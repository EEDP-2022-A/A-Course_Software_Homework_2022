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
    return x+x0, y+y0


if __name__ == '__main__':

    # inputs
    x0 = 0
    y0 = 0
    n = 20
    r = 2
    choice = 1

    if choice == 1:
        thetas = generate_theta_uniform(n)
    elif choice == 2:
        thetas = generate_theta_random(n)

    print(calc_xy(r, thetas, x0, y0))


