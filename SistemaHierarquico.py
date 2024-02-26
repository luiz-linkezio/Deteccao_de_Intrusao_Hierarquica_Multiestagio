import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.datasets import load_digits
from FirstStage import FirstStage
from SecondStage import SecondStage
from Extension import Extension

class Sistema_Hierarquico_Base(FirstStage, SecondStage, Extension):
    def __init__(self, anomaly_detector, classifier, n_anomalias, threshold_b, threshold_m, threshold_u):
        assert threshold_b <  threshold_u # not sure why

        FirstStage().__init__(anomaly_detector, threshold_b, benign_label= n_anomalias + 1)
        SecondStage().__init__(classifier, n_anomalias, threshold_m)
        Extension().__init__(threshold_u)

        self.n_anomalias = n_anomalias


    def get_labels(self):
        print("0 means zero-day, the system do not recognize as benign or any known malign")
        print(f"numbers 1 to {self.n_anomalias} are each one type of anomaly")
        print(f"{self._benign_label} means benign")

    def predict(self, X):
        # todos sao classificados como benign por default
        prediction = np.zeros(len(X),dtype= int) + self._benign_label

        # primeiro estagio: detector de anomalias
        possibly_malign_indices, prob_anomalia = self.detectar_anomalia(X)

        # segundo estagio: classificador de ataque
        # atk e um vetor com os labels (de 1 ate n_anomalias) e com alguns unkown (-1)
        atk = self.predict_atack(X[possibly_malign_indices])

        possibly_zero_day_indices = possibly_malign_indices[atk == self._unknown_label]

        # inferimos o zero day
        # nao precisamos definir os outros elementos como benignos, pois isso foi feito por default no inicio desta funcao
        is_not_zero_day = self.predict_benign_zero_day(prob_anomalia[possibly_zero_day_indices])
        zero_day_indices = possibly_zero_day_indices[is_not_zero_day == False]

        # n_classes+1 representa zero-day,
        # [1,2,..., n_anomalias] representam anomalias
        # 0 representa zero-day
        prediction[possibly_malign_indices] = atk
        prediction[possibly_zero_day_indices] = np.where(is_not_zero_day, self._benign_label, self._zero_day_label)

        return prediction

if __name__ == '__main__':
    class SistemaHierarquico(Sistema_Hierarquico_Base):
        def __init__(self,anomaly_detector, classifier, n_classes, threshold_b, threshold_m, threshold_u):
            super().__init__(anomaly_detector, classifier, n_classes, threshold_b, threshold_m, threshold_u)

        def detect_anomaly_proba(self, X):
            # vetor com classe de maior probabilidade de cada instancia
            # pegam so a probabilidade dos elementos serem 1
            probs = self.anomaly_detector.predict_proba(X)
            return probs[:,0]

        def classify_proba(self,X):
            # matriz, cada linha representa uma instancia que pde ser maligna,
            # cada coluna representa uma classe
            # cada elemento da matriz representa uma probabilidade
            return self.classifier.predict_proba(X)
