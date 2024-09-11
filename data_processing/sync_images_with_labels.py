import os

folder_path = '../data/Obstacle Dataset/img-train'

files = os.listdir(folder_path)

image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
label_files = [f for f in files if f.endswith('.txt')]

label_basenames = {os.path.splitext(f)[0] for f in label_files}

for image_file in image_files:
    image_basename = os.path.splitext(image_file)[0]

    if image_basename not in label_basenames:
        os.remove(os.path.join(folder_path, image_file))
        print(f"Image deleted: {image_file} - missing annotation file")
    else:
        print(f"An annotation file was found for the image: {image_file}")
