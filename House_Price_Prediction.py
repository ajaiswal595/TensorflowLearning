# This is a very simple prediction of house prices based on house size. implemented
# in Tensorflow.


import tensorflow as  tf 
import numpy as np 
import math 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation # import animation support

# generate  some house sizes between 1000 and 3500 (typically sq ft of house)

num_house=160
np.random.seed(42)
house_size =  np.random.randint(low=1000, high=3500, size=num_house);

#Generate house prices from house size with  a random noise added.

np.random.seed(42)
house_price = house_size * 100.0 + np.random.randint(low=20000,high=70000,size=num_house)

#plot generated house and size
plt.plot(house_size,house_price,"bx") # bx = blue x
plt.ylabel("Price")
plt.xlabel("Size")
plt.show()