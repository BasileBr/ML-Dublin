import continuous as cont;
import categorical as cat;
import utils as u;
import treemodel as tm;
import pandas as pd;
    
def main():
    
    file = './dataset/census-income.data.csv';
#    with open(file, "r") as f:
#        raw_csv = f.read()
#        
#    with open(file, "w") as f:
#        f.write("age,class of worker,detailed industry recode,detailed occupation recode,education,wage per hour,unroll in edu inst last week,marital status,major industry code,major occupation code,race,hispanic origin,sex,member of a labor union,reason for unemployment,full or part time employment stat,capital gains,capital losses,dividends from stocks,tax filter stat,region of previous residence,state of previous residence,detailed household and family stat,detailed household summary in household,instance weight,migration code-change in MSA,migration code-change in REG,migration code-change within REQ,live in this house 1 year ago,migration prev res in sunbelt,num person work for employer,family member under 18,country of birth father,country of birth mother,country of birth self,citizenship,own business or self employed,fill inc questionnaire for veteran's admin,veteran's benefits,weeks work in year,year")
#        f.write(raw_csv)
#        
#    continuous = cont.Continuous(file);
#    continuous.draw_DQR();
#
#    categorical = cat.Categorical(file);
#    categorical.draw_DQR();
    
        
#    dataset = pd.read_csv(file, delimiter=';')          
#    dataset.head()
#    X = dataset.drop('income', axis=1)  
#    y = dataset['income']  
#    
#    from sklearn.model_selection import train_test_split  
#    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
#    
#    from sklearn.tree import DecisionTreeClassifier  
#    classifier = DecisionTreeClassifier()  
#    classifier.fit(X_train, y_train)  
#    
#    y_pred = classifier.predict(X_test)
#
#    from sklearn.metrics import classification_report, confusion_matrix  
#    print(confusion_matrix(y_test, y_pred))  
#    print(classification_report(y_test, y_pred))      
#    
#    utils = u.Utils();
#    
#    utils.graph_continuous();
#    utils.graph_categorical();


    from pandas import DataFrame
    from sklearn import preprocessing
    from sklearn import tree
    from sklearn.svm import SVC
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import cross_validation
    from sklearn import model_selection
    from sklearn.feature_extraction import DictVectorizer
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    import numpy as np
    import pandas as pd
    
    #import continuous_features as cont
    #import categorical_features as cat
    
    ##############################################
    ##### ##### ##  PREPARING DATA  ## ##### ##### 
    ##############################################
    
    # Get bank
    bank = pd.read_csv(file,delimiter = ';')
    columnHeadings=list(bank.columns)
    
    # Only one target (output)
    target = 'income'
    # Extract target feature
    training_target = bank[target]
    
    ########################
    #### Training bank ####
    ######################
    
    # Training bank means that we only have a little part of data set
    training_bank = bank.sample(4000)
    
    ##################
    ## Testing bank ##
    ##################
    
    # Droping training bank from whole bank
    testing_bank = bank.drop(training_bank.index)
    
    ##############################
    ##      Extracting values   ##
    ## Categorical / Continuous ##
    ##############################
    
    #####  Continuous  #####
    # Column names of continuous features #
    #numeric_cfs =  list(bank.select_dtypes(include=[np.number]).columns)
    numeric_cfs = ['age','detailed industry recode','detailed occupation recode','num person work for employer','own business or self employed','veteran\'s benefits','weeks work in year','year']
    # Data features #
    numeric_dfs = bank[numeric_cfs]
    
    #####  Categorical  #####
    # Extract Categorical Descriptive Features
    cat_dfs = bank.drop(numeric_cfs + [target],axis=1)
    
    # Transpose into array of dictionaries (one dict per instance) of feature:level pairs #
    cat_dfs = cat_dfs.T.to_dict().values()
    
    #########################
    ##   
    ########################
    
    
    #convert to numeric encoding
    vectorizer = DictVectorizer( sparse = False )
    vec_cat_dfs = vectorizer.fit_transform(cat_dfs) 
    # Merge Categorical and Numeric Descriptive Features
    train_dfs = np.hstack((numeric_dfs.as_matrix(), vec_cat_dfs ))
    
    ##---------------------------------------------------------------
    ##   Create and train a decision tree model using sklearn api
    ##---------------------------------------------------------------
    #create an instance of a decision tree model.
    decTreeModel = tree.DecisionTreeClassifier(criterion='entropy', max_depth=50)
    #fit the model using the numeric representations of the training data
    decTreeModel.fit(train_dfs, training_target)
    data_dot = tree.export_graphviz(decTreeModel,out_file='./tree.dot')
    #---------------------------------------------------------------
    #   Define 2 Queries, Make Predictions, Map Predictions to Levels
    #---------------------------------------------------------------
    
    q = {}
    for column in bank:
        if column != target:
            f = bank[column]
            tabf = f.value_counts()
            #keys = tabf.keys()
            firstvalue = bank[column].value_counts().keys()[0]
            secondvalue = bank[column].value_counts().keys()[1]
            q[column] = np.unique([firstvalue,secondvalue])
            #q[column] = np.unique(bank[column].value_counts())
            
    #q = {'age':[39,50],'workclass':['State-gov','Self-emp-not-inc'],'fnlwgt':[77516,83311],'education':['Bachelors','Bachelors'],'education-num':[13,13],'marital-status':['Never-married','Married-civ-spouse'],'occupation':['Adm-clerical','Exec-managerial'],'relationhip':['Not-in-family','Husband'],'race':['White','White'],'sex':['Male','Male'],'capital-gain':[2174,0],'capital-loss':[0,0],'hours-per-week':[40,13],'native_country':['United-States','United-States']}
    #col_names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationhip','race','sex','capital-gain','capital-loss','hours-per-week','native_country']
    #col_names = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome']
    col_names =list(bank.columns)
    col_names.remove(target)
    qdf = pd.DataFrame.from_dict(q,orient="columns")
    
    #extract the numeric features
    q_num = qdf[numeric_cfs].as_matrix() 
    #convert the categorical features
    q_cat = qdf.drop(numeric_cfs,axis=1)
    q_cat_dfs = q_cat.T.to_dict().values()
    q_vec_dfs = vectorizer.transform(q_cat_dfs) 
    #merge the numeric and categorical features
    query = np.hstack((q_num, q_vec_dfs))
    #Use the model to make predictions for the 2 queries
    predictions = decTreeModel.predict([query[0],query[1]])
    
    print("Predictions!")
    print("------------------------------")
    print(predictions)
    
    predictions = decTreeModel.predict(train_dfs)
    accuracy = accuracy_score(training_target, predictions, normalize=True)
    
    #--------------------------------------------
    # Hold-out Test Set + Confusion Matrix
    #--------------------------------------------
    print("-------------------------------------------------")
    print("Accuracy and Confusion Matrix on Hold-out Testset")
    print("-------------------------------------------------")
    
    #Split the data: 90% training : 10% test set
    instances_train, instances_test, target_train, target_test = model_selection.train_test_split(train_dfs, training_target, test_size=0.2, random_state=0)
    #
    #define a decision tree model using entropy based information gain
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    
    #fit the model using just the test set
    clf.fit(instances_train, target_train)
    #Use the model to make predictions for the test set queries
    predictions = clf.predict(instances_test)
    #Output the accuracy score of the model on the test set
    print("Accuracy = " + str(accuracy_score(target_test, predictions)))
    #Output the confusion matrix on the test set
    confusionMatrix = confusion_matrix(target_test, predictions)
    print("Confisious " , confusionMatrix)
    print("\n\n")
    
