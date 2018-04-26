import continuous as cont;
import categoricalv2 as cat;
import utils as u;
import view as v;

def main():
    
    file = './dataset/census-income.data.csv';
#    with open(file, "r") as f:
#        raw_csv = f.read()
#        
#    with open(file, "w") as f:
#        f.write("Age,Class of worker,Detailed industry recode,detailed occupation recode,education,wage per hour,unroll in edu inst last week,marital status,major industry code,major occupation code,race,hispanic origin,sex,member of a labor union,reason for unemployment,full or part time employment stat,capital gains,capital losses,dividends from stocks,tax filter stat,region of previous residence,state of previous residence,detailed household and family stat,detailed household summary in household,migration code-change in MSA,migration code-change in REG,migration code-change within REQ,live in this house 1 year ago,migration prev res in sunbelt,num person work for employer,family member under 18,country of birth father,country of birth mother,country of birth self,citizenship,own business or self employed,fill inc questionnaire for veteran's admin,veteran's benefits,weeks work in year,year")
#        f.write(raw_csv)
        
    #continuous = cont.Continuous(file);
    #continuous.draw_DQR();


    categorical = cat.CategoricalV2(file);
    categorical.draw_DQR();
    
#    categorical = cat.Categorical('./dataset/census-income.data.csv');    
#    categorical.draw_DQR();
    
    #view = v.View();
    
    #view.graph_continuous();
    #view.graph_categorical();

    print("Finished");

main()
    
