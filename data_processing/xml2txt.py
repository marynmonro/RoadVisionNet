import xml.etree.ElementTree as ET
import os

classes = ["stop_sign", "person", "bus", "truck", "car", "motorbike", "dog"]
myRoot = r'C:\Praca Dyplomowa\Nowa wersja\Klasyfikacja_obiektow_na_drodze\data\Obstacle Dataset'

# xmlRoot = myRoot + r'\Annotations'
# txtRoot = myRoot + r'\labels'
# imageRoot = myRoot + r'\JPEGImages'

# xmlRoot = myRoot + r'\ann-test'
# txtRoot = myRoot + r'\label-test'
# imageRoot = myRoot + r'\img-test'

# xmlRoot = myRoot + r'\ann-train'
# txtRoot = myRoot + r'\label-train'
# imageRoot = myRoot + r'\img-train'

xmlRoot = myRoot + r'\ann-val'
txtRoot = myRoot + r'\label-val'
imageRoot = myRoot + r'\img-val'


def getFile_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        print(files)
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.splitext(file)[0])
    return L


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open(f"{xmlRoot}\\{image_id}.xml", encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    valid_objects = []

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text),
             float(xmlbox.find('xmax').text),
             float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        valid_objects.append((cls_id, bb))

    if valid_objects:
        out_file = open(f"{txtRoot}\\{image_id}.txt", 'w', encoding='utf-8')
        for cls_id, bb in valid_objects:
            out_file.write(f"{cls_id} {' '.join(f'{a:.6f}' for a in bb)}\n")
        out_file.close()


image_ids = getFile_name(imageRoot)

list_file_img = open(myRoot + r'\img.txt', 'w')

for image_id in image_ids:
    list_file_img.write(imageRoot + '\\%s.jpg\n' % (image_id))
    convert_annotation(image_id)
list_file_img.close()


# list_file_train = open(myRoot + r'\train.txt', 'w')
#
# for image_id in image_ids:
#     list_file_train.write(imageRoot + '\\%s.jpg\n' % (image_id))
#     convert_annotation(image_id)
# list_file_train.close()
#
#
# list_file_test = open(myRoot + r'\test.txt', 'w')
#
# for image_id in image_ids:
#     list_file_test.write(imageRoot + '\\%s.jpg\n' % (image_id))
#     convert_annotation(image_id)
# list_file_test.close()
#
#
# list_file_val = open(myRoot + r'\val.txt', 'w')
#
# for image_id in image_ids:
#     list_file_val.write(imageRoot + '\\%s.jpg\n' % (image_id))
#     convert_annotation(image_id)
# list_file_val.close()


