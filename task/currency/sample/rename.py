import os, sys
import shutil
import math
from PIL import Image

SAVE_PATH = './'
dir_list = [d for d in os.listdir(SAVE_PATH)]
file_list = [f for f in os.listdir(SAVE_PATH) if os.path.isfile(f)]


THRES = 256
large=0
small=0
for _, mdir in enumerate(dir_list):
  SEARCH_PATH = os.path.join(SAVE_PATH, mdir)
  file_list = [f for f in os.listdir(SEARCH_PATH) if os.path.isfile(os.path.join(SEARCH_PATH,f))]
  
  for k, v in enumerate(file_list):
    '''
    file name format: IDX0_IID0.jpg
    '''
    try:
      IMG_PATH = os.path.join(SEARCH_PATH, v)
      im = Image.open(IMG_PATH)
      w, h = im.size
      if min(w,h) > THRES:
        large+=1
        _, ext = os.path.splitext(v)
        if ext.lower() in ['.jpg', '.png', '.jpeg']:
          new_name = '{}_IID{}{}'.format(mdir, str(k).zfill(4), ext)
          os.rename(IMG_PATH, os.path.join(SEARCH_PATH, new_name))
        else:
          os.remove(IMG_PATH)
      else:
        small+=1
        os.remove(IMG_PATH)
      print('thres: {}, included: {}, excluded: {}, survive: {:.2f}'.format(THRES, large, small, large/float(large+small)))
    except Exception as e:
      # if error, remove the image file for folder.
      print(e)
      os.remove(IMG_PATH)

    
