import site
import os
import shutil

print(site.getsitepackages())

dest_path = site.getsitepackages()[0]

dest_path = dest_path + '/duckietown_world/data/gd1/maps'

src_path = './src/gym_duckietown/maps'
files = os.listdir(src_path)


for fname in files:
     
    # copying the files to the
    # destination directory
    shutil.copy2(os.path.join(src_path,fname), dest_path)




