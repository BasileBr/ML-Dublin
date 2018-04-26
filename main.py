import continuous as cont;
import categorical as cat;
import utils as u;
from sklearn import tree;
from sklearn.datasets import load_iris
import graphviz
    
    
def main():
    
    file = './dataset/census-income.data.csv';
#    with open(file, "r") as f:
#        raw_csv = f.read()
#        
#    with open(file, "w") as f:
#        f.write("age,class of worker,detailed industry recode,detailed occupation recode,education,wage per hour,unroll in edu inst last week,marital status,major industry code,major occupation code,race,hispanic origin,sex,member of a labor union,reason for unemployment,full or part time employment stat,capital gains,capital losses,dividends from stocks,tax filter stat,region of previous residence,state of previous residence,detailed household and family stat,detailed household summary in household,instance weight,migration code-change in MSA,migration code-change in REG,migration code-change within REQ,live in this house 1 year ago,migration prev res in sunbelt,num person work for employer,family member under 18,country of birth father,country of birth mother,country of birth self,citizenship,own business or self employed,fill inc questionnaire for veteran's admin,veteran's benefits,weeks work in year,year")
#        f.write(raw_csv)
        
#    continuous = cont.Continuous(file);
#    continuous.draw_DQR();
#
#
#    categorical = cat.Categorical(file);
#    categorical.draw_DQR();

#    utils = u.Utils();
#    
#    utils.graph_continuous();
#    utils.graph_categorical();

	
#    Classification
    X = [[0, 0], [1, 1]];
    Y = [0, 1];
    clf = tree.DecisionTreeClassifier();
    clf = clf.fit(X, Y);
    clf.predict([[2., 2.]])
    
    iris = load_iris()
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(iris.data, iris.target)
    
    dot_data = tree.export_graphviz(clf, out_file=None); 
    graph = graphviz.Source(dot_data);
    graph.render("iris");
    
    print("Finished");

main()
    
