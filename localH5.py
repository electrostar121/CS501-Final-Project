import h5py
import os
import numpy as np
from PIL import Image

defaultLocation = '/data/HDF5files/'

contents = []
def saveContents(name):
    contents.append(name)
    
class h5Ext:
    def __init__(self, location=None):
        self.location = defaultLocation if location is None else (location if location[-1] == '/' else location + '/')
        self.file = None
        self.data = None
        self.files = None
        self.contents = []
        
    def listFiles(self): # List all files in the directory of the current location
        self.files = os.listdir(self.location)
        
        return self
    
    def selectFile(self, FileName): # Select the H5 file to use
        self.file = FileName
        
        return self
        
    def listContents(self): # List the structure of the H5 file
        if self.file is None:
            print('ERROR! No file selected.')
            return
        
        if os.path.isfile(self.location + self.file) is False:
            print('ERROR! File does not exist.')
            return
        
        self.contents = []
        with h5py.File(self.location + self.file, 'r') as h5f:
            h5f.visit(saveContents)
        self.contents = contents
        
        return self
            
    def newH5File(self, name): # Create a new H5 file
        with h5py.File(self.location + name, 'w') as h5f:
            pass
        
        self.file = name
        
        return self
        
    def newData(self, file): # Add a new image to the H5 file
        with h5py.File(self.location + self.file, 'a') as h5f:
            img = Image.open(file)
            data = np.asarray((img), dtype="uint8")
            h5f.create_dataset('images/' + file.split('/')[-1], data=data, dtype='uint8')
            dset = h5f.get('images/' + file.split('/')[-1])
            dset.attrs["CLASS"] = np.bytes_('IMAGE')
            dset.attrs["IMAGE_VERSION"] = np.bytes_("1.2")
            arr = np.asarray([0, 255], dtype = np.uint8)
            dset.attrs["IMAGE_MINMAXRANGE"] = list(arr)
            dset.attrs["IMAGE_SUBCLASS"] = np.bytes_('IMAGE_TRUECOLOR')
            dset.attrs["INTERLAVE_MODE"] = np.bytes_('INTERLACE_PIXEL')
            
    def image(self, image): # Set the data from the image
        with h5py.File(self.location + self.file) as h5f:
            self.data = h5f['images'][image][()]
            
        return self
    
    def flip(self, axis=0): # Flip the image, if axis is set to 1 than flip x-axis, otherwise flip on y-axis
        if self.data is None:
            print('Error! No data.')
            return self
        
        if axis == 1:
            self.data = self.data[:, ::-1]
        else:
            self.data = self.data[::-1, :]
            
        return self
    
    def scale(self, xFactor, yFactor, down=True): # Scale the image up or down
        if self.data is None:
            print('Error! No data.')
            return self
        
        if down:
            self.data = self.data[::xFactor, ::yFactor]
        else:
            self.data = self.data.repeat(xFactor, axis=0).repeat(yFactor, axis=1)
        
        return self
    
    def crop(self, xStart, yStart, xEnd, yEnd): # Crop the image
        if self.data is None:
            print('Error! No data.')
            return self
        
        if xStart >= xEnd or yStart >= yEnd:
            print('Error! Starting coord(s) bigger than or equal to ending coord(s).')
            return self
        
        if xStart < 0 or yStart < 0:
            print('Error! Starting coord(s) cannot be less than 0.')
            return self
        
        if xEnd > self.data.shape[0] or yEnd > self.data.shape[1]:
            print('Error! Ending coord(2) cannot be greater than image size.')
            return self
        
        self.data = self.data[xStart:xEnd, yStart:yEnd]
        
        return self
    
    def invert(self): # Invert the colors of the image
        if self.data is None:
            print('Error! No data.')
            return self
        
        self.data = 255 - self.data
        
        return self
    
    def reduction(self, factor): # Reduce the color the image by a factor
        if self.data is None:
            print('Error! No data.')
            return self
        
        self.data = self.data // factor * factor
        
        return self
    
    def pad(self, xBefore, xAfter, yBefore, yAfter, mode='constant'): # Pad the edges of the image
        if self.data is None:
            print('Error! No data.')
            return self
        
        if mode == 'constant':
            self.data = np.pad(self.data, ((xBefore, xAfter), (yBefore, yAfter), (0, 0)), mode='constant', constant_values=0)
        else:
            self.data = np.pad(self.data, ((xBefore, xAfter), (yBefore, yAfter), (0, 0)), mode=mode)
        
        return self