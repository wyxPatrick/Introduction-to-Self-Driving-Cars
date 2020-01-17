import numpy as np
from math import atan

x0 = np.array([[0],[5]])
P0 = np.array([[0.01,0],[0,1]])
delta_t = 0.5
u0 = -2
w0 = 0
y1 = np.pi/6
S = 20
D = 40

F0 = np.array([[1,delta_t],[0,1]])
L0 = np.eye(2)
Q0 = 0.1 * np.eye(2)

# Prediction
x1_p = np.dot(np.array([[1,delta_t],[0,1]]),x0) + np.array([[0],[delta_t]])*u0 + w0
P1_p = np.dot(np.dot(F0,P0),F0.T) + np.dot(np.dot(L0,Q0),L0.T)

# Optimal Gain
H1 = np.array([S/((D-x1_p[0])**2 + S**2), 0])
M1 = 1
R1 = 0.01
K1 = np.matrix(np.dot(P1_p,H1.T) * (1/(np.dot(np.dot(H1,P1_p),H1.T) + M1*R1*M1))).T

#Correction
v1 = 0
x1 = x1_p + np.dot(K1, (y1 - atan(S/(D-x1_p[0])) + v1))
print(x1)
