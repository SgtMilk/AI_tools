import os
import shutil

base_folder = '/home/alix/Documents/ML_data/drone_obstacle_detection/classified'
all_folders = os.listdir(base_folder)

destination_folder = '/home/alix/Documents/ML_data/drone_obstacle_detection/re-classified'
destination_folder_train = os.path.join(destination_folder, 'train')
destination_folder_validation = os.path.join(destination_folder, 'validation')
destination_folder_test = os.path.join(destination_folder, 'test')

if(os.path.exists(destination_folder) == False):
    os.mkdir(destination_folder)
if(os.path.exists(destination_folder_train) == False):
    os.mkdir(destination_folder_train)
if(os.path.exists(destination_folder_validation) == False):
    os.mkdir(destination_folder_validation)
if(os.path.exists(destination_folder_test) == False):
    os.mkdir(destination_folder_test)

destination_folder_all_folders = [
    destination_folder_train, destination_folder_validation, destination_folder_test]


for folder in all_folders:
    if os.path.isdir == False:
        continue
    current_folder = os.path.join(base_folder, folder)

    for Type in destination_folder_all_folders:
        sub_destination_folder = os.path.join(Type, folder)
        if os.path.exists(sub_destination_folder == False):
            os.mkdir(sub_destination_folder)

    counter = 0
    all_files_in_folder = os.listdir(current_folder)
    for File in all_files_in_folder:
        src = os.path.join(current_folder, File)
        if os.path.isfile(src) == False:
            continue

        if counter == 0 or counter == 1:
            dst = os.path.join(destination_folder_train, folder, File)
            shutil.copyfile(src, dst)
            counter += 1
            continue
        elif counter == 2:
            dst = os.path.join(destination_folder_validation, folder, File)
            shutil.copyfile(src, dst)
            counter += 1
            continue
        elif counter == 3:
            dst = os.path.join(destination_folder_test, folder, File)
            shutil.copyfile(src, dst)
            counter = 0
            continue
