import cv2 as cv
import numpy as np
from pathlib import Path
import pandas as pd

subnotebooks = Path.cwd()
notebooks_path = subnotebooks.parent
repo_path = notebooks_path.parent

class path_label():
    """Class to access paths and labels from csv
    """
    def __init__(self, meta=pd.read_csv(str(repo_path) + '/data/meta_info.csv', sep='\t'), classif='binary', set_name='train') -> None:
        meta = meta.loc[meta['classif'] == classif] #Filter by classif
        meta = meta.loc[meta['set'] == set_name] #Filter by set
        self.paths = list(meta.path)
        self.paths_NH = list(meta.NH_path)
        self. labels = np.array(meta.label)
        self.FOV_x1 = np.array(meta.FOV_x1, dtype=np.int16)
        self.FOV_x2 = np.array(meta.FOV_x2, dtype=np.int16)
        self.FOV_y1 = np.array(meta.FOV_y1, dtype=np.int16)
        self.FOV_y2 = np.array(meta.FOV_y2, dtype=np.int16)
        self.len = len(self.paths)
        
#create class to call patient and its information
class patient():
    """Class to access patient information
    """
    def __init__(self, info = path_label() ,num=0, NH = False) -> None:
        self.path = info.paths[num] if NH == False else info.paths_NH[num]
        self.label = info.labels[num]
        self.FOV_x1 = info.FOV_x1[num]
        self.FOV_x2 = info.FOV_x2[num]
        self.FOV_y1 = info.FOV_y1[num]
        self.FOV_y2 = info.FOV_y2[num]
        self.NH_status = NH
    def RGB_im(self):
        self.image = cv.imread(str(repo_path) +"/"+ self.path)
        self.image = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
        self.image = self.image[self.FOV_x1:self.FOV_x2, self.FOV_y1:self.FOV_y2] if self.NH_status == False else self.image
        return self.image
        
    def HSV_im(self):
        self.HSV = cv.imread(str(repo_path) +"/"+ self.path)
        self.HSV = cv.cvtColor(self.HSV, cv.COLOR_BGR2HSV)
        self.HSV = self.HSV[self.FOV_x1:self.FOV_x2, self.FOV_y1:self.FOV_y2] if self.NH_status == False else self.HSV
        return self.HSV
    
    def gray_im(self):
        self.gray = cv.imread(str(repo_path) +"/"+ self.path)
        self.gray = cv.cvtColor(self.gray, cv.COLOR_BGR2GRAY)
        self.gray = self.gray[self.FOV_x1:self.FOV_x2, self.FOV_y1:self.FOV_y2] if self.NH_status == False else self.gray
        return self.gray
    
    def ycrcb_im(self):
        self.ycrcb = cv.imread(str(repo_path) +"/"+ self.path)
        self.ycrcb = cv.cvtColor(self.ycrcb, cv.COLOR_BGR2YCrCb)
        self.ycrcb = self.ycrcb[self.FOV_x1:self.FOV_x2, self.FOV_y1:self.FOV_y2] if self.NH_status == False else self.ycrcb
        return self.ycrcb