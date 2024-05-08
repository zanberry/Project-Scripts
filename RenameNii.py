import glob
import os
import pathlib

# Loop through .nii files in specified folder
for file in pathlib.Path(r'/storage/research/cinn_comp/ThalSR/zan/FTHP/').glob("*.nii"):
    # Add prefix to .nii files
    dst = f"{os.path.basename(file)}"
    # Rename existing files to new files with prefix
    os.rename(file, os.path.join(os.path.dirname(file), dst))

print("Renamed .nii files!")


