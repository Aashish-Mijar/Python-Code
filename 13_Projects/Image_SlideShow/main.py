from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow viewer")

# List of Image Path
image_path = [
    r'\For_SlideShow_app\img1.jpg',
    r'\For_SlideShow_app\img2.jpg',
    r'\For_SlideShow_app\img3.jpg',
    r'\For_SlideShow_app\img4.jpg',
    r'\For_SlideShow_app\img5.jpg',
    r'\For_SlideShow_app\img6.jpg',
]

# Resize the images to 1080 x 1080
