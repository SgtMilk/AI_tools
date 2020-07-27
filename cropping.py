from PIL import Image
import os

base_folder = '/home/alix/Documents/pictures/2nd'
dest_folder = '/home/alix/Documents/ML_data/drone_obstacle_detection/all_pictures'

counter = 2000

x = [0, 2000]
y = [0, 1000]

for item in os.listdir(base_folder):
    src = os.path.join(base_folder, item)
    print(src)
    img = Image.open(src)
    for j in y:
        for i in x:
            dimensions = (i, j, i+2000, j+2000)
            c = img.crop(box=dimensions)
            c.save(os.path.join(dest_folder, 'image_' +
                                str(counter) + '.jpg'), dpi=(1000, 1000))
            counter += 1
    img.close()
