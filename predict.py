import pandas as pd

# Load the datasets
train_data = pd.read_csv('/mnt/data/train.csv')
test_data = pd.read_csv('/mnt/data/test.csv')
gender_submission = pd.read_csv('/mnt/data/gender_submission.csv')
