import numpy as np
import pandas as pd
import plotly as ply

class Continuous:
    
    def __init__(self,fileCSV=None):
        
        if fileCSV is None:
            self.pathBank = './dataset/dataset.csv'
            self.fileCSV = pd.read_csv(filepath_or_buffer=self.pathBank,delimiter = ',', header=0, index_col=0)
        else:
            self.fileCSV = fileCSV
            
        self.continuous = self.fileCSV.select_dtypes(include=[np.number])
        self.pathFileResult = './results/DQR-ContinuousFeatures.csv';
        
    def get_continuous(self):        
        if self.continuous is not None:
            return self.continuous
        else:
            return pd.read_csv(filepath_or_buffer=self.pathFileResult)
    
    def write_results(self):
        pd.DataFrame(self.continuous).to_csv(path_or_buf=self.pathFileResult)
        
    def draw_DQR(self):
        
        continuous_columns = self.continuous;  
        continuous_header = ["Features","Count","% Miss", "Card", "Min", "1st Qrt", "Mean","Median","3rd Qrt", "std" ]
        continuous_features_table = []
        
        for col in continuous_columns:
            feature = [col]
            feature.append(self.continuous[col].size)
            feature.append((self.continuous[col].isnull().sum()/self.continuous[col].size) * 100)
            feature.append(self.continuous[col].unique().size)
            feature.append(np.min(self.continuous[col]))
            feature.append(np.percentile(self.continuous[col],25))
            feature.append(np.mean(self.continuous[col]))
            feature.append(np.percentile(self.continuous[col],50))
            feature.append(np.percentile(self.continuous[col],75))
            feature.append(np.std(self.continuous[col]))
                
            continuous_features_table.append(feature);

        print(continuous_features_table);
            


cont = Continuous();
#cont.write_results();
#cont.get_continuous();
cont.draw_DQR();
