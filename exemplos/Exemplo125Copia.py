from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
# A->B (1)
# 2A->C (2)

def Multiplas(CI,V):
    T=CI[0]
    FA=CI[1]
    FB=CI[2]
    FC=CI[3]

    k1A = 10 * np.exp(4000 * (1 / 300 - 1 / T))  # 1/s
    k2A = 0.09 * np.exp(9000 * (1 / 300 - 1 / T))  # L/mol s
    FT = FA + FB + FC
    CA = CT0 * (FA / FT) * (T0 / T)
    r1A = -k1A * CA
    r2A = -k2A * CA**2
    dTdV = ((-r1A)*(-deltH1A) + (-r2A)*(-deltH2A) - Ua*(T-Ta)) / (FA*cpA + FB*cpB + FC*cpC)
    dFAdV = r1A+r2A
    dFBdV = -r1A
    dFCdV = -r2A/2
    return np.array([dTdV,dFAdV,dFBdV,dFCdV])

#PARÂMETROS
deltH1A=-20000 #J/molA1
deltH2A=-60000 #J/molA2
cpA= 90 #J/mol°C
cpB= 90 #J/mol°C
cpC= 180 #J/mol°C
Ua=4000 #J/m³s°C
Ta=373 #K

#VALORES INICIAIS
FA0=100 #mol/s
FB0=0
FC0=0
T0 = 423  # K
CT0 = 0.1  # mol/L

#EDO
CI= np.array([T0,FA0,FB0,FC0])
V = np.arange(0, 1, 0.001)  # faixa de variação do volume
x = odeint(Multiplas, CI, V)

print("T=",x[-1,0])
print("FA=",x[-1,1])
print("FB=",x[-1,2])
print("FC=",x[-1,3])

#GRÁFICOS
plt.subplots_adjust(left=0.25,hspace=0.4) #configura as distâncias entre gráficos no subplot
plt.subplot(211)
plt.plot(V, x[:, 1], 'k',label="FA")
plt.plot(V, x[:, 2], 'k:',label="FB")
plt.plot(V, x[:, 3], 'k--',label="FC")
plt.legend()
plt.xlabel('Volume (m³)') # \u00b3 -> unicode para ³, Ctrl+Alt+3
plt.ylabel('Fi (mol/s)',rotation=0,labelpad=35) #Eixo y escrito na horizontal(rotation) e a uma certa distancia do eixo (labelpad)
plt.grid()
plt.yticks(np.arange(0,101,20))
plt.subplot(212)
plt.plot(V, x[:, 0], 'r', label="T(t)")
plt.xlabel('Volume (m\u00b3)') # \u00b3 -> unicode para ³
plt.ylabel('T(K)',rotation=0,labelpad=20)
plt.grid()
plt.show()