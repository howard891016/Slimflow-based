import os
import shutil

source_dir = '/home/tkyen/PatchDM/dataset/ffhq128'  # 原始資料夾路徑
target_dir = '/tmp2/ffhq128'  # 目標資料夾路徑

# 確保目標資料夾存在
os.makedirs(target_dir, exist_ok=True)

# 遍歷 source_dir 下所有子資料夾與檔案
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.png'):
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_dir, file)
            
            # 若檔名重複，可加上前綴或編號
            if os.path.exists(target_file):
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(target_file):
                    target_file = os.path.join(target_dir, f"{base}_{counter}{ext}")
                    counter += 1
            
            shutil.copy2(source_file, target_file)

print("所有 .png 檔案已成功複製到", target_dir)
