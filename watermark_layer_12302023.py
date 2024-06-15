from PIL import Image as PILImage
import os
import sys
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

# Run 'python -m auto_py_to_exe' in command prompt to create .exe
# https://pillow.readthedocs.io/en/stable/reference/Image.html

def openFolder():
    dir_path = filedialog.askdirectory(title='+++++++++ SELECT FOLDER WITH IMAGES +++++++++')
    start(dir_path)
    
def start(dir_path):
    # Loop through directory 
    for image in os.listdir(dir_path):
        # print('dir_pth : ' + dir_path)
        print('Image Name : ' + image)
        if '.jpg' in image and image != 'MadrigueraWatermark_4000x4000.png':
            
            # Opening the primary image (used in background)
            img1 = PILImage.open(dir_path + '\\' + image)
            width, height = img1.size
            print('IMAGE SIZE : ' + str(width) + ', ' + str(height))
            
            # Opening the secondary image (overlay image)
            if getattr(sys, 'frozen', False):
                # Running in a bundle
                bundle_dir = sys._MEIPASS
            else:
                # Running in a normal Python environment
                bundle_dir = os.path.dirname(os.path.abspath(__file__))

            img2_path = os.path.join(bundle_dir, 'MadrigueraWatermark_4000x4000.png')
            img2 = PILImage.open(img2_path)
            
            print('Image 2 size: ' + str(img2.size))
            print('AFTER Image 2 size: ' + str(img2.size))

            # Pasting img2 image on top of img1 
            img1.paste(img2, box=None, mask = img2)
            
            # Split 'png' from the file to later insert '_ForRevision' in between
            pngSplit = image.split('.')

            print(pngSplit)
            # Save Image
            img1.save(dir_path + '\\' + pngSplit[0] + '_ForRevision.' + pngSplit[1]) 
            
# Set up GUI
window = Tk()
Label(window
      , text='IMPORTANT NOTES:\n - All image must be within the same folder\n - All images to be watermarked must be of \'.jpg\' format'
      , font=('Aerial 14'),).pack()

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set window size
window_width = 500
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