# VerteVision Biomedical Engineering Capstone Project Spring 2024
# Author(s): Shayne Shelton
# Collaborator(s): Pete Rotering, Ali Suleheria

# Objective: This script provides functions for obtain orientation measurements
# from images of vertebral transverse crossections acquired from the O-arm

# Create an ImageJ2 gateway with the newest available version of ImageJ2.
import imagej
print("Opening Gateway...")
ij = imagej.init()
print(f"ImageJ version: {ij.getVersion()}")
# Load an image.
print("Loading Image...")
image_url = 'https://imagej.net/images/clown.png'
jimage = ij.io().open(image_url)

# Convert the image from ImageJ2 to xarray, a package that adds
# labeled datasets to numpy (http://xarray.pydata.org/en/stable/).
print("Converting Image...")
image = ij.py.from_java(jimage)

# Display the image (backed by matplotlib).
print("Displaying Image...")
ij.ui().show(image, cmap='gray')
