import numpy as np
from utils import numpy_softmax, numpy_relu


def unit_propagation():
    pass

def backtracking():
    pass




class Transformer:
    def __init__(self,num_rows_X, num_cols_X, num_rows_Q, num_rows_W, max_vars):
        self.Q = np.zeros((num_rows_Q,num_rows_X))  # query
        self.K = np.zeros((num_rows_Q,num_rows_X))  # key
        self.V = np.zeros((num_rows_Q,num_cols_X))  # value

        self.W1 = np.zeros((num_rows_W,num_rows_X)) # FF1 weight
        self.b1 = np.zeros((num_rows_W,num_cols_X)) # FF1 bias
        self.W2 = np.zeros((num_rows_X,num_rows_W)) # FF2 weight
        self.b2 = np.zeros((num_rows_X,num_cols_X)) # FF2 bias

        self.max_vars = max_vars

    def forward(self, X, heatmap_title=None): # return the output of TF Encoder layer (in eq.1b)
        # X: input matrix with size (num_rows_X, num_cols_X)
        np.set_printoptions(precision=1, suppress=True)
        self.softmax_output = numpy_softmax(X.T @ self.K.T @ self.Q @ X, lam=self.lam, dim=1) 
        self.attn = X + self.V @ X @ self.softmax_output
        ff1_output = numpy_relu(self.W1 @ self.attn + self.b1)
        output = self.attn + self.W2 @ ff1_output + self.b2

        return output