import sys, os, time
import pandas as pd
import subprocess


INPUT = './sake_list.csv'
data = pd.read_csv(INPUT, skiprows=0)
length = len(data)



for i in range(length):
  s_time = time.time()

  keywords = []
  keywords.append('{} {}'.format(data['origin'][i].replace(',', ' '), data['name'][i].replace(',',' ')))
  keywords.append('{} {}'.format(data['made_by'][i].replace(',', ' '), data['name'][i].replace(',',' ')))
  keywords.append('{}'.format(data['name'][i].replace(',',' ')))
  
  key = None
  for _, v in enumerate(keywords):
    if key is not None:
      key += ','+v
    else:
      key = v
  
  try:
    # remove garbages
    #subprocess.call(['rm','-rf','keyword_*'])
    os.system('rm -rf downloads/keyword_*')
   
    # download.
    cmd = []
    cmd.extend(['python', '../../google-image-downloader.py'])
    cmd.extend(['-k', key])
    cmd.extend(['-l', '60'])
    cmd.extend(['-o', 'downloads'])
    subprocess.call(cmd)
    
    # move data and remove folder.
    #subprocess.call(['pwd'])
    #for k in range(2):
    #  os.system('mv downloads/keyword_'+str(k)+'/*' 'downloads/keyword_2')
    os.system('mv downloads/keyword_0/* ' 'downloads/keyword_2')
    os.system('mv downloads/keyword_1/* ' 'downloads/keyword_2')
    os.system('mv downloads/keyword_2 ' + 'downloads/'+str(i))
      #subprocess.call(['mv', '/home1/irteam/workspace/git/google-images-download/task/sake/downloads/keyword_{}/*'.format(i), '/home1/irteam/workspace/git/google-images-download/task/sake/downloads/keyword_2'])
    #subprocess.call(['mv', 'downloads/keyword_2', 'downloads/'+str(i)])
    
  except Exception as e:
    print(e)

  print('[{}/{}] finished. elapsed time: {:.2f} hours.'.format(i+1, length, (time.time()-s_time)/3600))




