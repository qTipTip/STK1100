import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import bernoulli, poisson, binom

a = np.arange(2)

# Bernoulli

colors = matplotlib.rcParams['axes.color_cycle']
plt.figure(figsize=(12,8))
for i, p in enumerate([0.1, 0.2, 0.6, 0.7]):
  ax = plt.subplot(1, 4, i+1)
  plt.bar(a, bernoulli.pmf(a, p), label=p, color=colors[i], alpha=0.5)
  ax.xaxis.set_ticks(a)

  plt.legend(loc=0)
  if i == 0:
    plt.ylabel("PDF at $k$")


plt.show()
plt.suptitle("Bernoulli probability")

# Poisson
k = np.arange(20)
colors = matplotlib.rcParams['axes.color_cycle'] 
plt.figure(figsize=(12,8))
for i, lambda_ in enumerate([1, 4, 6, 12]):
  plt.bar(k, poisson.pmf(k, lambda_), label=lambda_, color=colors[i], alpha=0.4, edgecolor=colors[i], lw=3)
  plt.legend()
plt.title("Poisson distribution")
plt.xlabel("$k$")
plt.ylabel("PDF at k")
plt.show()

# Poisson 2
k = np.arange(15)
plt.figure(figsize=(12,8))
for i, lambda_ in enumerate([1, 2, 4, 6]):
  plt.plot(k, poisson.pmf(k, lambda_), '-o', label=lambda_, color=colors[i])
  plt.fill_between(k, poisson.pmf(k, lambda_), color=colors[i], alpha=0.5)
  plt.legend()
plt.title("Poisson distribution")
plt.ylabel("PDF at $k$")
plt.xlabel("$k$")
plt.show()

# Binomial

plt.figure(figsize=(12,6))
k = np.arange(0, 22)
for p, color in zip([0.1, 0.3, 0.6, 0.8], colors):
  rv = binom(20, p)
  plt.plot(k, rv.pmf(k), lw=2, color=color, label=p)
  plt.fill_between(k, rv.pmf(k), color=color, alpha=0.5)
  plt.legend()
plt.title("Binomial distribution")
plt.tight_layout()
plt.ylabel("PDF at $k$")
plt.xlabel("$k$")
plt.show()

# Alpha


x = np.linspace(0.1, 2, 100)
alpha = scipy.stats.alpha
alphas = [0.5, 1, 2, 4]
plt.figure(figsize=(12,6))
for a,c in zip(alphas,colors):
  label=r"$\alpha$ = {0:.1f}".format(a)
  plt.plot(x, alpha.pdf(x, a), lw=2, 
  color=c, label=label)
  plt.fill_between(x, alpha.pdf(x, a), color=c, alpha = .33)
plt.ylabel("PDF at $x$")
plt.xlabel("$x$")
plt.title("Alpha distribution")
plt.legend()
plt.show()

# Beta


beta = scipy.stats.beta
x = np.linspace(0,1, num=200)


fig = plt.figure(figsize=(12,6))
for a, b, c in zip([0.5, 0.5, 1, 2, 3], [0.5, 1, 3, 2, 5], colors):
  plt.plot(x, beta.pdf(x, a, b), lw=2, 
  c=c, label = r"$\alpha = {0:.1f}, \beta={1:.1f}$".format(a, b))
  plt.fill_between(x, beta.pdf(x, a, b), color=c, alpha = .1)


plt.legend(loc=0)
plt.ylabel("PDF at $x$")
plt.xlabel("$x$")
plt.show()

# Gamma

gamma = scipy.stats.gamma
plt.figure(figsize=(12, 6))
x = np.linspace(0, 10, num=200)
for a, c in zip([0.5, 1, 2, 3, 10], colors):
  plt.plot(x, gamma.pdf(x, a), lw=2, 
  c=c, label = r"$\alpha = {0:.1f}$".format(a))
  plt.fill_between(x, gamma.pdf(x, a), color=c, alpha = .1)
plt.legend(loc=0)
plt.title("Gamma distribution with scale=1")
plt.ylabel("PDF at $x$")
plt.xlabel("$x$")
plt.show()

# Exponential


x = np.linspace(0,4, 100)
expo = scipy.stats.expon
lambda_ = [0.5, 1, 2, 4]
plt.figure(figsize=(12,4))
for l,c in zip(lambda_,colors):
  plt.plot(x, expo.pdf(x, scale=1./l), lw=2, 
  color=c, label = "$\lambda = %.1f$"%l)
  plt.fill_between(x, expo.pdf(x, scale=1./l), color=c, alpha = .33)

plt.legend()
plt.ylabel("PDF at $x$")
plt.xlabel("$x$")
plt.title("Probability density function of an Exponential random variable;\
differing $\lambda$");
plt.show()
