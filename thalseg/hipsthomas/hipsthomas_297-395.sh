#!/bin/bash

#SBATCH -J HIPS-THOMAS
#SBATCH -N 1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=4G
#SBATCH --mail-user=sl009034@student.reading.ac.uk
#SBATCH --mail-type=ALL
#SBATCH --array=297-395
#SBATCH --partition=cinn

echo "Running HIPS-THOMAS on sub-${SLURM_ARRAY_TASK_ID}" && cd /storage/research/cinn_comp/ThalSR/zan/derivatives/sing_prac/fmriprep/297-395/sub-${SLURM_ARRAY_TASK_ID}/anat && singularity run -B ${PWD}:${PWD} -W ${PWD} -u --cleanenv /storage/research/cinn_comp/ThalSR/singularityContainers/thomasmerged_8b4002e08cc5.sif bash -c "hipsthomas_csh -i sub-${SLURM_ARRAY_TASK_ID}_desc-preproc_T1w.nii.gz -t1 -big" 