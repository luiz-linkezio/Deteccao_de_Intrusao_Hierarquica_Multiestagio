import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.datasets import load_digits
import time
class SecondStage:
    def __init__(self,classifier,n_anomalias,threshold_m):
        self.classifier = classifier
        self.tm = threshold_m
        self.n_anomalias = n_anomalias
        self._unknown_label = -1
        self.execution_time_list2 = []


    def set_threshold_m(self, threshold_m):
        self.tm = threshold_m

    # PRECISA IMPLEMENTAR
    def classify_proba(self,X) -> np.array:
        NotImplemented

    # CLASSIFICADOR
    def get_class_and_proba(self,X):
        probs = self.classify_proba(X)
        classes = np.argmax(probs,1) + 1 # as classes do classificador sao de 1 para cima
        probs   =  np.max(probs,1)
        # an array shape (len(X),2), each row is a sample
        # the first column is the class and the second one is the probability to be a member of that class
        return classes,probs


    def get_execution_time_list2(self):
        return self._execution_time_list2

    def predict_attack(self, X,  return_probs= False):

        start = time.perf_counter()
        atk, Patk = self.get_class_and_proba(X)
        # se nenhum ataque tiver a minima probabilidade:
        # classifique como desconhecido
        atk = np.where(Patk > self.tm, atk, self._unknown_label)
        finish = time.perf_counter()

        self.execution_time_list2.append(finish-start)

        if return_probs:
            return atk, Patk
        return atk

if __name__ == '__main__':
    class SegundoEstagio(SecondStage):
        def __init__(self, classifier, n_anomalias, threshold_m):
            super().__init__(classifier, n_anomalias, threshold_m)

        def classify_proba(self,X):
            # matriz, cada linha representa uma instancia que pde ser maligna,
            # cada coluna representa uma classe
            # cada elemento da matriz representa uma probabilidade
            return self.classifier.predict_proba(X)

    classificador = MLPClassifier((10,10,10))

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

    classificador.fit(X_anomalia, y_anomalia)
    y_pred = classificador.predict(X_anomalia)

    print("modelo de classificacao")
    print(classification_report(y_anomalia, y_pred))
    print("---"*50)

    segundo = SegundoEstagio(classificador, 5, .9)
    
    print("segundo estagio sem zero-day")
    segundo.predict_attack(X_anomalia)
    print(classification_report(y_anomalia, y_pred))
    print("---"*50)

    print("segundo estagio com zero-day")
    unknown_label = segundo._unknown_label
    y_ = np.concatenate((y_anomalia, np.zeros_like(y_zero_day)+unknown_label))
    X_ = np.row_stack((X_anomalia, X_zero_day))
    y_pred = segundo.predict_attack(X_)

    print(classification_report(y_, y_pred))
    print("---"*50)