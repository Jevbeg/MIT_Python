# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:19:32 2020

@author: Lietotajs
"""
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
#set starting temerature
init_temp = 40

# Initialize communication with TMP102
#tmp102.init()

def read_temp(old_temp):
    
    new_temp = old_temp + randint(-5, 5)
    
    return new_temp
    



# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    temp_c = read_temp(init_temp)
    
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=90, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')
    plt.ylim(0, 50)
# Set up plot to call animate() function periodically

# while True:
#     try:
#         for i in range(100):
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
    
    # except KeyboardInterrupt:
    #     break
        
        
        
        
        