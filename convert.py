import h5py
import numpy as np
from PIL import Image
import glob

nfiles = len(glob.glob("/home/pwanner/Downloads/dataset/*.png"))

with h5py.File("test.h5", 'w') as h5f:

    for cnt, ifile in enumerate(glob.iglob("/home/pwanner/Downloads/dataset/*.png")):
        if cnt > 100:
            break
        img = Image.open(ifile)

        data = np.asarray((img), dtype="uint8")
        h5f.create_dataset("images/" + ifile.split('/')[-1], data=data, dtype='uint8')
        dset = h5f.get("images/" + ifile.split('/')[-1])
        dset.attrs["CLASS"] = np.bytes_('IMAGE')
        dset.attrs["IMAGE_VERSION"] = np.bytes_("1.2")
        arr = np.asarray([0, 255], dtype = np.uint8)
        dset.attrs["IMAGE_MINMAXRANGE"] = list(arr)
        dset.attrs["IMAGE_SUBCLASS"] = np.bytes_('IMAGE_TRUECOLOR')
        dset.attrs["INTERLAVE_MODE"] = np.bytes_('INTERLACE_PIXEL')