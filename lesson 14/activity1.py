from tkinter import *

from PIL import Image, ImageTk

import os

# Create window

root = Tk()

root.title("Image Viewer")

root.geometry("400x400")

# Get current folder path

current_path = os.getcwd()

# Full image path (make sure img.jpg is in same folder)

image_path = os.path.join(current_path, "img.jpg")

# Open image

try:
	upload = Image.open(image_path)

	# Resize image (optional but recommended)

	upload = upload.resize((300, 300))

	# Convert image for Tkinter

	image = ImageTk.PhotoImage(upload)

	# Display image

	label = Label(root, image=image)

	label.image = image # Prevent garbage collection

	label.pack(pady=10)

except FileNotFoundError:
	error_label = Label(root, text="Error: img.jpg not found!", fg="red")
	error_label.pack()

# Text label

text_label = Label(root, text="This is how you add image in Tkinter")

text_label.pack()

# Run app

root.mainloop()