# Load libraries
import pandas as pd
from pathlib import Path
import os

# Load FTHP_Metadata excel doc as a pandas dataframe
data = pd.read_excel("FTHP_Metadata.xlsx", sheet_name='data')
# Subset data
df = data[["scanID", "sessionID", "repeatID"]]

# Create a for loop that iterates across the range of values in "sessionID"
for index,row in df.iterrows():
    scan_id = row["scanID"]
    session_id = row["sessionID"]
    from_path = Path(f"/storage/research/cinn_comp/ThalSR/zan/derivatives/test/practice/scanID/{scan_id}")
    to_path = Path(f"/storage/research/cinn_comp/ThalSR/zan/derivatives/test/practice/sessionID/{session_id}/anat")
    
    # Loop through .nii files in specified folder
    for file in Path(r'/storage/research/cinn_comp/ThalSR/zan/FTHP/').glob("*.nii"):
        # Add prefix to .nii files
        dst = f"sub-001_ses-{session_id}_scan-{os.path.basename(file)}"
        # Rename existing files to new files with prefix
        os.rename(file, os.path.join(os.path.dirname(file), dst))

# To name the .nii & .json files correctly
#f"sub-01_ses-{session_id}_run-{repeatID+1}{os.path.basename(file)}"
