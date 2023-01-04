from os import listdir
from os.path import isfile, join
import os
import shutil


def move_to_folder(downloads):

    files = [f for f in listdir(downloads) if isfile(join(downloads, f))]

    type_list = []          #lists all variations of type
    folder_dict = {}        #dictionary associating file type with folder name

    for file in files:
        if '.' in file:
             type = str(file.rsplit('.', 1)[-1])
        else:
            type = 'typeless'
        if type not in type_list:
            type_list.append(type)
            if type == 'img' or type == 'jpg' or type == 'png' or type == 'jpeg':
                new_folder = downloads + '/images'
            elif type == 'txt' or type == 'c' or type == 'h':
                new_folder = downloads + '/text'
            else:
                new_folder = downloads + '/' + type + '_files'
            folder_dict[str(type)] = str(new_folder)
        
        if os.path.isdir(new_folder):
            continue
        else:
            os.mkdir(new_folder)        #makes directory if folder does not already exist

    for file in files:
        source = downloads + '/' + file
        if '.' in file:
            type = str(file.rsplit('.', 1)[-1])
        else:
            type = 'typeless'
        if type in folder_dict.keys():
            destination = folder_dict[str(type)]
            shutil.move(source, destination)

if __name__ == "__main__":
    downloads = '/users/MilenaPetrovic/Downloads'
    move_to_folder(downloads)