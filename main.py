import continuous as cont;
import categorical as cat;
import view as v;

def main():
    continuous = cont.Continuous();
    continuous.draw_DQR();

    categorical = cat.Categorical();    
    categorical.draw_DQR();
    
    view = v.View();
    
    view.graph_continuous();
    view.graph_categorical();
    print("Finished");

main()
    
