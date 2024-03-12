import numpy as np
from sklearn.metrics import classification_report

def test_sistema(sistema, test_dataset_list, test_dataset_names= None, nome_labels= None):

    if test_dataset_names is None:
        test_dataset_names =  np.arange()
    for set_name,test_dataset in zip(test_dataset_names, test_dataset_list):
        y_test = test_dataset.Label.to_numpy()
        X_test = test_dataset.drop(columns= ["Label", "Unnamed: 0"]).to_numpy()

        y_pred = sistema.predict(X_test)
        
        if nome_labels is not None:
            # basta usar o sescond.classes_ para anomalias, 
            y_pred = np.array([nome_labels[pred] for pred in y_pred])

        print(set_name)
        print(classification_report(y_test,y_pred))
        print("-"*100,"\n\n")