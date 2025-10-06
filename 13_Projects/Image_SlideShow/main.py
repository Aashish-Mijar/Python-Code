from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow viewer")

# List of Image Path
image_paths = [
    r'\For_SlideShow_app\img1.jpg',
    r'\For_SlideShow_app\img2.jpg',
    r'\For_SlideShow_app\img3.jpg',
    r'\For_SlideShow_app\img4.jpg',
    r'\For_SlideShow_app\img5.jpg',
    r'\For_SlideShow_app\img6.jpg',
]

# Resize the images to 1080 x 1080
image_size = (1080, 1080)
images = [Image.open(path). resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.root()
