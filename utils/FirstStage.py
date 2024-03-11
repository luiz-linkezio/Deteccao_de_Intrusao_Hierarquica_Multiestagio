import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.datasets import load_digits
from utils.best_threshold import binary_distribution_threshold_search
import time
class FirstStage:
    def __init__(self,anomaly_detector,threshold_b= None, ys= None):
        """anomaly detector must be a pretrained binary classifier
        threshold_b must be between 0 and 1
        ys must be a tuple of 2 np.arrays containing the correct labels and probabilities of being classified as 1"""
        self.anomaly_detector = anomaly_detector
        
        if threshold_b is not None:
            self.tb = threshold_b
        elif ys is not None:
            self.tb = binary_distribution_threshold_search(ys[0],ys[1])
        else:
            ValueError("ys and threshold_b cannot be both None")

        self._execution_time_list1 = []

    # PRECISA IMPLEMENTAR
    # probabilidade de ser uma anomalia
    def detect_anomaly_proba(self, X) -> np.array:
        """ deve retornar um vetor (apenas 1 dim) com as probabilidades de cada sample em X ser uma anomalia"""
        NotImplemented

    def set_threshold_b(self, threshold_b):
        self.tb = threshold_b

    def search_threshold(self, y_true: np.array, y_pred_proba= None, X= None, set_threshold: bool= True):
        assert (y_pred is not None) or (X is not None)
        if X is not None:
            y_pred_proba = self.detect_anomaly_proba(X)
        t = binary_distribution_threshold_search(y_true, y_pred_proba)
        if set_threshold:
            self.tb = t
        return t

    def get_execution_time_list1(self):
        return self._execution_time_list1


    def detectar_anomalia(self, X, return_probs= True):
        start = time.perf_counter()
        
        # prob_anomalia == lambda_b no esquema original
        prob_anomalia = self.detect_anomaly_proba(X)
        possivelmente_anomalia_indices = np.where(prob_anomalia >= self.tb)[0]
        finish = time.perf_counter()
        self.execution_time_list1.append(finish - start)

        if return_probs:
            return possivelmente_anomalia_indices, prob_anomalia
        return possivelmente_anomalia_indices

if __name__ == '__main__':
    """Drive Test Code"""
    class PrimeiroEstagio(FirstStage):
        def __init__(self, anomaly_detector, threshold_b):
            super().__init__(anomaly_detector,threshold_b)  
        
        def detect_anomaly_proba(self, X) -> np.array:
            return self.anomaly_detector.predict_proba(X)[:,1]



    #detector_anomalia = DecisionTreeClassifier(max_depth=4)
    detector_anomalia = LogisticRegression()

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
    # 1 ---> anomalia
    # 0 ---> benign
    y_tree = np.concatenate(
        (np.ones(len(X_anomalia)), np.zeros(len(X_benign)))
    )

    detector_anomalia.fit(X_tree,y_tree)
    y_pred = detector_anomalia.predict(X_tree)
    
    print("modelo detector de anomalia")
    print(classification_report(y_tree, y_pred))
    print("---"*50)


    primeiro = PrimeiroEstagio(detector_anomalia, .5)
    
    indices, prob_anomalia = primeiro.detectar_anomalia(X_tree)
    y_pred = np.zeros_like(y_tree)
    y_pred[indices] = 1

    print("Primeiro estagio")
    print(classification_report(y_tree, y_pred))
    print("---"*50)

    primeiro.search_threshold(y_tree, detector_anomalia.predict(X_tree))
    indices, prob_anomalia = primeiro.detectar_anomalia(X_tree)
    y_pred = np.zeros_like(y_tree)
    y_pred[indices] = 1
    
    print("Primeiro estagio post threshold search")
    print(classification_report(y_tree, y_pred))
    print("---"*50)