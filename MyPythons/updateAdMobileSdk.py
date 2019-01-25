# encoding: utf8

import os
import shutil

latest_sdk_files_dir = "/Users/kaifa/Desktop/Test" #最新sdk文件路径
old_sdk_files_dir = "/Users/kaifa/Desktop/Working/GitLab/MCFM/Pods"  #老的sdk文件所在的最大目录，所有的 sdk 在一起的总目录，将会在这个目录下进行 sdk 查找

# 从 latest_sdk_files_dir 下查找出所有的 sdk 文件名放入数组
sdk_file_names = []
sdk_file_map = {}

for root, dirs, filenames in os.walk(latest_sdk_files_dir) :
    for dir in dirs :
        suffix = os.path.splitext(dir)[1]
        if suffix == ".framework" :
            file_path = os.path.join(root, dir)
            sdk_file_names.append(dir)
            sdk_file_map[dir] = file_path

# 在 old_sdk_files_dir 中查找 sdk， 如果包含在 sdk_file_names 中，则进行文件替换, sdk_file_names 移除已替换文件名
for root, dirs, filenames in os.walk(old_sdk_files_dir) :
    for dir in dirs :
        if len(sdk_file_names) == 0 :
            print("end sdk udpate......")
            os._exit(0)
        suffix = os.path.splitext(dir)[1]
        if suffix == ".framework" :
            if dir in sdk_file_map :
                latest_file_path = sdk_file_map[dir]
                old_file_path = os.path.join(root, dir)
                shutil.rmtree(old_file_path)
                shutil.copytree(latest_file_path, old_file_path)
                sdk_file_names.remove(dir)
