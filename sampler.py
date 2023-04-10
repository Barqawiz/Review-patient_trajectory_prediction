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

# Filter patients with at least two admissions
patients_admission_counts = admissions['SUBJECT_ID'].value_counts()
patients_with_two_admissions = patients_admission_counts[patients_admission_counts >= 2].index
patients_with_less_than_two_admissions = patients_admission_counts[patients_admission_counts < 2].index

# Calculate the number of patients to sample
num_sample = int(0.4 * len(patients))
print('- the sample size: ', num_sample)

# Calculate the number of patients with two or more admissions and with less than two admissions in the sampled data
num_sample_two_admissions = int(0.85 * num_sample)
num_sample_less_than_two_admissions = num_sample - num_sample_two_admissions

# Sample patients with at least two admissions and less than two admissions
sampled_subject_ids_two_admissions = patients[patients['SUBJECT_ID'].isin(patients_with_two_admissions)]['SUBJECT_ID'].sample(n=num_sample_two_admissions).values
sampled_subject_ids_less_than_two_admissions = patients[patients['SUBJECT_ID'].isin(patients_with_less_than_two_admissions)]['SUBJECT_ID'].sample(n=num_sample_less_than_two_admissions).values

print('- number of patients with at least two admissions: ', len(sampled_subject_ids_two_admissions))
print('- number of patients with less than two admissions: ', len(sampled_subject_ids_less_than_two_admissions))

# Combine the sampled_subject_ids
sampled_subject_ids = list(sampled_subject_ids_two_admissions) + list(sampled_subject_ids_less_than_two_admissions)

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
