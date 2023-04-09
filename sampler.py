import os
import pandas as pd

root_folder = '~/dl4hl/data'

data_folder = os.path.expanduser(root_folder)
output_folder = os.path.expanduser(root_folder + '/sample_mimic')
os.makedirs(output_folder, exist_ok=True)

# Read the data files
admissions = pd.read_csv(os.path.join(data_folder, 'ADMISSIONS.csv'))
diagnoses_icd = pd.read_csv(os.path.join(data_folder, 'DIAGNOSES_ICD.csv'))
noteevents = pd.read_csv(os.path.join(data_folder, 'NOTEEVENTS.csv'))
patients = pd.read_csv(os.path.join(data_folder, 'PATIENTS.csv'))

# Sample 50% of unique patients
sampled_subject_ids = patients['SUBJECT_ID'].sample(frac=0.35).values

# Filter each table by the sampled patients
admissions_sampled = admissions[admissions['SUBJECT_ID'].isin(sampled_subject_ids)]
diagnoses_icd_sampled = diagnoses_icd[diagnoses_icd['SUBJECT_ID'].isin(sampled_subject_ids)]
noteevents_sampled = noteevents[noteevents['SUBJECT_ID'].isin(sampled_subject_ids)]
patients_sampled = patients[patients['SUBJECT_ID'].isin(sampled_subject_ids)]

# Save the sampled data
admissions_sampled.to_csv(os.path.join(output_folder, 'ADMISSIONS.csv'), index=False)
diagnoses_icd_sampled.to_csv(os.path.join(output_folder, 'DIAGNOSES_ICD.csv'), index=False)
noteevents_sampled.to_csv(os.path.join(output_folder, 'NOTEEVENTS.csv'), index=False)
patients_sampled.to_csv(os.path.join(output_folder, 'PATIENTS.csv'), index=False)

# Save the sampled_subject_ids to a text file
with open(os.path.join(output_folder, 'sampled_subject_ids.txt'), 'w') as f:
    for subject_id in sampled_subject_ids:
        f.write(f"{subject_id}\n")