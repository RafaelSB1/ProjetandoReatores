from django.test import TestCase
import numpy as np
from scipy.integrate import odeint

def StrToFloat(CI):
    for x in CI:
        if x == "":
            x=0    
    vetorresposta = []
    for i in CI:
        i=float(i)
        vetorresposta.append(i)
    global T0
    T0=vetorresposta[0]
    return vetorresposta

######## EXEMPLO 10.2 #########
def e102(request):
    def PBR(CI,W):
        X=CI[0]
        p=(1-alfa*W)**0.5
        PT=PT0*(1-X)/(1+E*X)*p # E: épsilon
        PH2=PT0*(omegaH2-X)*p
        PB=PT0*X*p+PB0
        rT = -(k*PH2*PT/(1+KB*PB+KT*PT))*a
        dXdW = -rT/FT0 # FT0 - taxa molar de toluneo na alimentação
        return [dXdW]

    def Desativacao(a,t):
        dadt=-0.325*a**2
        return dadt

    #PARÂMETROS
    FT0= 50 #mol/min - taxa molar de alimentação de tolueno
    T=640 #°C  COMO k É FIXO, A TEMPERATURA NÃO ESTÁ AFETANDO NO PROCESSO
    P0=40 #atm
    yT=0.3
    yH2=0.45
    PT0=float(request.POST.get("PT0"))
    PH20=float(request.POST.get("PH20"))
    PB0=float(request.POST.get("PB0"))   
    omegaH2=PH20/PT0
    alfa=0.000098 #1/kg cat
    k=0.00087 #mol/atm²/kg cat/min
    KB=1.39 #1/atm
    KT=1.038 #1/atm
    E=0 #épsilon

    #DESATIVAÇÃO
    tf= float(request.POST.get("tf")) #dias
    t = np.arange(0, tf+1, 1)
    vetor_a=odeint(Desativacao, 1, t)
    a=float(vetor_a[-1])

    #EDO
    X0=0
    CI= np.array([X0])
    Wf=10000 #kg cat
    W = np.arange(0, Wf+100, 100)  # faixa de variação do catalisador
    x = odeint(PBR, CI, W)

    i=0
    vetor_p=[]
    vetor_PT=[]
    vetor_PH2=[]
    vetor_PB=[]
    a=[]
    for y in vetor_a[:,0]:
        a.append(y)
    for y in x[:,0]:
        X=y
        p=(1-alfa*W[i])**0.5
        PT=PT0*(1-X)/(1+E*X)*p # E: épsilon
        PH2=PT0*(omegaH2-X)*p
        PB=PT0*X*p+PB0

        vetor_p.append(float(p))
        vetor_PT.append(float(PT))
        vetor_PH2.append(float(PH2))
        vetor_PB.append(float(PB))
        i+=1
    return  {'W':W, 'x':x, 'p':vetor_p, 'PT':vetor_PT, 'PH2':vetor_PH2, 'PB':vetor_PB, 'a':a, 't':t}
######## EXEMPLO 10.2 #########/

