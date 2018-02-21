import sys, os, time
import pandas as pd
import subprocess


#INPUT = './csv/sake_list.csv'
#data = pd.read_csv(INPUT, skiprows=0)
#length = len(data)


PATH = './csv_list/csv'
INPUT=['currency_korean.csv', 'currency_english.csv', 'currency_japanese.csv', 'currency_chinese.csv', 'currency_spanish.csv']


def get_combination(idx):
  FULL_PATH = [ os.path.join(PATH, mfile) for mfile in INPUT ]
  keywords = []
  for f in FULL_PATH:
    data = pd.read_csv(f, skiprows=0)
    # pattern 1
    keywords.append('{} {} {}'.format(data['name'][idx], data['magic1'][0], data['magic2'][0]))
    # pattern 2
    keywords.append('{} {} {}'.format(data['name'][idx], data['magic1'][0], data['magic2'][1]))
    # pattern 3
    keywords.append('{} {} {}'.format(data['name'][idx], data['magic1'][1], data['magic2'][0]))
    # pattern 4
    keywords.append('{} {} {}'.format(data['name'][idx], data['magic1'][1], data['magic2'][1]))
    # pattern 5
    keywords.append('{} {} {}'.format(data['country'][idx], data['magic1'][0], data['magic2'][0]))
    # pattern 6
    keywords.append('{} {} {}'.format(data['country'][idx], data['magic1'][0], data['magic2'][1]))
    # pattern 7
    keywords.append('{} {} {}'.format(data['country'][idx], data['magic1'][1], data['magic2'][0]))
    # pattern 8
    keywords.append('{} {} {}'.format(data['country'][idx], data['magic1'][1], data['magic2'][1]))
    
  dir_name = data['code'][idx]
  return keywords, dir_name



data = pd.read_csv(os.path.join(PATH, 'currency_korean.csv'))
length = len(data)

# create directory beforehand.
for i in range(length):
  dir_name = data['code'][i]
  if not os.path.exists(os.path.join('downloads/', dir_name)):
    os.makedirs(os.path.join('downloads/', dir_name))


for i in range(length):
  s_time = time.time()

  keywords, dir_name = get_combination(i)
  key = None
  for _, v in enumerate(keywords):
    if key is not None:
      key += ','+v
    else:
      key = v
 
  try:
    # download.
    cmd = []
    cmd.extend(['python', '../../google-image-downloader.py'])
    cmd.extend(['-k', key])
    cmd.extend(['-l', '30'])
    cmd.extend(['-o', 'downloads'])
    cmd.extend(['-n', dir_name])
    subprocess.call(cmd)
    
  except Exception as e:
    print(e)

  print('[{}/{}] finished. elapsed time: {:.2f} hours.'.format(i+1, length, (time.time()-s_time)/3600))


