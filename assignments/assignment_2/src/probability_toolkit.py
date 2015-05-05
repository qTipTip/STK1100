import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

class ProbabilityToolKit:

  def __init__(self, number_of_trials):
    self.N = number_of_trials

  def uniform(self, n):
    observations = np.zeros((self.N, n))
    for i in range(self.N):
      observations[i] = np.random.uniform(0, 1, n)
    return observations

  def exponential(self, n, scale_param = 1):
    observations = np.zeros((self.N, n))
    for i in range(self.N):
      observations[i] = np.random.exponential(scale_param, n)
    return observations

  def bernoulli(self, n):
    #TODO
    pass

  def mean(self, observations):
    mean = np.zeros(len(observations))
    for i, trial in enumerate(observations):
      mean[i] = sum(trial)/float(len(trial))
    return mean

  def standarized_mean(self, n, mu, sigma, mean):
    Z = np.zeros(len(mean))
    for i, trial in enumerate(mean):
      Z[i] = sqrt(n) * (mean[i] - mu)/float(sigma)
    return Z

  def visualize(self, array, bin_size=0.25, title="Test", x_label="x", y_label="y"):
    plt.hist(array, bins=np.arange(min(array), max(array) + bin_size, bin_size))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
if __name__ == '__main__':

  test = ProbabilityToolKit(10000)
  test_values = test.standarized_mean(100, 1, 1, test.mean(test.uniform(100)))
  test.visualize(test_values)
  test.visualize(test.mean(test.uniform(100)))


