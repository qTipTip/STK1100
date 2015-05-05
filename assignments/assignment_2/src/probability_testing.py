import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform 

print uniform.rvs(loc=0, scale = 1, size=10)
print uniform.stats(moments='mvsk')

print uniform.rvs(size=1000)
