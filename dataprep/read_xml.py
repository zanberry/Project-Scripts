# Load libraries
import pandas as pd
import xml.etree.ElementTree as ET
import csv
from pathlib import Path
import os

ROOT = "/storage/research/cinn_comp/ThalSR/zan/derivatives/evalseg_output"
NUCLEI_LIST = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
SEG_LIST = ["t1thomas", "hipsthomas"]

# Extracts relevant information from the .xml file
def extract_info(filepath):
    
    tree = ET.parse(filepath)
    # Get the parent tag of the xml document
    root = tree.getroot()
    # Get the name of the moving image file (discards rest of the path)
    filename = Path(root.find("moving-image").attrib["filename"]).name

    # Remove file extensions
    filename = filename.split(".")[0]
    # Replace hyphens with underscores
    filename = filename.replace("-", "_")
    # Split filenames by underscores and turn them into a list
    file_info = filename.split("_")

    # Check if missing AVGDIST value
    r_avgdist = "NA"
    avgdist = root.find("metrics/AVGDIST")
    if avgdist != None:
        r_avgdist = avgdist.attrib["value"]
    else:
        print(f"No avgdist in: {filepath}")

    # Return all relvant values, skipping "sub-"
    return [
        file_info[1],
        file_info[2],
        file_info[3],
        file_info[4],
        r_avgdist   
    ]

infos = []

for sub in range(0,557):
    for seg in SEG_LIST:
        for nuclei in NUCLEI_LIST:
            
            # Define paths
            path_to_left_xml = f"{ROOT}/sub-{sub}/{seg}/left/sub-{sub}_evalseg_left_KM-{nuclei}_T1-{nuclei}.xml"
            path_to_right_xml = f"{ROOT}/sub-{sub}/{seg}/right/sub-{sub}_evalseg_right_KM-{nuclei}_T1-{nuclei}.xml"

            if Path(path_to_left_xml).exists():
                infos.append(extract_info(path_to_left_xml))

            if Path(path_to_right_xml).exists():
                infos.append(extract_info(path_to_right_xml))

# Create and write in csv
with open('metrics.csv', 'w', newline='') as file:
    
    # Define var to write inside csv
    writer = csv.writer(file)
    # Define var which is a list of col names
    field = ["scanID","segmethod","hemisphere","nuclei","AVGDIST","manufacturerCode","model","field"]

    # Write col names
    writer.writerow(field)
    # Write row values
    writer.writerows(infos)