######## EXEMPLO 12.2 #########
def e122(request):
    def PFR(x,V):
        X=x[0] #Conversão
        T=x[1] #Temperatura
        Ta=x[2] #Ta
        CpA=alfaA+betaA*T+gamaA*T**2 # J/(mol K)
        CpB=alfaB+betaB*T+gamaB*T**2
        CpC=alfaC+betaC*T+gamaC*T**2
        CpD=alfaD+betaD*T+gamaD*T**2
        CpI=R*(alfaI+betaI*T+deltaI*T**(-2)) #Dados do Smith van ness -> Cp/R
        Cpa=R*(alfaa+betaa*T+deltaa*T**(-2))
        H = (a * HA + b * HB + c * HC + d * HD) + delta_alfa*(T - 298) + delta_beta*(T**2 - 298**2)/2 + delta_gama*(T**3 - 298**3)/3  # J/mol
        k = A * np.exp(-Ea / R / T)
        #K = Aeq * np.exp(-H / R / T)
        rA = -k*CA0*(1-X)/(1+E*X)*T0/T*P/P0
        dXdV = -rA / FA0  # dX / dV
        dTdV  = (Ua * (Ta - T) + rA * H) / ((FA0*CpA + FB0*CpB + FC0*CpC + FD0*CpD + FI0*CpI) + FA0*X*(CpC+CpD-CpA-CpB))  # dT / dV
        dTadV = Ua*(T-Ta)/(m*Cpa)*fator # dTa/dV
        return np.array([dXdV,dTdV,dTadV])

    # CONSTANTES / PARÂMETROS
    FA0 = float(request.POST.get("FA0"))  # mol/s por tudo
    FB0 = float(request.POST.get("FB0")) 
    FC0 = float(request.POST.get("FC0")) 
    FD0 = float(request.POST.get("FD0")) 
    FI0 = float(request.POST.get("FI0")) 
    R = 8.31442 # J/(mol*K)
    Ea = 284536.0812 # J/mol
    A = 8.197 * 10**14 # s-¹
    P0 = 162000 #Pa
    P = 162000 #Pa
    Ta0 = float(request.POST.get("Ta0"))  #K
    T0 = float(request.POST.get("T0"))  #K
    Ua = 16500 # J/(s m³ K)
    m = 0.111 #mol/s
    # DADOS DA ESTEQUIOMETRIA
    a=-1;b=0;c=1;d=1
    yA0=FA0/(FA0+FB0+FC0+FD0+FI0)
    delta= -(1+b/a+c/a+d/a) # Considerando A e B negativos
    E = yA0*delta
    CA0 = yA0*P0/R/T0 #mol/m³
    v0 = FA0/CA0 #m³/s
    HA = -216670 #J/mol
    HB = 0 #J/mol
    HC = -61090 #J/mol
    HD = -74810 #J/mol
    alfaA=26.63 ;betaA=0.183 ;gamaA=-45.83*10**(-6) #J/(mol K)
    alfaB=0 ;betaB=0 ;gamaB=0
    alfaC=20.04 ;betaC=0.0945 ;gamaC=-30.95*10**(-6)
    alfaD=13.39 ;betaD=0.077 ;gamaD=-18.71*10**(-6)
    alfaI=3.280 ;betaI=0.593*10**(-3);deltaI=0.040*10**(5) #N2
    alfaa=3.470 ;betaa=1.450*10**(-3) ;deltaa=0.121*10**(5) #Água
    delta_alfa = a * alfaA + b * alfaB + c * alfaC + d * alfaD
    delta_beta = a * betaA + b * betaB + c * betaC + d * betaD
    delta_gama = a * gamaA + b * gamaB + c * gamaC + d * gamaD

    opcao= request.POST.get("x")
    if opcao == "a":
        Ua=0
        fator=0
    if opcao == "b":
        fator=0 
    if opcao == "c":
        fator=1
    if opcao == "d":
        fator=1 # primeiro calculo cocorrente para sabe o valor final de Ta (Ta0 no contracorrente)

    # CONDIÇÕES INICIAIS
    V0 = 0
    Vf = 0.001 #m³/tubo
    x0 = np.array([0, T0, Ta0]) # Conversão, Temperatura e Temperatura do fluido de troca térmica
    V= np.linspace(V0,Vf,101)

    # SOLUÇÃO DA EQUAÇÃO
    x = odeint(PFR, x0, V)

    if opcao=="d":
        Ta0=x[-1,2]
        CI= np.array([0,T0,Ta0])
        fator=-1
        x=odeint(PFR, CI, V)

    X=x[:,0]
    T=x[:,1]
    Ta =x[:,2]
    return {'V':V, 'X':X, 'T':T, 'Ta':Ta}
######## EXEMPLO 12.2 #########/

