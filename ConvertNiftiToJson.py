import json
from pathlib import Path
import SimpleITK as sitk

# get list of .nii.gz files inside the given dataFolder
dataFolder = Path("/storage/research/cinn_comp/ThalSR/zan/FTHP")
image_paths = filter(lambda f: str(f).endswith(".nii"), dataFolder.iterdir())


for image_path in image_paths:
    # read image
    itk_image = sitk.ReadImage(image_path)

    # get metadata dict
    header = {k: itk_image.GetMetaData(k) for k in itk_image.GetMetaDataKeys()}
    # create unique name for header file
    header_json_file = f"{image_path.name.replace('.nii','')}.json"

    # save dict in header file
    with open(header_json_file, "w") as outfile:
        json.dump(header, outfile, indent=4)
