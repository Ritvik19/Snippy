import os, random
import matplotlib.pyplot as plt
from tqdm.auto import tqdm
from keras.preprocessing.image import ImageDataGenerator

dataaug = ImageDataGenerator(
    shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True, rotation_range=10,
    height_shift_range=0.1, width_shift_range=0.1
)

def balance_class(source_directory, target_directory, imagegen_obj, target_size=None, cmap='viridis'):
    
    class_examples = []
    os.mkdir(target_directory)
    for directory in os.listdir(source_directory):
        os.mkdir(os.path.join(target_directory, directory))
        class_examples.append(len(os.listdir(os.path.join(source_directory, directory))))
    
    print('Class Distribution:', class_examples)
    
    if target_size == None:
        target_size = max(class_examples)
        
    for i, directory in enumerate(os.listdir(source_directory)):
        dest_dir = os.path.join(target_directory, directory)
        if target_size > class_examples[i]:        
            q, r = divmod(target_size, class_examples[i])
            q, r = q-1, r/class_examples[i]
            for imgpath in tqdm(os.listdir(os.path.join(source_directory, directory))):
                filename, file_extension = os.path.splitext(imgpath)
                img = plt.imread(os.path.join(source_directory, directory, imgpath))
                plt.imsave(os.path.join(dest_dir, imgpath), img, cmap=cmap)
                for i in range(q):
                    if cmap == 'gray':
                        aug_img = np.squeeze(dataaug.random_transform(np.expand_dims(img, axis=2)))
                    else:
                        aug_img = imagegen_obj.random_transform(img)
                    plt.imsave(os.path.join(dest_dir, f"{filename}-{i+1}{file_extension}"), aug_img, cmap=cmap)
                prob = random.random()
                if prob <= r:
                    if cmap == 'gray':
                        aug_img = np.squeeze(dataaug.random_transform(np.expand_dims(img, axis=2)))
                    else:
                        aug_img = imagegen_obj.random_transform(img)
                    plt.imsave(os.path.join(dest_dir, f"{filename}-{0}{file_extension}"), aug_img, cmap=cmap)
        else:
            r = target_size/class_examples[i]
            for imgpath in tqdm(os.listdir(os.path.join(source_directory, directory))):
                filename, file_extension = os.path.splitext(imgpath)
                img = plt.imread(os.path.join(source_directory, directory, imgpath))
                prob = random.random()
                if prob <= r:
                    plt.imsave(os.path.join(dest_dir, imgpath), img, cmap=cmap)
    class_examples_updated = []
    for directory in os.listdir(target_directory):
        class_examples_updated.append(len(os.listdir(os.path.join(target_directory, directory))))   
    print('Updated Class Distribution:', class_examples_updated)
    
    
    
balance_class(
    source_directory='dataset/train/', target_directory='dataset/train-balanced/',
    imagegen_obj=dataaug, target_size=None
)    