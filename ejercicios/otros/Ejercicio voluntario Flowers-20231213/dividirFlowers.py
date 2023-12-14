#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:53:40 2023

@author: migue8gl
"""

import os
import glob


def get_data_classes():
    data_classes = []
    with open('dataset/classes.txt', 'r') as f:
        for line in f:
            data_classes.append(line.replace('\n', ''))
    return data_classes


def create_directories_for_classes(directory_names):
    for name in directory_names:
        if not os.path.exists(name):
            os.makedirs(name)


def group_images_by_class(classes):
    images_path = 'dataset/'
    count = 1
    index_classes = 0

    elements = sorted(glob.glob(images_path+'image_*'))

    for image in elements:
        if count == 81:
            index_classes += 1
            count = 1
        new_name = classes[index_classes] + '/' + image.replace(
            images_path, '').replace('.jpg', '') + '_' + classes[index_classes] + '_' + str(count) + '.jpg'

        os.system('cp ' + image + ' ' + classes[index_classes])
        image_new_location = image.replace(
            images_path, classes[index_classes] + '/')

        os.system('mv ' + image_new_location + ' ' + new_name)
        count += 1


names = get_data_classes()
create_directories_for_classes(names)
group_images_by_class(names)
