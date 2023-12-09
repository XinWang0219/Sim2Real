"""
Copyright (C) 2020 NVIDIA Corporation.  All rights reserved.
Licensed under the NVIDIA Source Code License. See LICENSE at https://github.com/nv-tlabs/lift-splat-shoot.
Authors: Jonah Philion and Sanja Fidler
"""

from fire import Fire

import src

"""
pretrained model:

python main.py eval_model_iou mini --modelf=./model/model_pretrain_nuscene.pt --dataroot=./data
python main.py viz_model_preds mini --modelf=./model/model_pretrain_nuscene.pt --dataroot=./data --map_folder=./data/map_v1.3

# train model
python main.py train mini --dataroot=./ --logdir=./runs --gpuid=0 tensorboard --logdir=./runs
python main.py train mini --dataroot=./carla_data/median --logdir=./runs_median --gpuid=0 tensorboard --logdir=./runs_median
python main.py train mini --dataroot=./carla_data/large --logdir=./runs_large --gpuid=0 tensorboard --logdir=./runs_large

# eval model
python main.py eval_model_iou mini --modelf=./model/model_large2.pt --dataroot=./carla_data/small


# eval model on real data
python main.py eval_model_iou mini --modelf=./model/model_large2.pt --dataroot=./data
python main.py viz_model_preds mini --modelf=./model/model_large2.pt --dataroot=./data --map_folder=./data/map_v1.3
"""


if __name__ == '__main__':
    Fire({
        'lidar_check': src.explore.lidar_check,
        'cumsum_check': src.explore.cumsum_check,

        'train': src.train.train,
        'eval_model_iou': src.explore.eval_model_iou,
        'viz_model_preds': src.explore.viz_model_preds,
    })