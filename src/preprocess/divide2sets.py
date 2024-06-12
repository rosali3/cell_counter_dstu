import os
from os import listdir
from os.path import isfile, join
import shutil
from random import shuffle


path2images = 'images'
path2labels = 'labels'

files = [file for file in listdir(path2images) if isfile(join(path2images, file))]

shuffle(files)

for file in files[0:200]:
    shutil.copyfile(path2images + '/'  + file, 'images_test/' + file)
    shutil.copyfile(path2labels + '/' + os.path.splitext(file)[0] + '.txt', 'labels_test/' + os.path.splitext(file)[0] + '.txt')

for file in files[200:400]:
    shutil.copyfile(path2images + '/'  + file, 'images_valid/' + file)
    shutil.copyfile(path2labels + '/' + os.path.splitext(file)[0] + '.txt', 'labels_valid/' + os.path.splitext(file)[0] + '.txt')

for file in files[400:]:
    shutil.copyfile(path2images + '/'  + file, 'images_train/' + file)
    shutil.copyfile(path2labels + '/' + os.path.splitext(file)[0] + '.txt', 'labels_train/' + os.path.splitext(file)[0] + '.txt')

# print(files)
