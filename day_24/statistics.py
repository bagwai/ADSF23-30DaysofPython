#30 Days of Python Programming
# Arewa Data Science Fellowship 
# Day 24

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

normal_array = np.random.normal(79, 15, 80)
normal_array
sns.set()
plt.hist(normal_array, color="grey", bins=50)


two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1

Z

new_list = [ x + 2 for x in range(0, 11)]

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
pressure

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()


mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()