import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm.notebook import tqdm
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import pickle
try:
    from best_threshold import binary_distribution_threshold_max_acc, binary_distribution_threshold_recall_search
except ImportError:
    from .best_threshold import binary_distribution_threshold_max_acc, binary_distribution_threshold_recall_search
    
    # Implementação do Early Stopping
class EarlyStopping:
    def __init__(self, patience=7, delta=0, verbose=True, path='checkpoint.pt'):
        self.patience = patience
        self.delta = delta
        self.verbose = verbose
        self.counter = 0
        self.early_stop = False
        self.val_min_loss = np.Inf
        self.path = path

    def __call__(self, val_loss, model):
        if val_loss < self.val_min_loss - self.delta:   # Caso a loss da validação reduza, vamos salvar o modelo e nova loss mínima
            self.save_checkpoint(val_loss, model)
            self.counter = 0
        else:                                           # Caso a loss da validação NÃO reduza, vamos incrementar o contador da paciencia
            self.counter += 1
            print(f'EarlyStopping counter: {self.counter} out of {self.patience}. Current validation loss: {val_loss:.5f}')
            if self.counter >= self.patience:
                self.early_stop = True

    def save_checkpoint(self, val_loss, model):
        if self.verbose:
            print(f'Validation loss decreased ({self.val_min_loss:.5f} --> {val_loss:.5f}).  Saving model ...')
        torch.save(model, self.path)
        self.val_min_loss = val_loss

# Implementação do Autoencoder
class Autoencoder(nn.Module):
    def __init__(self, in_features, dropout_rate=0.1, scaler= None):
        super().__init__()

        self.in_features = in_features
        self.dropout_rate = dropout_rate
        self.early_stopping = None
        self.in_features = in_features
        self.dropout_rate = dropout_rate
        self.early_stopping = None
        self.scaler = scaler

        self.encoder = nn.Sequential(
        # Camada 1 de encoding:
            nn.Linear(in_features, 64),
            nn.ReLU(),
            # Camada 2 de encoding:
            nn.Linear(64, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Dropout(dropout_rate),

            # Camada 3 de encoding:
            nn.Linear(32,16),
            nn.BatchNorm1d(16),
            nn.ReLU(),
            nn.Dropout(dropout_rate),

            # Camada 4 de encoding:
            nn.Linear(16,8),
            nn.BatchNorm1d(8),
            nn.ReLU(),
            )

        self.decoder = nn.Sequential(
        # Camada 1 de decoding:
        nn.Linear(8, 16),
        nn.ReLU(),
        # Camada 2 de decoding:
        nn.Linear(16, 32),
        nn.BatchNorm1d(32),
        nn.ReLU(),
        nn.Dropout(dropout_rate),
        
        # Camada 3 de decoding
        nn.Linear(32,64),
        nn.ReLU(),
        

        nn.Linear(64, in_features),
        nn.Sigmoid()
        )


    def forward(self, X):
        """pass only scaled data"""
        encoded = self.encoder(X)
        decoded = self.decoder(encoded)
        return decoded

    def compile(self, learning_rate):
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.parameters(), lr = learning_rate)

    def fit(self, X_train, num_epochs, batch_size, X_val = None, patience = None, delta = None):
        if X_val is not None and patience is not None and delta is not None:
            print(f'Using early stopping with patience={patience} and delta={delta}')
            self.early_stopping = EarlyStopping(patience, delta)

        val_avg_losses = []
        train_avg_losses = []

        for epoch in range(num_epochs):
            # Calibrando os pesos do modelo
            train_losses = []
            self.train()
            for batch in tqdm(range(0, len(X_train), batch_size)):
                batch_X = X_train[batch:(batch+batch_size)]
                batch_reconstruction = self.forward(batch_X)

                train_loss = self.criterion(batch_reconstruction, batch_X)
                self.optimizer.zero_grad()
                train_loss.backward()
                self.optimizer.step()
                train_losses.append(train_loss.item())
            train_avg_loss = np.mean(train_losses)
            train_avg_losses.append(train_avg_loss)
            print(f'Epoch#{epoch+1}: Train Average Loss = {train_avg_loss:.5f}')

            # Mecanismo de early stopping
            if self.early_stopping is not None:
                val_losses = []
                self.eval()
                with torch.no_grad():
                    for batch in range(0, len(X_val), batch_size):
                        batch_X = X_val[batch:(batch+batch_size)]
                        batch_reconstruction = self.forward(batch_X)
                        val_loss = self.criterion(batch_reconstruction, batch_X)
                        val_losses.append(val_loss.item())
                val_avg_loss = np.mean(val_losses)
                val_avg_losses.append(val_avg_loss)
                self.early_stopping(val_avg_loss, self)
                if self.early_stopping.early_stop:
                    print(f'Stopped by early stopping at epoch {epoch+1}')
                    break

        if self.early_stopping is not None:
            self = torch.load('checkpoint.pt')
        self.eval()
        return train_avg_losses, val_avg_losses


    def score_samples(self, X, scale_data= False):
        """Quanto maior o valor retornado, mais anomalo"""
        if scale_data:
            X = self.scaler.transform(X)

        X = torch.FloatTensor(X)
        with torch.no_grad():
            reconstructed_X = self.forward(X)
            anomaly_scores = torch.mean(torch.pow(X - reconstructed_X, 2), axis=1).detach().numpy() # MSELoss
        return anomaly_scores

    def predict(self, X, threshold= .5, scale_data= False):
        anomaly_scores = self.score_samples(X, scale_data)
        y_pred = np.where(anomaly_scores > threshold, ANOMALY_LABEL, BENIGN_LABEL)
        return y_pred


