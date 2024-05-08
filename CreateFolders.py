import os

# Loop through specified folder, adding new folders in the specified numbered range
for count in range (0, 557):
    # Also add a subfolder to each folder
    os.makedirs("/storage/research/cinn_comp/ThalSR/zan/derivatives/sub-0{:0d}/anat".format(count))

