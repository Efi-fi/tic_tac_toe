import numpy as nm
from matplotlib import pyplot as plt


def visualize_seq(stat):
    print(stat)
    x = stat['xlst']
    y = stat['ylst']
    # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(x, y)  # Plot some data on the axes.
    dist_prob = [y[0]]
    for value in y[1:]:
        dist_prob.append(value+dist_prob[-1])
    summ = dist_prob[-1]
    dist_prob = [i*100/summ for i in dist_prob]
    ax.plot(stat['xlst'], dist_prob, label='linear')
    ax.set_xlabel('Number of moves')  # Add an x-label to the axes.
    ax.set_ylabel('Number of game')  # Add a y-label to the axes.
    ax.set_title("Moves per game")  # Add a title to the axes.
    #ax.legend()  # Add a legend.
    #fig.show()
    return fig
