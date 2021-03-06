import numpy as np

class ReLU():
    ''' Implements activation function rectified linear unit (ReLU)

    ReLU activation function is defined as the positive part of
    its argument. Todo: insert arxiv paper reference
    '''
    def __init__(self):
        self.params = []

    def forward(self, X):
        ''' In the forward pass return the identity for x < 0

        Safe input for backprop and forward all values that are above 0.
        '''
        self.X = X
        return np.maximum(X, 0)

    def backward(self, dout):
        ''' Derivative of ReLU

        Retruns:
            dX: for all x \elem X <= 0 in forward pass
                return 0 else x
            []: no gradients on ReLU operation
        '''
        dX = dout.copy()
        dX[self.X <= 0] = 0
        return dX, []

class LeakyReLU():
    ''' Description
    '''
    def __init__(self):
        self.params = []

    def forward(self, X):
        self.X = X
        self.alpha = 0.0001
        return np.maximum(X, X * a)

    def backward(self, dout):
        return None


class sigmoid():
    ''' Description
    '''
    def __init__(self):
        self.params = []

    def forward(self, X):
        return 1 / (1 + math.exp(-X))

    def backward(self, dout):
        return self.forward(dout) * (1 - self.forward(dout))

class tanh():
    ''' Description
    '''
    def __init__(self):
        self.params = []

    def forward(self, X):
        return np.tanh(X)

    def backward(self, dout):
        return 1 - (self.forward(dout) * self.forward(dout))

