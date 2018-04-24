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
            
        self.continuous = self.fileCSV.select_dtypes(include=['integer'])
        self.pathContinuousFeatures = './results/continuous_features.csv';
        self.pathDQR = './results/DQR_continuous.csv';
        
    def get_continuous(self):        
        if self.continuous is not None:
            return self.continuous
        else:
            return pd.read_csv(filepath_or_buffer=self.pathContinuousFeatures)
    
    def write_results(self, table=None, header_columns=None, path=None):
        if table is None and path is None:
            pd.DataFrame(self.continuous).to_csv(path_or_buf=self.pathContinuousFeatures);
        else:
            pd.DataFrame(table).to_csv(path_or_buf=path, header = header_columns, index = False);
        
    def draw_DQR(self):
        
        continuous_header = ["Feature name","Count","% Miss", "Card", "Min", "1st Qrt", "Mean","Median","3rd Qrt","Max", "Standard deviation" ]
        continuous_columns = self.get_continuous();
        continuous_features_table = [];
        
        for col in continuous_columns:
            
#            Feature name
            feature = [col];
            
#            Feature count
            count = self.continuous[col].size;
            feature.append(count);
            
#            Feature % Miss
            miss_pourcentage = (self.continuous[col].isnull().sum()/self.continuous[col].size) * 100;
            feature.append(miss_pourcentage);
            
#            Feature cardinality
            cardinality = self.continuous[col].unique().size;
            feature.append(cardinality);
            
#            Min value of the feature
            min_value = np.min(self.continuous[col]);
            feature.append(min_value);
            
#            1st quarter
            first_quarter = self.continuous[col].quantile(0.25);
            feature.append(first_quarter);
            
#            Feature mean
            mean = np.round(np.mean(self.continuous[col]), decimals=2);  
            feature.append(mean);
            
#            Feature median
            median = self.continuous[col].quantile(0.5);
            feature.append(median);
            
#            3rd quarter
            third_quarter = self.continuous[col].quantile(0.75);
            feature.append(third_quarter);
            
#            Feature max
            max_value = np.max(self.continuous[col]);
            feature.append(max_value);            
            
#            Feature standard deviation
            std = np.round(np.std(self.continuous[col]), decimals=2);
            feature.append(std);
                
            continuous_features_table.append(feature);
            
#        Write continuous table
        self.write_results();
#        Write continuous features table
        self.write_results(continuous_features_table, continuous_header, self.pathDQR);
 


cont = Continuous();
cont.draw_DQR();
