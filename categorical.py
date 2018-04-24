import numpy as np
import pandas as pd
import plotly as ply

class Categorical:
    
    def __init__(self,fileCSV=None):
        
        if fileCSV is None:
            self.pathBank = './dataset/dataset.csv'
            self.fileCSV = pd.read_csv(filepath_or_buffer=self.pathBank,delimiter = ',', header=0, index_col=1)
        else:
            self.fileCSV = fileCSV
            
        self.categorical = self.fileCSV.select_dtypes(exclude=[np.number])
        self.pathFeatures = './results/categorical_features.csv';
        self.pathDQR = './results/DQR_categorical.csv';
    
    def get_categorical(self):
        
        if self.categorical is not None:
            return self.categorical
        else:
            return pd.read_csv(filepath_or_buffer=self.pathFeatures)
    
    def write_results(self, table=None, header_columns=None, path=None):
        if table is None and path is None:
            pd.DataFrame(self.categorical).to_csv(path_or_buf=self.pathFeatures);
        else:
            pd.DataFrame(table).to_csv(path_or_buf=path, header = header_columns, index = False);
        
    def draw_DQR(self):
        
        categorical_header = ["Feature name","Count","% Miss", "Card", "Mode"]#, "Mode freq", "Mode %","2nd Mode","2nd mode freq","2nd Mode %" ]
        categorical_columns = self.get_categorical();
        categorical_features_table = [];
        
        for col in categorical_columns:
            
#            Feature name
            feature = [col];
            
#            Feature count
            count = self.categorical[col].size;
            feature.append(count);
            
#            Feature % Miss
            nb_miss = self.categorical[col].isnull().sum();
            print(self.categorical[col].str.contains("?").value_counts()[True])
            miss_pourcentage = (nb_miss/self.categorical[col].size) * 100;
            feature.append(miss_pourcentage);
            
#            Feature cardinality
            cardinality = self.categorical[col].unique().size;
            feature.append(cardinality);
            
#            Mode
            mode = np.max(self.categorical[col].value_counts());
            feature.append(mode);
#            
##            Mode frequency
#            mode_f = 
#            feature.append(mode_f);
#            
##            Mode %
#            mode_p =   
#            feature.append(mode_p);
#            
##            2nd mode
#            bis_mode = 
#            feature.append(bis_mode);
#            
##            2nd mode frequency
#            bis_mode_f = ;
#            feature.append(bis_mode_f);
#            
##            2nd mode %
#            bis_mode_p = ;
#            feature.append(bis_mode_p);            
                
            categorical_features_table.append(feature);
            
#        Write continuous table
        self.write_results();
#        Write continuous features table
        self.write_results(categorical_features_table, categorical_header, self.pathDQR);
      
                
Categorical().draw_DQR();