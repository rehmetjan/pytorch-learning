from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def plot_data(data, title, x_label, y_label):
    plt.plot(data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


datax = np.random.rand(12)
datay = np.random.rand(12)
data = [datax, datay]
plot_data(datax, "HELLO", "x_label", "y_label")