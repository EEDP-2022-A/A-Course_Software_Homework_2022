import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import calculate_coordinates as cc
import estimate_circumference as ec

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.
# plt.show()


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
    thetas = cc.get_theta_array(4, 1)
    assert(ec.estimate_circ(1, thetas) == 4*(np.sqrt(2*(1-np.cos(np.radians(90))))))
