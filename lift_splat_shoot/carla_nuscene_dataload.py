import os
import sys
from huggingface_hub import snapshot_download

def download_carla_nuscene_data():
    snapshot_download(repo_id='collabora/carla-nuscenes', repo_type='dataset', local_dir='./data/carla-nuscene')
    print('Downloaded Carla-Nuscene data')

# recursively in directory change all zip files persmissions to 777 and unzip them to the current directory
def unzip_all_files_in_dir(dir):
    # check if dir exists
    if not os.path.isdir(dir):
        print('Directory ' + dir + ' does not exist')
        return

    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.zip'):
                file_path = os.path.join(root, file)
                print('Unzipping ' + file_path)
                os.chmod(os.path.join(root, file), 0o777)
                os.system('unzip -o ' + os.path.join(root, file) + ' -d ' + root)
                # os.remove(os.path.join(root, file))

if __name__ == '__main__':
    # download_carla_nuscene_data()
    unzip_all_files_in_dir('./data/carla_nuscene')
    print('Done')