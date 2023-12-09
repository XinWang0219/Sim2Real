import sys
import os
import shutil

"""
    0: front
    1: front right
    2: back right
    3: back
    4: back left
    5: front left
"""

if __name__ == '__main__':
    source_dir = sys.argv[1]
    target_dir = sys.argv[2]

    print(source_dir)
    print(target_dir)

    # check source_dir
    if not os.path.exists(source_dir):
        print('source_dir does not exist')
        exit()

    # create target_dir if not exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # get all dir names and path in source_dir
    dir_names = os.listdir(source_dir)

    # print(target_dir)
    # print(source_dir)
    # print(dir_names)

    target_dir_path = os.path.join(target_dir, "CARLA")
    if not os.path.exists(target_dir_path):
        os.makedirs(target_dir_path)

    # create dir in target_dir
    for dir_name in dir_names:
        # get all camera dir in directory from source_dir
        data_dir_path = os.path.join(source_dir, dir_name)
        camera_dir_names = os.listdir(data_dir_path)
        camera_dir_names = [camera_dir_name for camera_dir_name in camera_dir_names if camera_dir_name.startswith('cam')]

        # print(camera_dir_names)

        for camera_dir_name in camera_dir_names:
            camera_dir_path = os.path.join(data_dir_path, camera_dir_name)
            # get all image file names in camera dir
            image_file_names = os.listdir(camera_dir_path)

            # cope all image files to target_dir
            for image_file_name in image_file_names:
                reformatted_image_file_name = camera_dir_name + '_' + dir_name + '_' + image_file_name
                image_file_path = os.path.join(camera_dir_path, image_file_name)
                target_image_file_path = os.path.join(target_dir_path, reformatted_image_file_name)
                shutil.copy(image_file_path, target_image_file_path)
                # print(image_file_path)
                # print(target_image_file_path)

    print('done')
    