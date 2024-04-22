import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

I,y = np.genfromtxt("data/data3.txt",unpack=True)

I=I-0.32
x=y-25
L=1000
phi=x/L
def sinc(X,A_0,b):
    #return A_0^2*b^2*(635/(np.pi*b*phi))^2*(np.sin((np.pi*b*phi)/635))^2

    return A_0^2*b^2*(635/(np.pi*b*np.sin(phi)))^2*(np.sin((np.pi*b*np.sin(phi))/635))^2

fig, (ax1) = plt.subplots(1, 1, layout="constrained")
ax1.plot(phi, I,".k" ,label="Doppelspalt")
#ax1.set_xlabel(r"$x \mathbin{/} \unit{\milli\meter}$")
#ax1.set_ylabel(r"$Stromstärke des Intensitätsmessgertes \mathbin{/} \unit{\nano\ampere}$")
ax1.legend(loc="best")

params, covariance_matrix=curve_fit(sinc, x,I,p0=[100000,0.1])
uncertainties=np.sqrt(np.diag(covariance_matrix))

x_plot=np.linspace(-27,27,100)

print(params, uncertainties)
ax1.plot(x_plot,sinc(x_plot,params[0],params[1]),"-")

fig.savefig("plot2.pdf")