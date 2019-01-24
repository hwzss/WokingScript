# encoding: utf8

import os
import shutil

latest_sdk_files_dir = " " #最新sdk文件路径
old_sdk_files_dir = ""  #老的sdk文件所在的最大目录，所有的 sdk 在一起的总目录，将会在这个目录下进行 sdk 查找

# 从 latest_sdk_files_dir 下查找出所有的 sdk 文件名放入数组
sdk_file_names = []
sdk_file_map = {}

for root, dirs, filenames in os.walk(latest_sdk_files_dir) :
    for filename in filenames :
        file_path = os.path.join(root, filename)
        sdk_file_names.append(filename)
        sdk_file_map[filename] = file_path

# 在 old_sdk_files_dir 中查找 sdk， 如果包含在 sdk_file_names 中，则进行文件替换, sdk_file_names 移除已替换文件名
for root, dirs, filenames in os.walk(old_sdk_files_dir) :
    for filename in filenames :
        if len(sdk_file_names) == 0 :
            os._exit(0)
        if filename in sdk_file_names :
            #  TODO: 文件替换
            latest_file_path = sdk_file_map[filename]
            old_file_path = os.path.join
            shutil.copyfile(latest_file_path, old_file_path)
            sdk_file_names.remove(filename)

# 结束