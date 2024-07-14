# Load libraries
import os

# Change the name of last folder in the line below to the desired dir
ROOT_PATH = "/storage/research/cinn_comp/ThalSR/zan/derivatives/singularity_prep_seg/fmriprep/0-98"

# Move target folders inside a newly created, specified folder
for item in os.listdir(ROOT_PATH):

    # Specify current path
    current_path = ROOT_PATH+"/"+item

    # Ignore everything except for folders in current path
    if not os.path.isdir(current_path):
        continue
    
    # Move inside subfolders in current path, to target location
    current_path+="/anat"
    # Define path to, and create a folder called "T1-THOMAS"
    t1thomas_path = current_path+"/T1-THOMAS"
    if not os.path.exists(t1thomas_path):
        os.makedirs(t1thomas_path)

    # Define original locations of the target folders
    from_left_path = current_path+"/left"
    from_right_path = current_path+"/right"
    from_temp_path = current_path+"/temp"
    from_tempr_path = current_path+"/tempr"
    # Define new locations for the target folders
    to_left_path = t1thomas_path+"/left"
    to_right_path = t1thomas_path+"/right"
    to_temp_path = t1thomas_path+"/temp"
    to_tempr_path = t1thomas_path+"/tempr"

    # Move target folders
    if os.path.exists(from_left_path):
        os.rename(from_left_path, to_left_path)
    if os.path.exists(from_right_path):
        os.rename(from_right_path, to_right_path)
    if os.path.exists(from_temp_path):
        os.rename(from_temp_path, to_temp_path)
    if os.path.exists(from_tempr_path):
        os.rename(from_tempr_path, to_tempr_path)


