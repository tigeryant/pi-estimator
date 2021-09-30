# This program estimates the value of Pi by using the monte carlo method

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randrange
from matplotlib.animation import FuncAnimation

plt.style.use("dark_background")

# Initialises trial counters and point lists
trialcount = 0
insidecount = 0
outsidecount = 0
piestimate = 0
xdata = []
ydata = []

insidex = []
insidey = []
outsidex = []
outsidey = []

# Applies an object oriented approach to the figure
fig, (ax1, ax2) = plt.subplots(nrows= 1, ncols= 2)

ax2.set_aspect("equal")
fig.suptitle("Monte Carlo Pi estimator")

# Define and draw circle
mycircle = plt.Circle((5000,5000), 5000)
mycircle.set_fill(False)
ax2.add_artist(mycircle)

# Sets the parameters for the first axis
def setax1params():
    ax1.tick_params(axis = "both", which = "both", bottom = False, left = False)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.text(x = 0.2, y = 0.75, s = f"Number of trials: {trialcount}\nPoints inside circle: {insidecount}\nPoints outside circle: {outsidecount}\nCurrent pi estimate: {piestimate}")

setax1params()

# Formats the axis parameters (so the viewport fits the data)
def setax2params():
    ax2.tick_params(axis = "both", which = "both", right = False, top = False)
    ax2.set_xlim([0,10000])
    ax2.set_ylim([0,10000])
    ax2.set_xticks([0,10000])
    ax2.set_yticks([0,10000])
    ax2.set_xticklabels([0,1])
    ax2.set_yticklabels([0,1])
    ax2.set_anchor(anchor = "E")

    setax2params()

    # ignores the animation initialisation function
def init():
    pass

    # Animate the scatter plot
def animate(i):
    ax1.cla()
    ax2.cla()
    global trialcount
    trialcount += 1
    # Generate a random pair of x and y co-ordinates
    newpoints = (randrange(0, 10001), randrange(0, 10001))
 
    # if the new point is inside the circle add it to an inner list, else, add it to an outer list
    if ((newpoints[0] - 5000) ** 2) + ((newpoints[1] - 5000) ** 2) <= (5000 ** 2):
        global insidex
        global insidey
        insidex.append(newpoints[0])
        insidey.append(newpoints[1])
        global insidecount
        insidecount += 1
    else:
        global outsidex
        global outsidey
        outsidex.append(newpoints[0])
        outsidey.append(newpoints[1])

        global outsidecount
        outsidecount += 1

    # Scatter the inner points in red, and the outer points in blue
    plt.scatter(insidex, insidey, s = 1, c = 'r')
    plt.scatter(outsidex, outsidey, s = 1, c = 'b')

    # pi estimate formula
    global piestimate
    piestimate = 4 * (insidecount / trialcount)

    setax1params()
    setax2params()

    ax2.add_artist(mycircle)


    
animation = FuncAnimation(fig, animate, init_func = init, interval = 60)

plt.show()


