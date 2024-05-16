# Load libraries
import pandas as pd
from pathlib import Path
from math import isnan
import os
import json

# Define constants
ROOT_PATH = "/storage/research/cinn_comp/ThalSR/zan/derivatives/test/casper" #rename this!!!!!
MODALITY = "MR"
BODY_PART_EXAMINED = "HEAD"
MR_ACQUISIITON_TYPE = "3D"

# Create dataframe from excel file
df = pd.read_excel("FTHP_Metadata.xlsx", sheet_name='data')

# Loops through all the rows in the dataframe
for index,row in df.iterrows():

    scan_id = row["scanID"]
    session_id = row["sessionID"]
    repeat_id = row["repeatID"]
    
    # Create scanID folder if it doesn't already exist
    scan_id_path = f"{ROOT_PATH}/sub/sub-{scan_id:03}/anat"
    if not os.path.exists(scan_id_path):
        os.makedirs(scan_id_path)
    
    # Define path that contains the files currently, and the path to which we want to move files to, which also renames the files
    file_name = f"sub-{scan_id:03}_T1w"
    from_nii_path = Path(f"{ROOT_PATH}/scanID/{scan_id}/{scan_id}.nii")
    #from_nii_path = f"/storage/research/cinn_comp/ThalSR/zan/derivatives/test/casper/FTHP/{scan_id}.nii"
    to_nii_path = Path(f"{scan_id_path}/{file_name}.nii")
    to_json_path = Path(f"{scan_id_path}/{file_name}.json")

    # Moves the .nii file to the new folder and renames it to be the correct format
    if os.path.exists(from_nii_path):
        os.rename(from_nii_path, to_nii_path)

    # Skip this is any of the vars are NaNs... IS THIS RIGHT?
    slice_thickness = row["sliceThickness"]
    echo_time = row["echoTime"]
    rep_time = row["repetitionTime"]
    flip_angle = row["flipAngle"]
    if isnan(slice_thickness) or isnan(echo_time) or isnan(rep_time) or isnan(flip_angle):
        continue

    # Create dictionary with current values
    current_obj = {
        "Modality": MODALITY,
        "MagneticFieldStrength": row["fieldStrength"],
        "Manufacturer": row["manufacturer"],
        "ManufacturersModelName": row["model"],
        "BodyPartExamined": BODY_PART_EXAMINED,
        "MRAcquisitionType": MR_ACQUISIITON_TYPE,
        "SeriesDescription": row["seriesDescription"],
        "ProtocolName": row["protocolName"],
        "SliceThickness": slice_thickness,
        "EchoTime": echo_time,
        "RepetitionTime": rep_time,
        "FlipAngle": flip_angle,
        # "BaseResolution": 224,
        # "PhaseEncodingSteps": 186,
        # "AcquisitionMatrixPE": 186,
        # "ReconMatrixPE": 186
        "rows": "cols" #IMPORTANT!!! can replace the unknown values so just ignore those ^^
        # maybe add age_at section too since age is a changing variable
    }

    # Write the object as json to the correct file
    with open(to_json_path, "w", encoding="utf-8") as file:
        json.dump(current_obj, file, ensure_ascii=False, indent=4)
