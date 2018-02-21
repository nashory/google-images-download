import os, sys


SAVE_PATH = './downloads'
dir_list = [d for d in os.listdir(SAVE_PATH)]
file_list = [f for f in os.listdir('./downloads/') if os.path.isfile(f)]

for _, mdir in enumerate(dir_list):
  SEARCH_PATH = os.path.join(SAVE_PATH, mdir)
  file_list = [f for f in os.listdir(SEARCH_PATH) if os.path.isfile(os.path.join(SEARCH_PATH,f))]
  

  for k, v in enumerate(file_list):
    '''
    file name format: IDX0_IID0.jpg
    '''
    _, ext = os.path.splitext(v)
    new_name = 'IDX{}_IID{}.{}'.format(mdir, k, ext)
    os.rename(os.path.join(SEARCH_PATH, v), os.path.join(SEARCH_PATH, new_name))
    print(new_name)
    