######## EXEMPLO 12.4 #########
def e124(request):
    #PARÂMETROS
    deltaH0=-36400 #Btu/lb-mol
    CpA= 35 #Btu/lb-mol·°F
    CpB= 18 #Btu/lb-mol·°F
    CpC= 46 #Btu/lb-mol·°F
    CpM= 19.5 #Btu/lb-mol·°F
    UA= 80*40 #Btu/h·°F
    conversao=4.187 # Btu/lbmol·°F para J/mol K
    Ta= float(request.POST.get("Ta")) #°R
    TaK= Ta*5/9 #K
    R= 1.987 #Btu / lb-mol·°R
    E= 32400 #Btu/lb-mol
    A= 16.96*10**12 #1/h

    alfaA=53.347 ;betaA=0.5154;gamaA=-1.8029E-03; deltaA=2.7795E-06 #J/mol K
    alfaB=92.053 ;betaB=-3.9953E-02 ;gamaB=-2.1103E-04; deltaB=5.3469E-07
    alfaC=118.614 ;betaC=0.6728;gamaC=-1.8377E-03; deltaC=2.1303E-06
    alfaM=40.152 ;betaM=0.3105 ;gamaM=-1.0291E-03; deltaM=1.4598E-06
    a=1;b=1;c=1 #Coeficientes estequiométricos
    HA = -40000 #J/mol
    HB = -60000 #J/mol
    HC = -190000 #J/mol
    #VALORES FICTICIOS DE H

    #VALORES INICIAIS
    T0 = float(request.POST.get("T0"))
    T0K = T0*5/9 #Temperatural inicial em K
    TR = 528 #°R
    TRK= TR*5/9 #K
    Tmax=585 #°R
    FA0= 43.04 #lb-mol/h
    FB0= 802.8 #lb-mol/h
    FC0= 0
    FM0=71.87 #lb-mol/h
    v0= 326.3 #ft³/h
    V= 40.1 #ft³
    tau= V/v0 #h
    CA0 = FA0/v0 #mol/ft³
    vetorXBM=[]
    vetorXBE=[]
    index=[]

    vetorT=np.arange(T0,625,1)
    i=0
    for T in vetorT:
        TK=T*5/9 #Temperatura em K
        integralCpA= alfaA*(TK-T0K)+betaA*(TK**2-T0K**2)/2+gamaA*(TK**3-T0K**3)/3+deltaA*(TK**4-T0K**4)/4 #J/mol
        integralCpB= alfaB*(TK-T0K)+betaB*(TK**2-T0K**2)/2+gamaB*(TK**3-T0K**3)/3+deltaB*(TK**4-T0K**4)/4 #J/mol
        integralCpC= alfaC*(TK-T0K)+betaC*(TK**2-T0K**2)/2+gamaC*(TK**3-T0K**3)/3+deltaC*(TK**4-T0K**4)/4 #J/mol 
        integralCpM= alfaM*(TK-T0K)+betaM*(TK**2-T0K**2)/2+gamaM*(TK**3-T0K**3)/3+deltaM*(TK**4-T0K**4)/4 #J/mol
        deltaH = (HC-HB-HA) + (alfaC-alfaB-alfaA)*(TK - TRK) + (betaC-betaB-betaA)*(TK**2 - TRK**2)/2 
        + (gamaC-gamaB-gamaA)*(TK**3 - TRK**3)/3 + (deltaC-deltaB-deltaA)*(TK**4 - TRK**4)/4 #J/mol

        k = A * np.exp(-E/R/T)  # 1/h
        XBM= tau*k/(1+tau*k)
        XBE= -((integralCpA+(FB0/FA0)*integralCpB+(FM0/FA0)*integralCpM+FC0/FA0*integralCpC)+(UA*(T-Ta)/FA0)*conversao)/deltaH

        vetorXBM.append(XBM)
        vetorXBE.append(XBE)
        index.append(i)
        i+=1
    return {'T':vetorT, 'XBM':vetorXBM, 'XBE':vetorXBE, 'index':index}
######## EXEMPLO 12.4 #########/

######## EXEMPLO 12.5 #########

def reacao(request):
    #PARÂMETROS
    global deltH1A,deltH2A,cpA,cpB,cpC,Ua,Ta,CT0
    deltH1A = float(request.POST.get("\u0394H1"))
    deltH2A = float(request.POST.get("\u0394H2"))
    cpA = float(request.POST.get("cpA"))
    cpB = float(request.POST.get("cpB"))
    cpC = float(request.POST.get("cpC"))
    Ua = float(request.POST.get("Ua"))
    Ta = float(request.POST.get("Ta"))
    CT0 = float(request.POST.get("CT0"))

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

######## EXEMPLO 12.5 #########/

