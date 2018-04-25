import continuous as cont;
import categorical as cat;
import utils as u;
import view as v;

def main():
    
    continuous = cont.Continuous('./dataset/census-income.data.csv');
    continuous.draw_DQR();

#    categorical = cat.Categorical('./dataset/census-income.data.csv');    
#    categorical.draw_DQR();
    
#    view = v.View();
#    
#    view.graph_continuous();
#    view.graph_categorical();
    print("Finished");

main()
    
