import os
import sys
import shutil

if __name__ == '__main__':
    # source_dir = "/mnt/c/Users/XinWang0219/Documents/EC518/project/lift-splat-shoot/data/mini/samples"
    # target_dir = "./CARLA_CAMERA/nuScenes"

    source_dir = sys.argv[1]
    target_dir = sys.argv[2]

    if not os.path.exists(source_dir):
        print('source_dir does not exist')
        exit()

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    dir_names = os.listdir(source_dir)
    dir_names = [dir_name for dir_name in dir_names if dir_name.startswith('CAM_')]

    for dir_name in dir_names:
        data_dir_path = os.path.join(source_dir, dir_name)
        image_file_names = os.listdir(data_dir_path)

        for image_file_name in image_file_names:
            reformatted_image_file_name = image_file_name
            image_file_path = os.path.join(data_dir_path, image_file_name)
            target_image_file_path = os.path.join(target_dir, reformatted_image_file_name)
            shutil.copy(image_file_path, target_image_file_path)