######## EXEMPLO 12.6 #########
def e126(request):
    deltaH1 = float(request.POST.get("\u0394H1"))
    deltaH2 = float(request.POST.get("\u0394H2"))
    UA = float(request.POST.get("UA"))
    Ta = float(request.POST.get("Ta"))
    CpA = float(request.POST.get("cpA"))
    CpB = float(request.POST.get("cpB"))
    CpC = float(request.POST.get("cpC"))
    E1 = float(request.POST.get("E1"))
    E2 = float(request.POST.get("E2"))
    T0 = float(request.POST.get("T0")) 
    Tf = float(request.POST.get("Tf")) 
    CA0 = float(request.POST.get("CA0"))
    v0 = float(request.POST.get("v0"))
    V = float(request.POST.get("V"))

    #PARÂMETROS
    R= 1.987 #cal/mol K
    A1= 3.3/np.exp(-E1/R/300) #1/min
    A2= 4.58/np.exp(-E2/R/500) #1/min

    alfaA=200 ;betaA=0.183*0 ;gamaA=-45.83*10**(-6)*0 #J/(mol K)
    alfaB=200 ;betaB=0.077*0 ;gamaB=-18.71*10**(-6)*0
    alfaC=200 ;betaC=0.0945*0 ;gamaC=-30.95*10**(-6)*0
    a=1;b=1;c=1 #Coeficientes estequiométricos
    HA = -50000 #J/mol
    HB = -105000 #J/mol
    HC = -176500 #J/mol

    #VALORES INICIAIS
    tau=V/v0
    FA0=CA0*v0
    FB0=0
    FC0=0
    vetorG=[]
    vetorR=[]
    EE={"T":[],"CA":[],"CB":[],"CC":[]} #Estado Estacionário
    dif=[]
    vetorCA=[]
    vetorCB=[]
    vetorCC=[]

    #EDO
    #Tf valor final de temperatura em K
    vetorT = np.arange(T0, Tf, 5)

    for T in vetorT:
        
        CpA=alfaA+betaA*T+gamaA*T**2 # J/(mol K)
        CpB=alfaB+betaB*T+gamaB*T**2 # J/(mol K)
        CpC=alfaC+betaC*T+gamaC*T**2 # J/(mol K)
        deltaH1 = (b*HB - a*HA ) + (alfaB-alfaA)*(T - 298) + (betaB-betaA)*(T**2 - 298**2)/2 + (gamaB-gamaA)*(T**3 - 298**3)/3  # J/mol
        deltaH2 = (c*HC - b*HB) + (alfaC-alfaB)*(T - 298) + (betaC-betaB)*(T**2 - 298**2)/2 + (gamaC-gamaB)*(T**3 - 298**3)/3  # J/mol

        k1 = A1 * np.exp(-E1/R/T)  # 1/min
        k2 = A2 * np.exp(-E2/R/T)  # 1/min
        CA=CA0/(1+tau*k1)
        CB=tau*k1*CA0/((1+tau*k1)*(1+tau*k2))
        r1A= -k1*CA
        r1B= -r1A
        r2B= -k2*CB
        rC=-r2B
        CC=tau*rC
        GT= (deltaH1*r1A+deltaH2*r2B)*V
        RT= UA*(T-Ta)+FA0*(1*CpA+FB0/FA0*CpB+FC0/FA0*CpC)*(T-T0)
        vetorG.append(GT)
        vetorR.append(RT)
        dif.append(abs(GT-RT))
        vetorCA.append(CA)
        vetorCB.append(CB)
        vetorCC.append(CC)
        """
        if abs(GT-RT)<499000:
            EE["T"].append(float(T))
            EE["CA"].append(round(float(CA),4)) #round(): arrendonda o valor
            EE["CB"].append(round(float(CB),4))
            EE["CC"].append(round(float(CC),4))
            """

    valor_anterior=1e8
    for i,x in enumerate(dif):
        if x < valor_anterior:
            valor_anterior = x
            index=i
            validacao=1
        else:
            if validacao==1:
                EE["T"].append(vetorT[index])
                EE["CA"].append(vetorCA[index])
                EE["CB"].append(vetorCB[index])
                EE["CC"].append(vetorCC[index])
                valor_anterior=1e9
                validacao=0

        
    return [vetorT, vetorG, vetorR, EE]

######## EXEMPLO 12.6 #########/

######## EXEMPLO 12.7 #########

