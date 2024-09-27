# An example of fitting a GLM to perform first and second level analysis
# source: https://nilearn.github.io/stable/auto_examples/07_advanced/plot_bids_analysis.html#



# 1. Fetch example BIDS dataset

import os
from sklearn.utils import Bunch
from bids import BIDSLayout
from nilearn.datasets import fetch_language_localizer_demo_dataset
# Define a path to store the dataset
data_dir = os.path.join(os.path.expanduser('~'), 'nilearn_data', 'fMRI-language-localizer-demo-dataset')

# Check if the data already exists
if os.path.exists(data_dir):
    print(f"Using existing data in {data_dir}")
    # Create a BIDSLayout object
    layout = BIDSLayout(data_dir)

    # Create a dictionary similar to what fetch_language_localizer_demo_dataset returns
    data = {
        'data_dir': data_dir,
        'func': layout.get(datatype='func', extension='nii.gz', return_type='file'),
        'events': layout.get(datatype='func', suffix='events', extension='tsv', return_type='file'),
        'confounds': layout.get(datatype='func', suffix='confounds', extension='tsv', return_type='file'),
    }
    data = Bunch(**data)
else:
    print("Downloading data...")
    data = fetch_language_localizer_demo_dataset(data_dir=data_dir, legacy_output=False)

print(data.data_dir)



# 2. Obtain automatically FirstLevelModel objects and fit arguments

from nilearn.glm.first_level import first_level_from_bids

task_label = "languagelocalizer"
(
    models,
    models_run_imgs,
    models_events,
    models_confounds,
) = first_level_from_bids(
    data.data_dir, task_label, img_filters=[("desc", "preproc")], n_jobs=2
)

# Quick sanity check on fit arguments
from pathlib import Path

print([Path(run).name for run in models_run_imgs[0]])
