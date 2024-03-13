# VerteVision Biomedical Engineering Capstone Project Spring 2024
# Author(s): Shayne Shelton
# Collaborator(s): Pete Rotering, Ali Suleheria

# Objective: This script provides functions for obtain orientation measurements
# from images of vertebral transverse crossections acquired from the O-arm

# Create an ImageJ2 gateway with the newest available version of ImageJ2.
import imagej
import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from sys import platform as sys_pf
from PIL import Image, ImageTk
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

print("Opening Gateway...")
ij = imagej.init()

# Load an image.
print("Loading Image...")
image_url = 'https://imagej.net/images/clown.png'
jimage = ij.io().open(image_url)

# Check if image loading was successful
if jimage is None:
    print("Failed to load image.")
else:
    # Convert the image from ImageJ2 to PIL Image
    print("Converting Image...")
    java_array = ij.py.from_java(jimage)
    image = np.array(java_array)

    # Check image dimensions
    if image.shape[0] > 0 and image.shape[1] > 0:
        # Display the image using Tkinter
        print("Displaying Image...")
        root = tk.Tk()
        root.title("Image Display")

        # Create a canvas to place the image
        canvas = tk.Canvas(root, width=image.shape[1], height=image.shape[0])
        canvas.pack()

        # Convert PIL Image to Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(image=Image.fromarray(image))

        # Create a label to display the image
        label = tk.Label(root, image=tk_image)
        label.pack()

        # Run the Tkinter event loop
        root.mainloop()
    else:
        print("Invalid image dimensions.")