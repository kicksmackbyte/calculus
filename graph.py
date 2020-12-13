import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import random
from collections import namedtuple
Point = namedtuple('Point', 'x y')


DRAW_ARROWS = True
DRAW_GRID_LINES = True

SAVE_GRAPH = True


def plot(points):
    # Sort by x-coordinate
    points.sort(key=lambda p: p.x)

    # Enter x and y coordinates of points and colors
    xs = [point.x for point in points]
    ys = [point.y for point in points]

    colors = ['r' for point in points]

    # Select length of axes and the space between tick labels
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    ticks_frequency = 1

    # Plot points
    fig, ax = plt.subplots(figsize=(xmax-xmin, ymax-ymin))
    ax.scatter(xs, ys, c=colors)

    # Connect points
    ax.plot(xs, ys, 'k-')

    # Draw lines connecting points to axes
    #[ax.plot([x, x], [0, y], c=c, ls='--', lw=1.5, alpha=0.5) for x, y, c in zip(xs, ys, colors)]
    #[ax.plot([0, x], [y, y], c=c, ls='--', lw=1.5, alpha=0.5) for x, y, c in zip(xs, ys, colors)]

    # Set identical scales for both axes
    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=15)
    ax.set_ylabel('y', size=14, labelpad=15, rotation=0)
    ax.xaxis.set_label_coords(1.03, 0.512)
    ax.yaxis.set_label_coords(0.5, 1.02)

    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    x_ticks_major = x_ticks[x_ticks != 0]
    ax.set_xticks(x_ticks_major)

    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
    y_ticks_major = y_ticks[y_ticks != 0]
    ax.set_yticks(y_ticks_major)

    # Create custom minor ticks to enable drawing of minor grid lines
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)


    if DRAW_GRID_LINES:
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)


    if DRAW_ARROWS:
        ax.plot((1), (0), linestyle='', marker='>', markersize=4, color='k', transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot((0), (1), linestyle='', marker='^', markersize=4, color='k', transform=ax.get_xaxis_transform(), clip_on=False)


    if SAVE_GRAPH:
        plt.savefig('A.png')


def random_points(num_points, low=-10, high=10):
    points = [Point(random.randint(low, high+1), random.randint(low, high+1)) for i in range(num_points)]
    return points


if __name__ == '__main__':
    points = random_points(5)

    plot(points)

