#!/bin/bash

#SBATCH -J T1-THOMAS
#SBATCH -N 1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=4G
#SBATCH --mail-user=sl009034@student.reading.ac.uk
#SBATCH --mail-type=ALL
#SBATCH --array=198-296
#SBATCH --partition=cinn

echo "Running T1-THOMAS on sub-${SLURM_ARRAY_TASK_ID}" && cd /storage/research/cinn_comp/ThalSR/zan/derivatives/sing_prac/fmriprep/0-98/sub-${SLURM_ARRAY_TASK_ID}/anat && singularity run -B ${PWD}:${PWD} -W ${PWD} -u --cleanenv /storage/research/cinn_comp/ThalSR/singularityContainers/thomas_e9a1a0e4463d.sif bash -c "thomas_csh_mv sub-${SLURM_ARRAY_TASK_ID}_desc-preproc_T1w.nii.gz"

