from PIL import Image
import os

# https://pillow.readthedocs.io/en/stable/reference/Image.html

dir_path = r'C:\Users\se_ba\Desktop\watermark\sample_images'
        dir_path = r'D:\MADRIGUERA\01 MADRIGUERA STUDIO\01 FIVERR\WATERMARK'

# Iterate directory 
for image in os.listdir(dir_path):
    # print('dir_pth : ' + dir_path)
    print('Image Name : ' + image)
    if '.jpg' in image:
        # Opening the primary image (used in background)
        img1 = Image.open(dir_path + '\\' + image)
        width, height = img1.size
        print('IMAGE SIZE : ' + str(width) + ', ' + str(height))
        # Opening the secondary image (overlay image)
        img2 = Image.open(r'C:\Users\se_ba\Desktop\watermark\Fiverr Watermark 4000x4000.png')
        # img2 = Image.open(r'D:\MADRIGUERA\01 MADRIGUERA STUDIO\01 FIVERR\WATERMARK\Resources\Fiverr Watermark 4000x4000.png')
        
        print('Image 2 size: ' + str(img2.size))
        
        # img2 = img2.resize(img1.size)

        print('AFTER Image 2 size: ' + str(img2.size))

        # Pasting img2 image on top of img1 
        img1.paste(img2, box=None, mask = img2)
        

        # Displaying the image
        # img1.show()
        list = image.split('.')
        # print(list)
        img1.save(dir_path + '\\test\\' + image) 
        # img1.save(dir_path + image)