import os
from pathlib import Path

# Specify paths where the files are stored
nii_from = Path("/storage/research/cinn_comp/ThalSR/zan/FTHP")
#json_from = Path("/storage/research/cinn_comp/ThalSR/zan/derivatives/FTHP_jsons")
# Define root path
root_path = "/storage/research/cinn_comp/ThalSR/zan/derivatives/test/scanID"

# Select json and nii files
nii_files = filter(lambda f: str(f).endswith(".nii"), nii_from.iterdir())
#json_files = filter(lambda f: str(f).endswith(".json"), json_from.iterdir())

# Move nii files
for file in nii_files:
    p = Path(file).stem
    #os.rename(file, root_path+"/"+p+"/"+p+".json")
    #os.rename(file, root_path+"/"+p+"/"+"/anat/"+"/"+p+".nii")
    os.rename(file, root_path+"/"+p+"/"+p+".nii")
    print(p)

# Move json files
#for file in json_files:
#    p = Path(file).stem
#    #os.rename(file, root_path+"/"+p+"/"+p+".json")
#    #os.rename(file, root_path+"/"+p+"/"+"/anat/"+"/"+p+".json")
#    os.rename(file, root_path+"/"+p+"/"+"/anat/"+"/"+p+".json")
#    print(p)

