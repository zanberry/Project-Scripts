# Load libraries
import pandas as pd
import xlrd
from pathlib import Path
import shutil
import os

# Load FTHP_Metadata excel doc as a pandas dataframe
data = pd.read_excel("FTHP_Metadata.xlsx", sheet_name='data')
# Subset data
df = data[["scanID", "sessionID", "repeatID"]]

# Create a for loop that iterates across the range of values in "sessionID"
for index,row in df.iterrows():
    scan_id = row["scanID"]
    session_id = row["sessionID"]
    repeat_id = row["repeatID"]
    from_path = Path(f"/storage/research/cinn_comp/ThalSR/zan/derivatives/test/practice/scanID/{scan_id}")
    to_path = Path(f"/storage/research/cinn_comp/ThalSR/zan/derivatives/test/practice/sessionID/{session_id}/anat")
    if not os.path.exists(from_path):
        print(f"{from_path} does not exist!")
        continue
    print(f"Moving from {from_path} to {to_path}")
    shutil.move(from_path, to_path)

