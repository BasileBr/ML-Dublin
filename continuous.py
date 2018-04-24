import numpy as np
import pandas as pd
import collections

class Continuous:
    
    def __init__(self,fileCSV=None):
        
        if fileCSV is None:
            self.pathBank = './dataset/dataset.csv'
            self.fileCSV = pd.read_csv(filepath_or_buffer=self.pathBank,delimiter = ',', header=0, index_col=1)
        else:
            self.fileCSV = fileCSV
            
        self.continuous = self.fileCSV.select_dtypes(include=[np.number])
        self.pathFeatures = './results/continuous-features.csv';
        self.pathDQR = './results/E-DQR-continuous.csv';
        
    def get_continuous(self):        
        if self.continuous is not None:
            return self.continuous
        else:
            return pd.read_csv(filepath_or_buffer=self.pathFeatures)
    
    def write_results(self, table=None, header_columns=None, path=None):
        if table is None and path is None:
            pd.DataFrame(self.continuous).to_csv(path_or_buf=self.pathFeatures);
        else:
            pd.DataFrame(table).to_csv(path_or_buf= path, header= header_columns, index= False);
        
    def draw_DQR(self):
        
        
        self.__continuous_features_table = [];
        self.__continuous_header = ["Feature name","Count","% Miss", "Card", "Min", "1st Qrt", "Mean","Median","3rd Qrt","Max", "Standard deviation" ]
        continuous_columns = self.get_continuous();
        
        for cat in continuous_columns:
            
            dataFeature = self.fileCSV[cat];
            feature = collections.OrderedDict();
            
            feature['nameFeature'] = cat;
            feature['countTotal'] = dataFeature.size;
            feature['% Miss'] = dataFeature.isnull().sum()/ dataFeature.size * 100;
            feature['cardTotal'] = np.unique(dataFeature).size;
            feature['min'] = np.min(dataFeature);
            feature['firstQuarter'] = np.percentile(dataFeature, 25);
            feature['mean'] = round(np.mean(dataFeature), 2);
            feature['median'] = np.percentile(dataFeature, 50);
            feature['thirdQuarter'] = np.percentile(dataFeature, 75);
            feature['max'] = np.max(dataFeature);
            feature['std'] = np.std(dataFeature);
            self.__continuous_features_table.append(feature); 
            
#        Write continuous table
        self.write_results();
#        Write DQR continuous
        self.write_results(self.__continuous_features_table, self.__continuous_header, self.pathDQR);

cont = Continuous();
cont.draw_DQR()