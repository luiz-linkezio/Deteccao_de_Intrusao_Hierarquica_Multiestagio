import numpy as np

def binary_distribution_threshold_max_acc(y_true, y_pred_proba):
    """y_true and y_pred_proba are arrays of the same size.
    y_true must be binary, 1 or 0, and y_pred_proba must be the probabilities of each element being 1"""

    y_prob_true = list(zip(y_pred_proba,y_true))
    y_prob_true.sort()

    # comecamos considerando threshold t = 0, 
    # ou seja, a classe atribuida a todos sera 1
    # portanto a acuracia sera o numero de elementos da classe 1
    t = -1e-5
    best_acc = acc = float((y_true == 1).mean())

    # o incremento (ou decremento) de um dado de um classe acima ou abaixo do threshold
    # portanto, se considerarmos o threshold t (em um determinado valor), e um dado x
    # x ou sera classificado corretamente, o que aumenta a acuracia no valor de one_p,
    # ou x sera classificado incorretamente, o que diinui a acuracia no valor de one_p
    one_p = 1/len(y_true)

    # cada iteracao do loop considera qual seria a acuracia (acc)
    # se o threshold fosse imediatamente acima do valor prob
    # ou seja, caso o threshold fizesse do dado atual o ultimo elemento da classe 0, 
    # qual seria a acuracia?
    for prob, classe in y_prob_true:

        if classe == 1:
            acc -= one_p # como o threshold esta acima do dado, ele sera categorizado incorretamente como 0

        else:           
            acc += one_p # como o threshold esta acima do dado, ele sera categorizado corretamente como 0

        if best_acc < acc:
            best_acc = acc
            t        = prob


    return t


def binary_distribution_threshold_recall_search(y_true, y_pred_proba, recall= .98):

    """y_true and y_pred_proba are arrays of the same size.
    y_true must be binary, 1 or 0, and y_pred_proba must be the probabilities of each element being 1
    weights is a tuple with the impact of the samples 0 and 1 on the acc"""

    y_prob_true = list(zip(y_pred_proba,y_true))
    y_prob_true.sort()

    t = -1e-5
    tp = np.sum(y_true == 1)
    fn = 0

    # cada iteracao do loop considera qual seria o recall (rec)
    # se o threshold fosse imediatamente acima do valor prob
    # ou seja, caso o threshold fizesse do dado atual o ultimo elemento da classe 0, 
    # qual seria a acuracia?
    for prob, classe in y_prob_true:

        if classe == 1:
            fn+=1
            tp-=1
            if tp/(fn+tp) < recall:
                return t
            else:
                t = prob




if __name__ == '__main__':
    y =   np.array([ 0, 1, 0, 0 , 0] + [ 1, 1, 1, 1, 0])
    y_p = np.array([.0,.1,.2,.3 ,.4] + [.5,.6,.7,.8,.9])
    print(binary_distribution_threshold_max_acc(y,y_p))