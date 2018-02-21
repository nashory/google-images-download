import os, sys
import shutil
from PIL import Image


NUM_TEST = 100
DATA_PATH = '../sample'
SAVE_FOLDER = './split'
dir_list = [d for d in os.listdir(DATA_PATH)]


def is_valid(path):
  try:
    if os.path.isfile(path):
      return True
    _, ext = os.path.splitext(path)
    if ext.lower() in ['.jpg', 'png', 'jpeg']:
      return True
    return False
  except:
    return False




def get_img_list(path):
  try:
    return [f for f in os.listdir(path) if is_valid(os.path.join(path,f))]
  except Exception as e:
    pass;


# main loop.
for _, mdir in enumerate(dir_list):
  file_list = get_img_list(os.path.join(DATA_PATH, mdir))
  
  # prepare directories.
  if not os.path.exists(os.path.join(SAVE_FOLDER, 'val', mdir)):
    shutil.os.makedirs(os.path.join(SAVE_FOLDER, 'val', mdir))
  if not os.path.exists(os.path.join(SAVE_FOLDER, 'val', mdir)):
    shutil.os.makedirs(os.path.join(SAVE_FOLDER, 'train', mdir))
  
  # split
  val = 0
  train = 0
  for i in range(len(file_list)):
    im = Image.open(os.path.join(DATA_PATH, mdir, file_list[i])).convert('RGB')
    if (i<NUM_TEST):
      val+=1
      im.save(os.path.join(SAVE_FOLDER, 'val', mdir, file_list[i]))
    else:
      train+=1
      im.save(os.path.join(SAVE_FOLDER, 'train', mdir, file_list[i]))
    print('[total:{}][cls:{}][val:{}][train:{}] saved image: {}'.format(len(file_list), mdir, val, train, file_list[i]))
      

    


