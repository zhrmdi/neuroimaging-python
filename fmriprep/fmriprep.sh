#!/bin/bash

#User inputs:
bids_root_dir=$HOME/Users/zahra/ds000102
subj=08
nthreads=4
mem=8 #gb
container=docker #docker or singularity

#Begin:

#Convert virtual memory from gb to mb
mem=`echo "${mem//[!0-9]/}"` #remove gb at end
mem_mb=`echo $(((mem*1000)-5000))` #reduce some memory for buffer space during pre-processing

export TEMPLATEFLOW_HOME=$HOME/.cache/templateflow
export FS_LICENSE=$HOME/BIDS_tutorial/derivatives/license.txt

#Run fmriprep
fmriprep-docker $bids_root_dir $bids_root_dir/derivatives \
    participant \
    --participant-label $subj \
    --skip-bids-validation \
    --md-only-boilerplate \
    --fs-license-file $bids_root_dir/derivatives/license.txt \
    --fs-no-reconall \
    --output-spaces MNI152NLin2009cAsym:res-2 \
    --nthreads $nthreads \
    --stop-on-first-crash \
    --mem_mb $mem_mb \
    -w $HOME
