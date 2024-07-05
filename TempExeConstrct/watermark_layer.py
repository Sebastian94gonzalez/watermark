from PIL import Image as PILImage
import os
import sys
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

# Run 'python -m auto_py_to_exe' in command prompt to create .exe
# https://pillow.readthedocs.io/en/stable/reference/Image.html

def openFolder():
    dir_path = filedialog.askdirectory(title='+++++++++ SELECT FOLDER CONTAINING THE IMAGES +++++++++')
    # Create an output folder where all non directory files will land
    if 'WaterMarkedOutput' not in os.listdir(dir_path):
        os.mkdir(os.path.join(dir_path, 'WaterMarkedOutput')) 
    # Location where all items will be moved to
    target_dir = dir_path + '\WaterMarkedOutput'
    start(dir_path, target_dir)
    
def start(dir_path, target_dir):
    # Loop through directory 
    for image in os.listdir(dir_path):
        # print('dir_pth : ' + dir_path)
        print('Image Name : ' + image)
        if ('.png' or '.jpg' in image) and os.path.isfile(dir_path + '\\' + image):
            
            # Opening the primary image (used in background)
            img1 = PILImage.open(dir_path + '\\' + image)
            width, height = img1.size
            print('IMAGE SIZE : ' + str(width) + ', ' + str(height))
            
            # Opening the secondary image (overlay watermark image)
            if getattr(sys, 'frozen', False):
                # Running in a bundle
                bundle_dir = sys._MEIPASS
            else:
                # Running in a normal Python IDE
                bundle_dir = os.path.dirname(os.path.abspath(__file__))

            img2_path = os.path.join(bundle_dir, 'MadrigueraWatermark_4000x4000.png')
            img2 = PILImage.open(img2_path)

            # Pasting img2 image on top of img1 
            img1.paste(img2, box=None, mask = img2)
            
            # Save image on to the WaterMarkedOutput folder
            img1.save(target_dir + '\\' + image) 
            
# Set up GUI
window = Tk()
Label(window
      , text='IMPORTANT NOTES:\n - All image must be within the same folder\n - All images to be watermarked must be of \'.jpg\' OR \'.png\'format'
      , font=('Aerial 14'),).pack()

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set window size
window_width = 600
window_height = 150

# Calculate x and y offsets to center the window
x_offset = (screen_width - window_width) // 2
y_offset = (screen_height - window_height) // 2

# Set window geometry
window.geometry(f'{window_width}x{window_height}+{x_offset}+{y_offset}')

# Button to select folder and execute process
button = Button(text='Click Here to Select Folder', command=openFolder)
button.pack()

dir_path = None  # Placeholder for the directory path, to be set after the user selects a folder

window.mainloop()