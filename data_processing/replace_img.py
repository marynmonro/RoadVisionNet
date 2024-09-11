import os
import shutil

source_folder = 'data/Obstacle Dataset/JPEGImages'
target_folder = 'data/Obstacle Dataset/img-val'

source_images = {file for file in os.listdir(source_folder) if file.endswith(('.jpg', '.jpeg', '.png'))}

target_images = {file for file in os.listdir(target_folder) if file.endswith(('.jpg', '.jpeg', '.png'))}

common_images = source_images.intersection(target_images)

for image in common_images:
    source_image_path = os.path.join(source_folder, image)
    target_image_path = os.path.join(target_folder, image)
    shutil.copy2(source_image_path, target_image_path)
    print(f"The image has been replaced: {image}")

print(f"Total number of replaced files: {len(common_images)}")