def e127(request):

    def edo_e127(CI,V):
        T=CI[0]
        FA=CI[1]
        FB=CI[2]
        FC=CI[3]
        FD=CI[4]
        Ta=CI[5]

        p=(1-alfa*V)**0.5 #Queda de pressão nos tubos
        k1A = 40 * np.exp(E1/R * (1 / 300 - 1 / T))  # 1/s
        k2C = 2 * np.exp(E2/R * (1 / 300 - 1 / T))  # L/mol s
        FT = FA + FB + FC + FD
        CA = CT0 * (FA / FT) * (T0 / T)*p
        CB = CT0 * (FB / FT) * (T0 / T)*p
        CC = CT0 * (FC / FT) * (T0 / T)*p
        r1A = -k1A * CA * CB**2
        r2C = -k2C * CA**2 * CC**3
        dTdV = ((-2*r1A)*(-deltH1B) + (-2/3*r2C)*(-deltH2A) - Ua*(T-Ta)) / (FA*CpA + FB*CpB + FC*CpC +FD*CpD)
        dFAdV = r1A+2/3*r2C
        dFBdV = 2*r1A
        dFCdV = -r1A+r2C
        dFDdV = -r2C/3
        dTadV = Ua * (T - Ta) / (mc * CpC0) *x #cocorrente, x
        return np.array([dTdV,dFAdV,dFBdV,dFCdV,dFDdV,dTadV])
    
    #PARÂMETROS
    deltH1B=-15000 #cal/molB
    deltH2A=-10000 #cal/molA
    CpA= 10 #cal/mol K
    CpB= 12 #cal/mol K
    CpC= 14 #cal/mol K
    CpD= 16 #cal/mol K
    CpC0= 10 #cal/mol K
    Ua= 80 #cal/(m³ min K)
    Ta0= float(request.POST.get("Ta")) 
    mc= 50 #mol/min
    R= 1.987 #cal/mol K
    E1= 8000 #cal/mol
    E2= 12000 #cal/mol
    alfa=0.01 #Parâmetro da queda de pressão

    opcao= request.POST.get("x")
    if opcao == "a":
        x=1
    if opcao == "b":
        x=1 # primeiro calculo cocorrente para sabe o valor final de Ta (Ta0 no contracorrente)
    if opcao == "c":
        x=0
    if opcao == "d":
        Ua=0
        x=0
    #VALORES INICIAIS
    FA0 = float(request.POST.get("FA")) 
    FB0 = float(request.POST.get("FB")) 
    FC0 = float(request.POST.get("FC")) 
    FD0 = float(request.POST.get("FD")) 
    T0 = float(request.POST.get("T")) 
    CT0 = 0.2  # mol/L

    #EDO
    CI= np.array([T0,FA0,FB0,FC0,FD0,Ta0])
    Vf=10.1 #L
    V = np.arange(0, Vf, 0.1)  # faixa de variação do volume
    x = odeint(edo_e127, CI, V)

    if opcao=="b":
        Ta0=x[-1,5]
        CI= np.array([T0,FA0,FB0,FC0,FD0,Ta0])
        x=-1
        x=odeint(edo_e127, CI, V)

    return {'V':V, 'x':x}

######## EXEMPLO 12.7 #########/

######## EXEMPLO 13.1 #########

def e131(request):
    def Batelada(CI,t):
        T=CI[0]
        X=CI[1]
        k = A * np.exp(-E/R/T)  # 1/s
        CA = CA0 * (1-X)
        lista.append(CA)
        rA = -k * CA
        deltaH = deltaH0 # considerando deltaCp=0
        Qrb= mc*CpC_massico*((T-Ta)*(1-np.exp(-UA/(mc*CpC_massico))))*fator
        Qgb= (-rA*V)*(-deltaH)
        dTdt= (Qgb-Qrb)/(NA0*CpA+NB0*CpB+NM*CpM)
        dXdt = -rA*V/NA0
        return np.array([dTdt,dXdt])
    
    #PARÂMETROS
    deltaH0=-20202 #cal/mol
    CpA= 35 #cal/mol K
    CpB= 18 #cal/mol K
    CpC= 46 #cal/mol K
    CpC_massico= 4.16 #cal/g K
    CpM= 19.5 #cal/mol K
    deltaCp= CpA + CpB - CpC
    UA= 10 #cal/s/K
    Ta= float(request.POST.get("Ta"))  #K
    mc= 10 #g/s
    R= 1.987 #cal/mol K
    E= 18000 #cal/mol
    A= 4.71 * 10**9 # 1/s
    V= float(request.POST.get("V"))  #dm³

    #CASOS
    resposta=request.POST.get("x")
    if resposta=="a":
        fator=0
    else:
        fator=1

    #VALORES INICIAIS
    NA0=float(request.POST.get("NA0")) 
    NB0=float(request.POST.get("NB0")) 
    NM=float(request.POST.get("NM")) 
    T0 = float(request.POST.get("T0")) 
    X0 = float(request.POST.get("X0")) 
    CA0 = NA0/V # fase líquida V=V0
    lista=[CA0]

    #EDO
    CI= np.array([T0,X0])
    tf=float(request.POST.get("tf"))  #s
    t = np.arange(0, tf+40, 40)  # faixa de variação do tempo
    x = odeint(Batelada, CI, t)
    return {'t':t, 'x':x}

