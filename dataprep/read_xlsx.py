# Load libraries
import pandas as pd
from pathlib import Path

# Assign path to the excel file to a variable
filepath_metadata = r'/storage/research/cinn_comp/ThalSR/zan/scripts/dataprep/FTHP_Metadata.xlsx'
# Create a pandas dataframe from an excel file
df = pd.read_excel(filepath_metadata, index_col="scanID", sheet_name="hardware")
# Convert pandas dataframe to a csv
df.to_csv('fthp_hardware.csv')
