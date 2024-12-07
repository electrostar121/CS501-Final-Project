import requests

class h5Cloud:
    def __init__(self, ip):
        self.ip = ip if ip[-1] == '/' else ip + '/'
        
    def listFiles(self):
        respone = requests.get(self.ip + 'ListFiles')
        
        return respone.json()['files']
    
    def selectFile(self, FileName):
        respone = requests.get(self.ip + 'SetFile/' + FileName)
        
        return self
    
    def listContents(self):
        respone = requests.get(self.ip + 'ListContents')
        
        return respone.json()['contents']
    
    def image(self, image):
        respone = requests.get(self.ip + 'Image/' + image)
        
        return self
    
    def flip(self, axis=0):
        respone = requests.get(self.ip + 'Flip/' + str(axis))
        
        return self
    
    def scale(self, xFactor, yFactor, down=True):
        respone = requests.get(self.ip + 'Scale/' + str(xFactor) + '/' + str(yFactor) + '/' + str(1 if down else 0))
        
        return self
    
    def crop(self, xStart, yStart, xEnd, yEnd):
        respone = requests.get(self.ip + 'Crop/' + str(xStart) + '/' + str(yStart) + '/' + str(xEnd) + '/' + str(yEnd))
        
        return self
    
    def invert(self):
        respone = requests.get(self.ip + 'Invert')
        
        return self
    
    def reduction(self, factor):
        respone = requests.get(self.ip + 'Reduction/' + str(factor))
        
        return self
    
    def pad(self, xBefore, xAfter, yBefore, yAfter, mode='constant'):
        respone = requests.get(self.ip + 'Pad/' + str(xBefore) + '/' + str(xAfter) + '/' + str(yBefore) + '/' + str(yAfter) + '/' + mode)
        
        return self
        
    def getImage(self):
        response = requests.get(self.ip + 'GetImage')
        
        return response.json()['data']