######## EXEMPLO 13.1 #########/

######## EXEMPLO 13.2 #########
def e132(request):

    def Adiabatico(CI,t):
        T=CI[0]
        X=CI[1]
        k = A * np.exp(-E/R/T)  # m³/kmol/min
        CA = CA0 * (1-X)
        CB = CA0 * (NB0/NA0 -2*X) 
        rA = -k * CA *CB
        fator=1
        UA=0 #kcal/(min K)
        if t <= 45:
            fator=0
        if t > 55:
            UA = 35.85 #kcal/(min K)
        dTdt= ((rA*deltaH*V -UA*(T-Ta))/(NA0*CpA+NB0*CpB+NW*CpW))*fator
        dXdt = -rA*V/NA0
        return np.array([dTdt,dXdt])

    #PARÂMETROS
    deltaH=-5.9*10**5 #kcal/kmol (considerando deltaCp=0)
    CpA= 40 #cal/mol K
    CpB= 8.38 #cal/mol K
    CpW= 18 #cal/mol K
    Ta = float(request.POST.get("Ta"))
    R= 1.987 #cal/mol K
    E= 11273 #cal/mol
    A= 0.00017/np.exp(-E/R/461) # m³/kmol/min
    V= 5.1 #m³

    #VALORES INICIAIS
    NA0=float(request.POST.get("NA0")) 
    NB0=float(request.POST.get("NB0")) 
    NW=float(request.POST.get("NM")) 
    T0 = float(request.POST.get("T0")) 
    X0 = float(request.POST.get("X0")) 
    NA0=9.044 # kmol
    NB0=33.0 #kmol
    NW=103.7 #kmol - inerte (água)
    T0 = 448  # K
    X0 = 0
    CA0 = NA0/V 

    #EDO
    CI= np.array([T0,X0])
    tf=121 #min
    t = np.arange(0, tf+1, 1)  # faixa de variação do tempo
    x = odeint(Adiabatico, CI, t)

    return {'t':t, 'x':x}

######## EXEMPLO 13.2 #########/

######## EXEMPLO 13.5 #########
def e135(request):
    def Semibatelada(CI,t):
        T=CI[0]
        CA=CI[1]
        CB=CI[2]
        CC=CI[3]
        k1 = A1 * np.exp(-E1/R/T)  # 1/h
        k2 = A2 * np.exp(-E2/R/T)  # 1/h
        rA = -k1 * CA
        rC = 3 * k2 * CB
        rB1 = -rA/2 
        rB2 = -rC/3
        rB = rB1 + rB2
        V = V0 + v0*t
        dCAdt = rA + (CA0-CA)*v0/V
        dCBdt = rB + (CB0-CB)*v0/V
        dCCdt = rC + (CC0-CC)*v0/V
        dTdt= (UA*(Ta-T)-FA0*CpA*(T-T0)+(deltaH1*rA+deltaH2*rB2)*V)/((CA*CpA+CB*CpB+CC*CpC)*V+Nh2so4*Cph2so4)
        return np.array([dTdt,dCAdt,dCBdt,dCCdt])

    #PARÂMETROS
    deltaH1=-6500 #cal/molA
    deltaH2=8000 #cal/molB
    CpA= 30 #cal/mol K
    CpB= 60 #cal/mol K
    CpC= 20 #cal/mol K
    Cph2so4= 35 #cal/mol K
    UA= 35000 #cal/h/K
    Ta= 298 #K
    R= 1.987 #cal/mol K
    E1= 9500 #cal/mol
    E2= 7000 #cal/mol
    A1= 1.25/np.exp(-E1/R/320) 
    A2= 0.08/np.exp(-E2/R/300) 

    #VALORES INICIAIS
    T0 = float(request.POST.get("T0")) 
    Ti = float(request.POST.get("Ti")) 
    CAi = float(request.POST.get("CAi")) 
    CBi = float(request.POST.get("CBi")) 
    CCi = float(request.POST.get("CCi")) 
    Ch2o4 = 1 #mol/dm³ 
    CA0 = float(request.POST.get("CA0")) 
    CB0 = float(request.POST.get("CB0")) 
    CC0 = float(request.POST.get("CC0")) 
    v0= 240 #dm³/h
    V0=100 #dm³
    Nh2so4=Ch2o4*V0 #mol
    FA0= CA0*v0 #mol

    #EDO
    CI= np.array([Ti,CAi,CBi,CCi])
    tf=1.5 #h
    t = np.arange(0, tf, 0.015)  # faixa de variação do tempo
    x = odeint(Semibatelada, CI, t)
    return {'t':t, 'x':x}