#    print("KNN")
#    #define a decision tree model using entropy based information gain
#    clf = KNeighborsClassifier(n_neighbors=50)
#    
#    #fit the model using just the test set
#    clf.fit(instances_train, target_train)
#    #Use the model to make predictions for the test set queries
#    predictions = clf.predict(instances_test)
#    #Output the accuracy score of the model on the test set
#    print("Accuracy = " + str(accuracy_score(target_test, predictions)))
#    #Output the confusion matrix on the test set
#    confusionMatrix = confusion_matrix(target_test, predictions)
#    print("Confisious " , confusionMatrix)
#    print("\n\n")
#    
    #
    #print("Support vector classification")
    ##define a decision tree model using entropy based information gain
    #clf = SVC()
    #
    ##fit the model using just the test set
    #clf.fit(instances_train, target_train)
    ##Use the model to make predictions for the test set queries
    #predictions = clf.predict(instances_test)
    ##Output the accuracy score of the model on the test set
    #print("Accuracy = " + str(accuracy_score(target_test, predictions)))
    ##Output the confusion matrix on the test set
    #confusionMatrix = confusion_matrix(target_test, predictions)
    #print("Confisious " , confusionMatrix)
    #print("\n\n")
    
    
    
    #Draw the confusion matrix
    import matplotlib.pyplot as plt
    
    # Show confusion matrix in a separate window
    plt.matshow(confusionMatrix)
    #plt.plot(confusionMatrix)
    plt.title('Confusion matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    
    #--------------------------------------------
    # Cross-validation to Compare to Models
    #--------------------------------------------
    print("------------------------")
    print("Cross-validation Results")
    print("------------------------")
    
    #run a 10 fold cross validation on this model using the full census data
    scores=cross_validation.cross_val_score(clf, instances_train, target_train, cv=10)
    #the cross validaton function returns an accuracy score for each fold
    print("Entropy based Model:")
    print("Score by fold: " + str(scores))
    #we can output the mean accuracy score and standard deviation as follows:
    print("Accuracy: %0.4f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    print("\n\n")
    
    #for a comparison we will do the same experiment using a decision tree that uses the Gini impurity metric
    decTreeModel3 = tree.DecisionTreeClassifier(criterion='gini')
    scores=cross_validation.cross_val_score(decTreeModel3, instances_train, target_train, cv=10)
    print("Gini based Model:")
    print("Score by fold: " + str(scores))
    print("Accuracy: %0.4f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    

    print("Finished");

main()
    
