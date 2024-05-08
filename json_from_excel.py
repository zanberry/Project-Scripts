import json
import pandas as pd
from math import isnan

# Constants
MODALITY = "MR"
BODY_PART_EXAMINED = "HEAD"
MR_ACQUISIITON_TYPE = "3D"

# Load FTHP_Metadata excel doc as a pandas dataframe
df = pd.read_excel("FTHP_Metadata.xlsx")

object_list = []

files_skipped = 0
skipped_indexes = []

# Loop through all the rows in data
for index,row in df.iterrows():
    # If one of these variables is NaN, we skip it for now!!!
    slice_thickness = row["sliceThickness"]
    echo_time = row["echoTime"]
    rep_time = row["repetitionTime"]
    flip_angle = row["flipAngle"]
    if isnan(slice_thickness) or isnan(echo_time) or isnan(rep_time) or isnan(flip_angle):
        files_skipped += 1
        skipped_indexes.append(index + 2) # We plus 2 here to map it to the excel file correctly!!!
        continue
    current_dict = {
        "Index": index,
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
        "FlipAngle": flip_angle
        # "BaseResolution": 224,
        # "PhaseEncodingSteps": 186,
        # "AcquisitionMatrixPE": 186,
        # "ReconMatrixPE": 186
    }
    object_list.append(current_dict)

with open("test.json", "w", encoding="utf-8") as file:
    json.dump(object_list, file, ensure_ascii=False, indent=4)

print(f"Finished with {files_skipped} files skipped.")
if len(skipped_indexes) > 0:
    print(f"Skipped indexes: {skipped_indexes}.")
