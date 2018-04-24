import numpy as np
import pandas as pd
import plotly as ply

class CategoricalFeatures:
    
    def __init__(self,fileCSV=None):
        
        if fileCSV is None:
            self.pathBank = './dataset/dataset.csv'
            self.fileCSV = pd.read_csv(filepath_or_buffer=self.pathBank,delimiter = ',', header=0, index_col=1)
        else:
            self.fileCSV = fileCSV
            
        self.categorical = self.fileCSV.select_dtypes(exclude=[np.number])
        self.pathFileResult = './results/DQR-CategoricalFeatures.csv';
        print(self.categorical)
    
    def getCategoricalFeatures(self):
        print("CategoricalFeatures : ",self.categorical)
        if self.categorical is not None:
            #print("CategoricalFeatures is not None")
            return self.categorical
        else:
            #print("CategoricalFeatures is None")
            return pd.read_csv(filepath_or_buffer=self.pathFileResult)
    
    def write_results(self):
        pd.DataFrame(self.categorical).to_csv(path_or_buf=self.pathFileResult)
    
    def draw_DQR(self):
        
        tableCategoralcalls = self.getCategoralCalls()          
        print(tableCategoralcalls);            
                
CategoricalFeatures().write_results();