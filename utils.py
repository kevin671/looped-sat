import torch.nn as nn
import torch
import numpy as np


def numpy_softmax(arr, lam=1, dim=1):
    if dim == 0:
        raise NotImplementedError

    exp_arr = np.exp(lam*arr)
    num_rows = exp_arr.shape[0]
    sum_exp_arr = (np.sum(exp_arr, axis=0, keepdims=True) * np.ones((num_rows,1)))
    
    return exp_arr/sum_exp_arr
    #return nn.Softmax(dim=dim)(torch.from_numpy(arr)).numpy()

def numpy_relu(arr):
    return nn.ReLU()(torch.from_numpy(arr)).numpy()