import numpy as np
X1 = np.array([1, -2, 0, -1])
X2 = np.array([0, 1.5, -0.5, -1])
X3 = np.array([-1, 1, 0.5, -1])
X = [X1, X2, X3]
W = np.array([1, -1, 0, 0.5])
 
d=[1,-1,-1]
c=0.1
epochs=1
op=0
for i in range(epochs):
    for j in range(3):
        net=np.dot(W,X[j])
        if net==0:
            op=0
        if net>0:
            op=1
        if net<0:
            op=-1
        error=d[j]-op
        dw=c*error*X[j]
        W+=dw
        print("W", j,  W)
print(f'Final weight after epoch is {W}')