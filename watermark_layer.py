from PIL import Image
import os

# Run 'python -m auto_py_to_exe' in command prompt to create .exe

# https://pillow.readthedocs.io/en/stable/reference/Image.html

dir_path = input("Enter filename: ")

def start():
    # Iterate directory 
    for image in os.listdir(dir_path):
        # print('dir_pth : ' + dir_path)
        print('Image Name : ' + image)
        if '.jpg' in image and image != 'Fiverr Watermark 4000x4000.png':
            
            # Opening the primary image (used in background)
            img1 = Image.open(dir_path + '\\' + image)
            width, height = img1.size
            print('IMAGE SIZE : ' + str(width) + ', ' + str(height))
            
            # Opening the secondary image (overlay image)
            img2 = Image.open(dir_path + '\Fiverr Watermark 4000x4000.png')
            
            print('Image 2 size: ' + str(img2.size))
            print('AFTER Image 2 size: ' + str(img2.size))

            # Pasting img2 image on top of img1 
            img1.paste(img2, box=None, mask = img2)
            
            # Split 'png' from the file to later insert '_WaterMarked' in between
            pngSplit = image.split('.')

            print(pngSplit)
            # Save Image
            img1.save(dir_path + '\\' + pngSplit[0] + '_WaterMarked.' + pngSplit[1]) 
            

start()

    