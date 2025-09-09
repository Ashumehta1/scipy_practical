import numpy as np
import matplotlib.pyplot as plt
x=np.arange(11)
y=np.array([2,1.9,1.7, 1.5,0.5,0,0.8,2,1.4,0.1,1.7])
plt.plot(x,y,"o:",label="normal")#markwith doted line
plt.legend()
#plt.plot(x,y,"o")# only marked nor dotted line
plt.show()

print('''scipy.interpolate
      from scipy.interpolate import interp1d''')
from scipy.interpolate import interp1d
predict_quad=interp1d(x,y,kind="quadratic")
predict_linear=interp1d(x,y,kind="linear")
predict_nearest=interp1d(x,y,kind="nearest")
predict_zero=interp1d(x,y,kind="zero")
predict_slinear=interp1d(x,y,kind="slinear")
predict_cubic=interp1d(x,y,kind="cubic")

x2=np.linspace(0,10,100)
y_q=np.array([predict_quad(x) for x in x2])
y_l=np.array([predict_linear(x) for x in x2])
y_n=np.array([predict_nearest(x) for x in x2])
y_z=np.array([predict_zero(x) for x in x2])
y_sl=np.array([predict_slinear(x) for x in x2])
y_c=np.array([predict_cubic(x) for x in x2])

y2=[y_q,y_l,y_n,y_z,y_sl,y_c]
names = ['quadratic','linear','nearest','zero','slinear','cubic']
plt.plot(x,y,"o:",label="data")
for i,names in zip(y2,names):
    plt.plot(x2,i,"ro:",label=names)
    plt.legend()
    plt.show()

