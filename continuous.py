import numpy as np
import pandas as pd
import plotly as ply

class Continuous:
    
    def __init__(self,fileCSV=None):
        
        if fileCSV is None:
            self.pathBank = './'
            self.fileCSV = pd.read_csv(filepath_or_buffer=self.pathBank,delimiter = ';', header=0, index_col=0)
        else:
            self.fileCSV = fileCSV
            
        self.continuous = self.fileCSV.select_dtypes(include=[np.number])
        self.pathFileResult = './Data/Results/DQR-ContinuousFeatures.csv'
    
    def get_continuous(self):
        print("continuous : ",self.continuous)
        if self.continuous is not None:
            print("Continuous is not None")
            return self.continuous
        else:
            print("Continuous is None")
            return pd.read_csv(filepath_or_buffer=self.pathFileResult)
    
    def write_results(self):
        pd.DataFrame(self.continuous).to_csv(path_or_buf=self.pathFileResult)
    
    def draw_DQR(self):
        
        tableContinuous = self.get_continuous()
        for feature,value in tableContinuous.items():                
            print(value)
            #print(feature)
#            count = len(value)
#            ERROR HERE TO FIX TO SAVE DATA IN CSV IN FUTUR
#            nbMiss = 0
#            for i in range(count):
#                val = value[i]
#                if val == ' ?':
#                    nbMiss += 1
#                    self.setMissingFeatures('Miss',value)
#            #print((nbMiss / count) * 100)
#            
#
            unique_value = len(set(tableContinuous))
            #print(unique_value)
            # Create & save plots
            #print(value)
            '''
            if unique_value >= 10:
                
                ply.offline.plot({
                    "data": [
                        ply.graph_objs.Histogram(
                            x=tableContinuous[feature]
                        )
                    ],
                    "layout": ply.graph_objs.Layout(
                        title="Histogram of feature \"" + feature + "\" - cardinality >=10"
                    )
                }, filename="./Data/HTML/Continuous/%s.html" % feature)
            else:
                ply.offline.plot({
                    "data": [
                        ply.graph_objs.Bar(
                            x=tableContinuous[feature].value_counts().keys(),
                            y=tableContinuous[feature].value_counts().values
                        )
                    ],
                    "layout": ply.graph_objs.Layout(
                        title="Bar plot for feature \"" + feature + "\" - cardinality <10"
                    )
                }, filename="./Data/HTML/Continuous/%s.html" % feature)
                    
                    '''
    def launch_test(self):
        csvFile = self.get_csv_file()
        #self.write_results()
        
        self.draw()
        
Continuous().launch_test()