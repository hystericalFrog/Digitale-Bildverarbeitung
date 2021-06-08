import numpy as np

M = np.arange(100).reshape(10,10)
print("M")
print(M)

v = np.ones(10) * 20
print("v")
print(v)

vr = v - M[1][:]
print("vr = v - M[1][:]")
print(vr)


mr = M.dot(vr.transpose())
print("mr = M * vr^(-1)")
print(mr)

mr100 = np.round(mr / 100)
print("mr / 100 gerundet")
print(mr100)
print("Maximum")
print(max(mr100))

