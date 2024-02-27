import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.datasets import load_digits
from FirstStage import FirstStage
from SecondStage import SecondStage
from Extension import Extension
from sklearn.model_selection import train_test_split

class Sistema_Hierarquico_Base(FirstStage, SecondStage, Extension):
    def __init__(self, anomaly_detector, classifier, n_anomalias, threshold_b, threshold_m, threshold_u):
        assert threshold_b <  threshold_u # not sure why

        FirstStage.__init__(self,anomaly_detector, threshold_b)
        SecondStage.__init__(self,classifier, n_anomalias, threshold_m)
        Extension.__init__(self,threshold_u)

        self.n_anomalias = n_anomalias
        self._benign_label = n_anomalias+1

    def get_labels(self):
        print("0 means zero-day, the system do not recognize as benign or any known malign")
        print(f"numbers 1 to {self.n_anomalias} are each one type of anomaly")
        print(f"{self._benign_label} means benign")

    def predict(self, X):
        # todos sao classificados como benign por default
        prediction = np.zeros(len(X),dtype= int) + self._benign_label

        # primeiro estagio: detector de anomalias
        possivelmente_anomalia_indices, prob_anomalia = self.detectar_anomalia(X)

        # segundo estagio: classificador de ataque
        # atk e um vetor com os labels (de 1 ate n_anomalias) e com alguns unkown (-1)
        atk = self.predict_attack(X[possivelmente_anomalia_indices])

        possibly_zero_day_indices = possivelmente_anomalia_indices[atk == self._unknown_label]

        # inferimos o zero day
        # nao precisamos definir os outros elementos como benignos, pois isso foi feito por default no inicio desta funcao
        is_not_zero_day = self.predict_benign_zero_day(prob_anomalia[possibly_zero_day_indices])

        # n_classes+1 representa zero-day,
        # [1,2,..., n_anomalias] representam anomalias
        # 0 representa zero-day
        prediction[possivelmente_anomalia_indices] = atk
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
            return probs[:,1]

        def classify_proba(self,X):
            # matriz, cada linha representa uma instancia que pde ser maligna,
            # cada coluna representa uma classe
            # cada elemento da matriz representa uma probabilidade
            return self.classifier.predict_proba(X)

if __name__ == '__main__':
    """Drive Test Code"""
    def criar_dados(X,y):

        # imagens 6,7,8,9 sao benignos
        X_benign = X[y > 5]
        y_benign = y[y > 5]

        # imagens 1,2,3,4,5 sao anomalias
        X_anomalia = X[(y <= 5) & (y != 0)]
        y_anomalia = y[(y <= 5) & (y != 0)]

        # imagem 0 e zero-day
        X_zero_day = X[y == 0]
        y_zero_day = y[y == 0]

        return X_benign, y_benign, X_anomalia, y_anomalia, X_zero_day, y_zero_day

    def treinar_modelos(X_anomalia,y_anomalia,X_benign):
            
        detector_anomalia = DecisionTreeClassifier(min_samples_split= 10)
        classificador = MLPClassifier((32,64,64,128,64,32))
        X_tree = np.row_stack((X_anomalia,X_benign))
        # 1 ---> anomalia
        # 0 ---> benign
        y_tree = np.concatenate(
            (np.ones(len(X_anomalia)), np.zeros(len(X_benign)))
        )

        detector_anomalia.fit(X_tree,y_tree)
            
        classificador.fit(X_anomalia, y_anomalia)
        return detector_anomalia, classificador

    X,y = load_digits(return_X_y= True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    X_benign, y_benign, X_anomalia, y_anomalia, X_zero_day, y_zero_day = criar_dados(X_train,y_train)
    detector_anomalia, classificador = treinar_modelos(X_anomalia,y_anomalia,X_benign) 

    n_anomalias = 5
    sistema = SistemaHierarquico(detector_anomalia, classificador, n_anomalias,.5,.9,.6)
    y_test = np.where(y_test > n_anomalias, sistema._benign_label, y_test)

    y_pred = sistema.predict(X_test)
    
    print("Primeiro estagio")
    print(classification_report(y_test,y_pred))
    print("---"*50)