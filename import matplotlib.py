import matplotlib.pyplot as plt
import numpy as np

i = np.array([[255,255,255],
              [0,255,0],[0,255,0]])   # Fíjate en los dobles corchetes

plt.imshow(i,vmin=0,vmax=255)
plt.show()
