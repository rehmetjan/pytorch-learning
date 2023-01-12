import dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
xs, ys = dataset.get_beans(100)
print(xs)
print(ys)

plt.title('Size-Toxicity Analysis', fontsize=12)
plt.xlabel('Bean size')
plt.ylabel('Toxicity')
# Plot data
plt.scatter(xs, ys)
w = 0.5
for m in range(10):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        y_pre = w * x
        e = y - y_pre
        alpha = 0.05
        w = w + alpha * e * x
        print("now w is {}".format(w))
        plt.plot(x, y, color="green")

print("final w is {}".format(w))
y_pre = w * xs
print(y_pre)
plt.plot(xs, y_pre, color='red')

plt.show()
