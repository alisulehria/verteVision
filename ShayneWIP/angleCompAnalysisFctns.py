# VerteVision Biomedical Engineering Capstone Project Spring 2024
# Author(s): Shayne Shelton
# Collaborator(s): Pete Rotering, Ali Suleheria

# Objective: This script provides functions for analyzing and visualizing vertebral
# angles obtained from O-arm images.

import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import matplotlib.pyplot as plt


# orientVectors(float[]) --> (float, float)[]
#   The angles (in degrees) obtained are not guaranteed to all be positive or negative.
#   oreintVectors takes in the data directly from the previous step of the workflow
#   and ensures they are all positive or negative. The function outputs a list of
#   tuples in the format (degrees, radians)[]

def orientVectors(degrees):
    output = []

    radians = (np.array(degrees) * np.pi) / 180
    for i in range(len(degrees)):
        if degrees[i] > 0:
            degrees[i] -= 180
            radians[i] -= np.pi
        output.append((degrees[i], radians[i]))

    return output


# generateVectorGraph((float, float)[]) --> matplotlib.figure.Figure
#   The angeles obtained in the format (degrees, radians)[] are represented as
#   vectors and displayed in a graph.

def generateVectorGraph(angles):
    graph = plt.figure()
    ax = plt.subplot(111, projection='polar')
    for i in angles:
        ax.plot([i[1], i[1]], [0, 1])
    print(type(graph))
    return graph


# rotationScore((float, float)[]) --> float
#   The angeles obtained in the format (degrees, radians)[] are reduced and expressed
#   to represent the degree of rotation.
#   * Computations are base on angles expressed in degrees.

def rotationScore(angles):
    score = 0
    for i, j in angles:
        dev = i + 90
        score += (dev * dev)
    score /= len(angles)
    return score


# print(rotationScore(orientVectors([-83.313, -82.792, 89.175, -87.748, 84.785, -84.264])))

# Create a Tkinter window
root = tk.Tk() # This is what we hope to use for our UI moving forward.
root.title("Vector Graph")

angles = orientVectors([-83.313, -82.792, 89.175, -87.748, 84.785, -84.264])

# Generate the Matplotlib figure
fig = generateVectorGraph(angles)

# Embed the figure in a Tkinter frame
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# # Add a text box to the canvas
# text_box = tk.Text(root, height=2, width=30)
# text_box.insert(tk.END, "Sample Text")
# canvas._tkcanvas.create_window(50, 50, anchor='nw', window=text_box)

# Add Matplotlib navigation toolbar
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Add a label to display information
info_label = tk.Label(root, text="Roation Score: " + str(rotationScore(angles)), bg="black", padx=10, pady=5)
canvas._tkcanvas.create_window(50, 50, anchor='nw', window=info_label)

# Run the Tkinter event loop
root.mainloop()
