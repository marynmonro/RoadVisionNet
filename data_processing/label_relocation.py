import os
import shutil

images_path = '../data/Obstacle Dataset/img-val'
labels_path = '../data/Obstacle Dataset/label-val'
destination_path = '../data/Obstacle Dataset/img-val'

image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

for image_file in image_files:
    base_name = os.path.splitext(image_file)[0]
    label_file = base_name + '.txt'

    source_label_path = os.path.join(labels_path, label_file)
    destination_label_path = os.path.join(destination_path, label_file)

    if os.path.exists(source_label_path):
        shutil.move(source_label_path, destination_label_path)
        print(f"Relocated: {label_file}")
    else:
        print(f"Label file not found: {label_file}")
