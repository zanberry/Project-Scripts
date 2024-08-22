# Load libraries
import pandas as pd
import xml.etree.ElementTree as ET
import csv
from pathlib import Path
import os

ROOT = "/storage/research/cinn_comp/ThalSR/zan/derivatives/evalseg_output"
NUCLEI_LIST_1 = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
NUCLEI_LIST_2 = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
SEG_LIST = ["t1thomas", "hipsthomas", "freesurfer"]

# Extracts relevant information from the .xml file
def extract_avgdist(filepath):
    
    tree = ET.parse(filepath)
    # Get the parent tag of the xml document
    root = tree.getroot()

    # Check if missing AVGDIST value
    r_avgdist = "NA"
    avgdist = root.find("metrics/AVGDIST")
    if avgdist != None:
        r_avgdist = avgdist.attrib["value"]
    else:
        print(f"No avgdist in: {filepath}")

    return r_avgdist

infos = []

missingsubs = []

for sub in range(0,557):
    for seg in SEG_LIST:

        if not Path(f"{ROOT}/sub-{sub}/{seg}").exists():
            continue

        for hemisphere in ["left", "right"]:
            for nuclei1 in NUCLEI_LIST_1:
                for nuclei2 in NUCLEI_LIST_2:
                
                    path_to = f"{ROOT}/sub-{sub}/{seg}/{hemisphere}/sub-{sub}_evalseg_{hemisphere}_KM-{nuclei1}_T1-{nuclei2}.xml"

                    if not Path(path_to).exists(): 
                        print(f"{path_to} does not exist, skipped!")
                        missingsubs.append(sub)
                        continue

                    # print(f"Running {path_to}")

                    avgdist = extract_avgdist(path_to)
                    info = [ sub, seg, hemisphere, nuclei1, nuclei2, avgdist ]

                    infos.append(info)

print(set(missingsubs))

# Create and write in csv
with open('fthp_metrics_wfreesurfer.csv', 'w', newline='') as file:
    
    # Define var to write inside csv
    writer = csv.writer(file)
    # Define var which is a list of col names
    field = ["scanID","segmethod","hemisphere","nuclei1", "nuclei2", "AVGDIST"]

    # Write col names
    writer.writerow(field)
    # Write row values
    writer.writerows(infos)