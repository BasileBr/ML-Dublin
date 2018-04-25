import continuous as cont;
import categorical as cat;
import utils as u;
import view as v;

def main():
    
    file = './dataset/census-income.data.csv';
    header = ["AAGE","ACLSWKR","ADTIND","ADTOCC","AHGA","AHRSPAY","AHSCOL","AMARITL","AMJIND","AMJOCC","ASEX","AREORGN","AUNMEM","AUNTYPE","AWKSTAT","CAPGAIN","CAPLOSS","DIVVAL","FILESTAT","GRINREG","GRINST","HHDFMX","HHDREL","MIGMTR1","MIGMTR3","MIGMTR4","MIGSAME","MIGSUN","NOEMP","PARENT","PEFNTVTY","PEMNTVTY","PENATVTY","PRCITSHP","SEOTR","VETQVA","VETYN","WKSWORK"];
        
    
    print(len(header))
    continuous = cont.Continuous(file, header);
    continuous.draw_DQR();

#    categorical = cat.Categorical('./dataset/census-income.data.csv');    
#    categorical.draw_DQR();
    
#    view = v.View();
#    
#    view.graph_continuous();
#    view.graph_categorical();
    print("Finished");

main()
    
