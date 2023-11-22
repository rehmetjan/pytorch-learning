"""using python"""
import numpy as np
import matplotlib.pyplot as plt

# Load data
# xs, ys = lesson.dataset.get_beans(100)

# get beans method
def get_beans(counts):
    """method using get beans"""
    Xs = np.random.rand(counts)
    # Xs = np.sort(Xs)
    Ys = [1.7 * x + np.random.rand() / 5 for x in Xs]
    # Ys = [1.2 * x + np.random.rand() / 10 for x in Xs]
    # Ys = np.random.rand(counts)
    return Xs, Ys


xs, ys = get_beans(100)
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
