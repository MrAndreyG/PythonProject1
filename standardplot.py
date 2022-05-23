import matplotlib.pyplot as plt
import numpy as np
import hello as hlc


#x = np.linspace(50, 65, 100)  # Create a list of evenly-spaced numbers over the range
ArrayListofNumbers=[0,4,10,15,20]
x = np.linspace(ArrayListofNumbers, 65, 100)  # Create a list of evenly-spaced numbers over the range
#plt.plot(x, np.sin(x))        # Plot the sine of each x point
plt.plot(x)        # Plot the sine of each x point
plt.show()                    # Display the plot

print(hlc.msg);