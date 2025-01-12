import matplotlib.pyplot as plt
import numpy as np



I_s,B_s,s=np.genfromtxt("data/silber.txt",unpack=True)
I_k,B_k,k=np.genfromtxt("data/kupfer.txt",unpack=True)
I_z,B_z,z=np.genfromtxt("data/zink.txt",unpack=True)

D_s=0.5*(s[0]-0.158)
U_s=s-D_s

D_k=0.5*(k[0]-0.335)
U_k=k-D_k

D_z=0.5*(z[0]+0.004)
U_z=z-D_z


params, covariance_matrixs = np.polyfit(B_s, U_s, deg=1, cov=True)
paramk, covariance_matrixk = np.polyfit(B_k, U_k, deg=1, cov=True)
paramz, covariance_matrixz = np.polyfit(B_z, U_z, deg=1, cov=True)

uncertainties = np.sqrt(np.diag(covariance_matrixs))
uncertaintiek = np.sqrt(np.diag(covariance_matrixk))
uncertaintiez = np.sqrt(np.diag(covariance_matrixz))



fig, (s, k, z) = plt.subplots(1, 3, layout="constrained")
s.plot(B_s, U_s,"." ,label="Kurve")
s.set_xlabel(r"$B \mathbin{/} \unit{\milli\tesla}$")
s.set_ylabel(r"$U_H \mathbin{/} \unit{\milli\volt}$")
s.legend(loc="best")


s.plot(
    B_s,
    params[0] * B_s + params[1],
    label="Lineare Regression",
    linewidth=2,
)

k.plot(B_k, U_k,".", label="Kurve")
k.set_xlabel(r"$B \mathbin{/} \unit{\milli\tesla}$")
k.set_ylabel(r"$U_H \mathbin{/} \unit{\milli\volt}$")
k.legend(loc="best")

k.plot(
    B_k,
    paramk[0] * B_k + paramk[1],
    label="Lineare Regression",
    linewidth=2,
)

z.plot(B_z, U_z,".", label="Kurve")
z.set_xlabel(r"$B \mathbin{/} \unit{\milli\tesla}$")
z.set_ylabel(r"$U_H \mathbin{/} \unit{\milli\volt}$")
z.legend(loc="best")

z.plot(
    B_z,
    paramz[0] * B_z + paramz[1],
    label="Lineare Regression",
    linewidth=2,
)

print(D_s,D_k,D_z)
print(params[0],paramk[0],paramz[0])
print(uncertainties[0],uncertaintiek[0],uncertaintiez[0])

fig.savefig("build/plot.pdf")
