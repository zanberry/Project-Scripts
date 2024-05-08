import os

# Loop through specified folder, adding new folders in the specified numbered range
for count in range (1, 158):
    # Also add a subfolder to each folder
    os.makedirs("/storage/research/cinn_comp/ThalSR/zan/derivatives/test/sessionID/ses-{:0d}/anat".format(count))

print("Created sessionID folders!")