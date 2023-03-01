from PIL import Image
import os

# folder_path = "C:\Users\se_ba\Desktop\watermark"
# folder path
dir_path = r'C:\Users\se_ba\Desktop\watermark\sample_images'

# Iterate directory 
for path in os.listdir(dir_path):
    print('dir_pth : ' + dir_path)
    print('PATH : ' + path)
    if '.jpg' in path:
        # Opening the primary image (used in background)
        img1 = Image.open(dir_path + '\\' + path)
        width, height = img1.size
        print('IMAGE SIZE : ' + str(width) + ', ' + str(height))
        # Opening the secondary image (overlay image)
        img2 = Image.open(r'C:\Users\se_ba\Desktop\watermark\Fiverr Watermark.png')
        
        # Pasting img2 image on top of img1 
        # starting at coordinates (0, 0)
        img1.paste(img2, (0,0), mask = img2)
        

        # Displaying the image
        # img1.show()
        list = path.split('.')
        print(list)
        img1.save(dir_path + '\\test\\' + list[0] + '.jpg')