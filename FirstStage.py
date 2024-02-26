import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.datasets import load_digits

class FirstStage:
    def __init__(self,anomaly_detector,threshold_b):
        self.anomaly_detector = anomaly_detector
        self.tb = threshold_b

    # PRECISA IMPLEMENTAR
    # probabilidade de ser uma anomalia
    def detect_anomaly_proba(self, X) -> np.array:
        """ deve retornar um vetor (apenas 1 dim) com as probabilidades de cada sample em X ser uma anomalia"""
        NotImplemented

    def set_threshold_b(self, threshold_b):
        self.tb = threshold_b

    def detectar_anomalia(self, X, return_probs= True):
        # prob_anomalia == lambda_b no esquema original
        prob_anomalia = self.detect_anomaly_proba(X)
        possibly_malign_indices = np.where(prob_anomalia > self.tb)[0]

        if return_probs:
            return possibly_malign_indices, prob_anomalia
        return possibly_malign_indices

if __name__ == '__main__':
    """Drive Test Code"""
    class PrimeiroEstagio(FirstStage):
        def __init__(self, anomaly_detector, threshold_b):
            super().__init__(anomaly_detector,threshold_b)  
        
        def detect_anomaly_proba(self, X) -> np.array:
            return self.anomaly_detector.predict_proba(X)[:,0]



    detector_anomalia = DecisionTreeClassifier(min_samples_split= 10)
    
    X,y = load_digits(return_X_y= True)

    # imagens 6,7,8,9 sao benignos
    X_benign = X[y > 5]
    y_benign = y[y > 5]

    # imagens 1,2,3,4,5 sao anomalias
    X_anomalia = X[(y <= 5) & (y != 0)]
    y_anomalia = y[(y <= 5) & (y != 0)]

    # imagem 0 e zero-day
    X_zero_day = X[y == 0]
    y_zero_day = y[y == 0]


    X_tree = np.row_stack((X_anomalia,X_benign))
    # 0 ---> anomalia
    # 1 ---> benign
    y_tree = np.concatenate(
        (np.zeros(len(X_anomalia)), np.ones(len(X_benign)))
    )

    detector_anomalia.fit(X_tree,y_tree)
    y_pred = detector_anomalia.predict(X_tree)
    
    print("modelo detector de anomalia")
    print(classification_report(y_pred, y_tree))
    print("---"*50)


    primeiro = PrimeiroEstagio(detector_anomalia, .5)
    indices, prob_anomalia = primeiro.detectar_anomalia(X_tree)
    print(prob_anomalia)
    y_pred = np.ones_like(y_tree)
    y_pred[indices] = 0

    print("Primeiro estagio")
    print(classification_report(y_pred, y_tree))
    print("---"*50)