if __name__ == '__main__':
    BENIGN_LABEL = 0
    ANOMALY_LABEL = 1

    train_stage_1_3_OCSVM = pd.read_csv("data\\train_stage_1_3_AE.csv")
    X_train = train_stage_1_3_OCSVM.drop(columns=["Label", "Unnamed: 0"])
    y_train = np.ones(len(train_stage_1_3_OCSVM["Label"])) * BENIGN_LABEL
    del train_stage_1_3_OCSVM   

    validation_stage_1_3 = pd.read_csv("data/validation_stage_1_3.csv")
    X_val = validation_stage_1_3.drop(columns=["Label", "Unnamed: 0"])
    y_val = np.where(validation_stage_1_3["Label"] == "BENIGN", BENIGN_LABEL, ANOMALY_LABEL)
    del validation_stage_1_3

    qtd_anomalia = np.sum(y_val == ANOMALY_LABEL)
    qtd_benigno  = len(y_val) - qtd_anomalia
    pctg_anomalia = qtd_anomalia/(qtd_anomalia + qtd_benigno)
    X_val, X_test, y_val, y_test = train_test_split(X_val, y_val)


    minmax_scaler = MinMaxScaler()
    minmax_scaler = minmax_scaler.fit(X_train)

    X_train = minmax_scaler.transform(X_train)
    X_val = minmax_scaler.transform(X_val)
    X_test = minmax_scaler.transform(X_test)

    with open("Models\melhorado\scaler_ae.p","wb") as f:
        pickle.dump(minmax_scaler,f)

    X_train = torch.FloatTensor(X_train)
    X_val = torch.FloatTensor(X_val)
    X_test = torch.FloatTensor(X_test)

    ae = Autoencoder(X_train.shape[1],scaler= minmax_scaler)
    
    BATCH_SIZE = 2048
    LR = 1e-4
    PATIENCE = 10
    DELTA = 0.001
    NUM_EPOCHS = 200
    IN_FEATURES = X_train.shape[1]
        
    ae.compile(learning_rate = LR)
    ae.fit(
            X_train,
            NUM_EPOCHS,
            BATCH_SIZE,
            X_val = X_val[y_val == BENIGN_LABEL],
            patience=PATIENCE,
            delta=DELTA
            )

    y_score = ae.score_samples(X_val)


    y_score_benigno  = pd.Series(np.random.choice(y_score[y_val == BENIGN_LABEL], qtd_anomalia))
    y_score_anomalia = pd.Series(y_score[y_val == ANOMALY_LABEL])

    norm01 = lambda v: (v-v.min()) / (v.max()-v.min())

    t = binary_distribution_threshold_recall_search(y_val, y_score, .95)
    print(t)
    y_score_anomalia.hist(label= "anomalia")
    y_score_benigno.hist(label= "benigno")

    plt.axvline(x = t, color = 'g', label = f'threshold:{np.round(t*1e3,2)}e3')
    plt.legend()
    plt.show()

    print(y_score_benigno.min(),y_score_benigno.max())
    print(y_score_anomalia.min(),y_score_anomalia.max())


    for X_i, y_i in [(X_train,y_train), (X_val, y_val), (X_test, y_test)]:
        y_pred = ae.predict(X_i, threshold= t)
        print(classification_report(y_i,y_pred))
