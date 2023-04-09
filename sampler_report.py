import os
import pandas as pd

root_folder = '~/dl4hl/data'

data_folder = os.path.expanduser(root_folder)
output_folder = os.path.expanduser(root_folder + '/sample_mimic')
os.makedirs(output_folder, exist_ok=True)

# Read the data files

noteevents = pd.read_csv(os.path.join(data_folder, 'NOTEEVENTS.csv'))
sample_noteevents = pd.read_csv(os.path.join(output_folder, 'NOTEEVENTS.csv'))

print(' ---data report ---')
print('-original data path: ', os.path.join(data_folder, 'NOTEEVENTS.csv'))
print('-sample data path : ', os.path.join(output_folder, 'NOTEEVENTS.csv'))
print('----')
print('-note size before the sample: ', len(noteevents))
print('-note size after the sample: ', len(sample_noteevents))