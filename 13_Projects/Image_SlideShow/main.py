from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow viewer")

# List of Image Path
image_paths = [
    r'E:\Files_Semesters\Python\Python_Code\13_Projects\Image_SlideShow\For_SlideShow_app\img1.jpg',
    r'E:\Files_Semesters\Python\Python_Code\13_Projects\Image_SlideShow\For_SlideShow_app\img2.jpg',
    r'E:\Files_Semesters\Python\Python_Code\13_Projects\Image_SlideShow\For_SlideShow_app\img3.png',
    r'E:\Files_Semesters\Python\Python_Code\13_Projects\Image_SlideShow\For_SlideShow_app\img4.jpg',
    r'E:\Files_Semesters\Python\Python_Code\13_Projects\Image_SlideShow\For_SlideShow_app\img5.png',
    r'E:\Files_Semesters\Python\Python_Code\13_Projects\Image_SlideShow\For_SlideShow_app\img6.jpg',
]

# Resize the images to 900 x 900
image_size = (900, 900)
images = [Image.open(path). resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()