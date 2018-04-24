import numpy as np
import pandas as pd
import plotly as ply
from scipy import stats

class CategoricalFeatures:
    
    def __init__(self,fileCSV=None):
        print('start');
        if fileCSV is None:
            self.pathFeatures = './dataset/dataset.csv'
            self.fileCSV = pd.read_csv(filepath_or_buffer=self.pathFeatures,delimiter = ',', header=0, index_col=1)
        else:
            self.fileCSV = fileCSV
            
        self.categorical = self.fileCSV.select_dtypes(exclude=['int_', 'float64'])
        self.pathFileResult = './results/DQR-categorical_features.csv';
        self.pathDQR = './results/DQR_categoral.csv';
    
    def get_categoral(self):        
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
        
        categoral_header = ["Feature name","Count","% Miss", "Card", "Mode", "Mode Freq", "Mode %","2nd Mode","2nd Mode Freq","2nd Mode %"]
        categoral_columns = self.get_categoral();
        categoral_features_table = [];
            
            
        for col in categoral_columns:
            print('Affichage de la colonne')
            print(self.categorical[col]);
            
#            Feature name
            feature = [col];
            
#            Feature count
            count = self.categorical[col].size;
            feature.append(count);
            
#            Feature % Miss
            miss_pourcentage = (self.categorical[col].isnull().sum()/self.categorical[col].size) * 100;
            feature.append(miss_pourcentage);
            
#            Feature cardinality
            cardinality = self.categorical[col].unique().size;
            feature.append(cardinality);
            
#           Feature Mode
            modeTab = stats.mode(self.categorical[col]);
            mode =  modeTab[0] 
            countMode = modeTab[1];
            feature.append(mode);
            count = len(self.categorical[col])
            print(count)
#           Feature Mode Freq
            modeFreq = (float(countMode) / count) * 100
            print(modeFreq)
            feature.append(np.argmax(modeFreq));
            
            
#           Feature Mode %
#            modePercent = max(self.categorical[col].values())/sum(self.categorical[col].values()),            
#            feature.append(modePercent);
#           Write continuous table
            self.write_results();
#           Write continuous features table
            self.write_results(categoral_features_table, categoral_header, self.pathDQR);
 
            
            
cont = CategoricalFeatures();
cont.draw_DQR();

 