######## EXEMPLO 13.5 #########/

######## PROBLEMA 12.16 #########
def p1216(request):
    #PARÂMETROS
    deltaH0=-80000 #cal/molA
    CpA= 40 #cal/mol K
    CpB= 40 #cal/mol K
    UA= float(request.POST.get("UA")) #cal/min/K
    Ta= float(request.POST.get("Ta"))  #K
    R= 1.987 #cal/mol K
    E= 20000*R #cal/mol

    ki = float(request.POST.get("k"))
    Tki = float(request.POST.get("Tk"))
    Kci = float(request.POST.get("Kc"))
    TKci = float(request.POST.get("TKc"))
    A= ki/np.exp(-E/R/Tki) #1/min
    Aeq= Kci/np.exp(-deltaH0/R/TKci)

    #A: m-cymene, B:p-cymene
    alfaA=121.295 ;betaA=0.8535*0;gamaA=-2.2176E-03*0; deltaA=2.5641E-06*0 #J/(mol K)
    alfaB=121.863 ;betaB=0.8159*0 ;gamaB=-2.1402E-03*0; deltaB=2.5029E-06*0
    alfaA=40;alfaB=40
    a=1;b=1;c=1 #Coeficientes estequiométricos
    HA = -30.9*1000 #J/mol
    HB = -29*1000 #J/mol

    #VALORES INICIAIS
    T0 = float(request.POST.get("T0"))  # K 
    v0= 1 #dm³/min
    V=10 #dm³
    tau=V/v0
    FA0=float(request.POST.get("FA0"))  #mol/min
    FB0=float(request.POST.get("FB0")) 
    CA0=FA0*v0
    vetorG=[]
    vetorR=[]
    EE={"T":[],"CA":[],"CB":[],"XBM":[],"XBE":[],"Xeq":[],"indexEE":[]} #Estado Estacionário
    vetorXBM=[]
    vetorXBE=[]
    vetorXeq=[]

    vetorT=np.arange(T0,450,1)
    i=0
    index=[]
    TEE=[]
    for T in vetorT:
        
        CpA=alfaA+betaA*T+gamaA*T**2+deltaA*T**3 # cal/(mol K)
        CpB=alfaB+betaB*T+gamaB*T**2+deltaB*T**3 # cal/(mol K)
        integralCpA=(alfaA*(T-T0)+betaA*(T**2-T0**2)+gamaA*(T**3-T0**3)+deltaA*(T**4-T0**4))
        integralCpB=(alfaB*(T-T0)+betaB*(T**2-T0**2)+gamaB*(T**3-T0**3)+deltaB*(T**4-T0**4))
        deltaH = deltaH0 + (alfaB-alfaA)*(T-298) + (betaB-betaA)*(T**2-298**2)/2 + (gamaB-gamaA)*(T**3-298**3)/3 + (deltaB-deltaA)*(T**4-298**4)/4  # J/mol

        k = A * np.exp(-E/R/T)  # 1/min
        Kc = Aeq * np.exp(-deltaH0/R/T)  # 1/min

        XBM=tau*k/(1+tau*k+tau*k/Kc)
        XBE= -((CpA+(FB0/FA0)*CpB)*(T-T0)+(UA*(T-Ta)/FA0))/deltaH
        Xeq=Kc/(1+Kc)

        vetorXBM.append(XBM)
        vetorXBE.append(XBE)
        vetorXeq.append(Xeq)

        CA=CA0*(1-XBM)
        CB=CA0*XBM
        GT= XBM*(-deltaH)
        RT= UA/FA0*(T-Ta)+(1*integralCpA+FB0/FA0*integralCpB)

        vetorG.append(GT)
        vetorR.append(RT)
        index.append(i)
        i+=1
        if np.isclose(XBM,XBE,rtol=0.09):
            TEE.append(round(T,2))

    return {'T':vetorT, 'XBM':vetorXBM, 'XBE':vetorXBE, 'Xeq':vetorXeq, 'TEE':TEE, 'GT':vetorG, 'RT':vetorR, 'index':index}
