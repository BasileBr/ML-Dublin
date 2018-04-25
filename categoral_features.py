#Julien LE GUILLANT IMR2
import numpy as np
import pandas as pd
import collections
class CategoricalFeatures:
    
#   Init    
    def __init__(self,fileCSV=None):
        if fileCSV is None:
            self.pathFeatures = './dataset/dataset.csv'
            self.fileCSV = pd.read_csv(filepath_or_buffer=self.pathFeatures,delimiter = ',', header=0, index_col=1)
        else:
            self.fileCSV = fileCSV
            
        self.categorical = self.fileCSV.select_dtypes(exclude=['int_', 'float64'])
        self.pathFileResult = './results/DQR-categorical_features.csv';
        self.pathDQR = './results/DQR_categorical.csv';
        self.__categorical_features_table = []
    
    def get_categorical(self):        
        if self.categorical is not None:
            return self.categorical
        else:
            return pd.read_csv(filepath_or_buffer=self.pathFeatures)
        
#   Write data in csv file from tab    
    def write_results(self, table=None, header_columns=None, path=None):
        if table is None and path is None:
            pd.DataFrame(self.categorical).to_csv(path_or_buf=self.pathFeatures);
        else:
            pd.DataFrame(table).to_csv(path_or_buf=path, header = header_columns, index = False);
        
             
    def draw_DQR(self):
        categorical_header = ["Feature name","Count","% Miss", "Card", "Mode", "Mode Freq", "Mode %","2nd Mode","2nd Mode Freq","2nd Mode %"]
        categorical_columns = self.get_categorical();
        categorical_features_table = [];
        i = 0;
        j = 1;
        for cat_name in categorical_columns:  
            print(cat_name,"cat_name")
            countWrongItem = 0;
#           We get all the column of the category in the CSV file
            dataFeature = self.fileCSV[cat_name]
            print(dataFeature)
#           We make a dictionnary to be granted to put string keys
            feature =  collections.OrderedDict()
            print(len(dataFeature.value_counts()))
            for index in dataFeature.index:
                if "?" in index:
                    #print(countWrongItem, " = NB of ?");   
                    countWrongItem = countWrongItem + 1 
                    
            print(dataFeature.value_counts());
            #print(dataFeature.value_counts()[0]);
#           ut in the table feature the name of the feature
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
            print(j, " column added in csv file ..")
            j = j + 1
            print(countWrongItem, " = NB of ?");   
#           Write continuous table
            self.write_results();
#           Write continuous features table
            self.write_results(self.__categorical_features_table,categorical_header, self.pathDQR);

CategoricalFeatures().draw_DQR();
print("Finished")

 