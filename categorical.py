#Julien LE GUILLANT IMR2
import numpy as np
import pandas as pd
import collections

class Categorical:
    
#   Init    
    def __init__(self,fileCSV=None):
        
        if fileCSV is None:
            self.pathBank = './dataset/dataset.csv'
            self.fileCSV = pd.read_csv(filepath_or_buffer=self.pathBank,delimiter = ',', header=0, index_col=1)
        else:
            self.fileCSV = fileCSV;
            
        self.categorical = self.fileCSV.select_dtypes(exclude=[np.number]);
        self.pathFeatures = './results/categorical-features.csv';
        self.pathDQR = './results/E-DQR-categorical.csv';
        self.__categorical_features_table = [];
    
    def get_categorical(self):
        
        if self.categorical is not None:
            return self.categorical;
        else:
            return pd.read_csv(filepath_or_buffer=self.pathFeatures);
        
#   Write data in csv file from tab    
    def write_results(self, table=None, header_columns=None, path=None):
        
        if table is None and path is None:
            pd.DataFrame(self.categorical).to_csv(path_or_buf=self.pathFeatures);
        else:
            pd.DataFrame(table).to_csv(path_or_buf=path, header = header_columns, index = False);
        
             
    def draw_DQR(self):
        categorical_header = ["Feature name","Count","% Miss", "Card", "Mode", "Mode Freq", "Mode %","2nd Mode","2nd Mode Freq","2nd Mode %"]
        categorical_columns = self.get_categorical();
        
        for cat_name in categorical_columns:   
            
            if cat_name is id:
                continue
            countWrongItem = 0;
#           We get all the column of the category in the CSV file
            dataFeature = self.fileCSV[cat_name]
#            We make a dictionnary to be granted to put string keys
            feature =  collections.OrderedDict()

            for index in dataFeature:
                if "?" in index:
#                   print(countWrongItem, " = NB of ?");   
                    countWrongItem = countWrongItem + 1 
                    
#           Put in the table feature the name of the feature
            feature['nameFeature'] = cat_name
#           Put in the table feature the total count of lines
            feature['countTotal'] = dataFeature.size
                   
            feature['% Miss'] = countWrongItem/ dataFeature.size * 100
            print(feature['% Miss'])
            feature['cardTotal'] = np.unique(dataFeature).size
    
            feature['First Mode'] = dataFeature.value_counts().keys()[0]
            feature['First Mode Freq'] = dataFeature.value_counts()[0]
            feature['First Mode %'] = round(dataFeature.value_counts()[0] / dataFeature.size * 100,2)
            
            feature['Second Mode'] = dataFeature.value_counts().keys()[1]
            feature['Second Mode Freq'] = dataFeature.value_counts()[1]
            feature['Second Mode %'] = round(dataFeature.value_counts()[1] / dataFeature.size * 100,2)
            self.__categorical_features_table.append(feature)   
        
#           Write continuous table
        self.write_results();
#           Write continuous features table
        self.write_results(self.__categorical_features_table,categorical_header, self.pathDQR);