######## PROBLEMA 12.16 #########/

######## PROBLEMA 12.23 #########
def p1223(request):
    def Multiplas_e_Reversivel(CI,V):
        T=CI[0]
        FA=CI[1]
        FB=CI[2]
        FC=CI[3]
        Ta=CI[4]
        FT=FA+FB+FC
        v=v0*(FT/FT0)*(T/T0)
        CA=FA/v
        CB=FB/v
        CC=FC/v
        Kca=Aeq*np.exp(-deltaH1A/R/T) #dm³/mol 
        k1 = A1 * np.exp(-E1/R/T)  #dm³/mol · min
        k2 = A2 * np.exp(-E2/R/T)  #dm6/mol² · min
        r1A = -k1*((CA**2)-CB/Kca) 
        r2C = k2*(CB**2)*CA 
        rA= r1A -r2C
        rB= -r1A -2*r2C
        rC= r2C
        dFAdV = rA
        dFBdV = rB
        dFCdV = rC
        dTdV= (Ua*(Ta-T)+(deltaH1A*(r1A)+deltaH2B*(-2*r2C)))/(FA*CpA + FB*CpB + FC*CpC)
        dTadV = Ua*(T-Ta)/(mc*CpRefri)*fator
        return np.array([dTdV,dFAdV,dFBdV,dFCdV,dTadV])

    #PARÂMETROS
    deltaH1A=-20*1000 #J/molA
    deltaH2B=30*1000 #J/molB
    CpA= 20 #J/mol K
    CpB= 80 #J/mol K
    CpC= 100 #J/mol K
    deltaCp1= 2*CpB-2*CpA
    deltaCp2= CpC-CpA-2*CpB
    CpRefri= 10 #J/mol K
    mc= 50 #mol/min
    Ua= 200 #J/(dm³ min K)
    Ta0= float(request.POST.get("Ta0")) #K
    R= 8.31 #J/mol K
    E1= 8000 #J/mol
    E2= 4000 #J/mol

    k1 = float(request.POST.get("k1"))
    Tk1 = float(request.POST.get("Tk1"))
    k2 = float(request.POST.get("k2"))
    Tk2 = float(request.POST.get("Tk2"))
    Kc = float(request.POST.get("Kc"))
    TKc = float(request.POST.get("TKc"))

    A1= k1/np.exp(-E1/R/Tk1) #dm³/mol
    A2= k2/np.exp(-E2/R/Tk2) #(dm³/mol)²
    Aeq= Kc/np.exp(-deltaH1A/R/TKc)

    #VALORES INICIAIS
    T0 = float(request.POST.get("T0")) # K - Temperatura da alimentação
    CA0 = 0.2 #mol/dm³ 
    CB0 = 1
    CC0 = 1
    FA0= float(request.POST.get("FA0")) #mol/min
    FB0= float(request.POST.get("FB0"))
    FC0= float(request.POST.get("FC0"))
    FT0=FA0+FB0+FC0 #Alimentação de A puro
    v0= FA0/CA0+FB0/CB0+FC0/CC0 #dm³/min

    opcao= request.POST.get("x")
    if opcao == "a":
        fator=1
    if opcao == "b":
        fator=1 # primeiro calculo cocorrente para sabe o valor final de Ta (Ta0 no contracorrente)
    if opcao == "c":
        fator=0
    if opcao == "d":
        Ua=0
        fator=0

    #EDO
    CI= np.array([T0,FA0,FB0,FC0,Ta0])
    Vf=10 #dm³
    V = np.arange(0, Vf+0.1, 0.1)  # faixa de variação do tempo
    x = odeint(Multiplas_e_Reversivel, CI, V)

    if opcao=="b":
        Ta0=x[-1,4]
        CI= np.array([T0,FA0,FB0,FC0,Ta0])
        fator=-1
        x=odeint(Multiplas_e_Reversivel, CI, V)

    T = x[:,0]
    FA = x[:,1]
    FB = x[:,2]
    FC = x[:,3]
    Ta = x[:,4]
    index= []
    
    for i,y in enumerate(V):
        index.append(i)
    return {'V':V, 'T':T, 'FA':FA, 'FB':FB, 'FC':FC, 'Ta':Ta, 'index':index}
######## PROBLEMA 12.23 #########/