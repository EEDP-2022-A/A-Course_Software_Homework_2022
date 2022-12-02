import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import calculate_coordinates as cc
import estimate_circumference as ec
import estimate_area as ea

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.
plt.show()

def test_generate_theta_uniform():
    # assert (cc.generate_theta_uniform(0) == [])
    assert(cc.generate_theta_uniform(1) == [360])
    assert(cc.generate_theta_uniform(2) == [180, 360])

def test_generate_theta_random():
    # assert (cc.generate_theta_uniform(0) == [])
    assert (len(cc.generate_theta_uniform(1)) == 1)
    assert (len(cc.generate_theta_uniform(2)) == 2)

def test_calc_distance():
    assert(ec.calc_distance(1, 180, 360) == 2)
    assert(ec.calc_distance(1, 0, 180) == 2)
    assert(ec.calc_distance(2, 0, 90) == np.sqrt(8*(1-np.cos(np.radians(90)))))
    assert(ec.calc_distance(3, 90, 185) == np.sqrt(18*(1-np.cos(np.radians(95)))))

def test_estimate_cir():
    thetas1 = cc.get_theta_array(4, 1)
    assert(ec.estimate_circ(1, thetas1) == 4*(np.sqrt(2*(1-np.cos(np.radians(90))))))
    thetas2 = cc.get_theta_array(2, 1)
    assert(ec.estimate_circ(1, thetas2) == 2*(np.sqrt(2*(1-np.cos(np.radians(180))))))

def test_estimate_area():
    thetas1 = cc.get_theta_array(4, 1)
    r1 = 1
    b1 = ec.calc_distance(1, thetas1[0], thetas1[1])
    h1 = np.sqrt(r1 ** 2 - (b1 / 2) ** 2)
    assert(ea.estimate_area(1, 4, 1) == (0.5)*4*b1*h1)

    thetas2 = cc.get_theta_array(3, 1)
    r2 = 1
    b2 = ec.calc_distance(1, thetas2[0], thetas2[1])
    h2 = np.sqrt(r2 ** 2 - (b2 / 2) ** 2)
    assert(round(ea.estimate_area(1, 3, 1), 5) == round(0.5*3*b2*h2, 5))

