from django.db import models
from scipy.integrate import odeint
import numpy as np

# Create your models here.
    
class Dados(models.Model):
    FA = models.FloatField(default=100, help_text="mol/s")
    FB = models.FloatField(default=0, help_text="mol/s")
    FC = models.FloatField(default=0, help_text="mol/s")
    T = models.FloatField(default=423, help_text="K")
    V = models.FloatField(default=0)

    def __str__(self):
        return "{self.T}"
    
class Const(models.Model):
    delta = '\u0394' #delta unicode
    #\u22C5 unicode para o ponto de multiplicação: ⋅
    deltaH1 = models.FloatField(name=f"{delta}H1", default=-20000, help_text="J/molA")
    deltaH2 = models.FloatField(name=f"{delta}H2", default=-60000, help_text="J/molA")
    cpA = models.FloatField(default=90, help_text="J/mol°C")
    cpB = models.FloatField(default=90, help_text="J/mol°C")
    cpC = models.FloatField(default=180, help_text="J/mol°C")
    Ua = models.FloatField(default=4000, help_text="J/m³\u22C5s\u22C5°C")
    Ta0 = models.FloatField(default=373, help_text="K")
    CT0 = models.FloatField(default=0.1, help_text="mol/L")

    def __str__(self):
        return "{self.T}"
    
class E102(models.Model):
    W = models.FloatField(default=0)
    X = models.FloatField(default=290, help_text="")
    p = models.FloatField(default=1, help_text="")
    PT0 = models.FloatField(default=12, help_text="atm")
    PH20 = models.FloatField(default=18, help_text="atm")
    PB0 = models.FloatField(default=0, help_text="atm")
    
    def __str__(self):
        return "{self.t}"
    
class E122(models.Model):
    V = models.FloatField(default=0, help_text="")
    X = models.FloatField(default=0, help_text="")
    T0 = models.FloatField(default=1035, help_text="K")
    Ta0 = models.FloatField(default=1250, help_text="K")
    
class E124(models.Model):
    T0 = models.FloatField(default=550, help_text="R")
    XBM = models.FloatField(default=0, help_text="")
    XBE = models.FloatField(default=0, help_text="")
    
    def __str__(self):
        return "{self.T0}"

class E126(models.Model):
    deltaH1 = models.FloatField(name="\u0394H1", default=-55000, help_text="J/molA")
    deltaH2 = models.FloatField(name="\u0394H2", default=-71500, help_text="J/molB")
    cpA = models.FloatField(default=200, help_text="J/mol K")
    cpB = models.FloatField(default=200, help_text="J/mol K")
    cpC = models.FloatField(default=200, help_text="J/mol k")
    UA = models.FloatField(default=40000, help_text="J/min\u22C5K")
    Ta0 = models.FloatField(default=330, help_text="K")
    E1= models.FloatField(default=9900, help_text="cal/mol")
    E2= models.FloatField(default=27000, help_text="cal/mol")

    alfaA=200 ;betaA=0.183*0 ;gamaA=-45.83*10**(-6)*0 #J/(mol K)
    alfaB=200 ;betaB=0.077*0 ;gamaB=-18.71*10**(-6)*0
    alfaC=200 ;betaC=0.0945*0 ;gamaC=-30.95*10**(-6)*0
    a=1;b=1;c=1 #Coeficientes estequiométricos
    HA = -50000 #J/mol
    HB = -105000 #J/mol
    HC = -176500 #J/mol

    #VALORES INICIAIS
    T0 = models.FloatField(default=283, help_text="K")
    Tf = models.FloatField(default=740, help_text="K")
    CA0 = models.FloatField(default=0.3, help_text="mol/L") 
    v0 = models.FloatField(default=1000, help_text="L/min") 
    V = models.FloatField(default=10, help_text="L/min") 
    #FA0=CA0*v0
    FB0=0
    FC0=0
    def __str__(self):
            return "{self.T0}"
    
class E127(models.Model):
     V = models.FloatField(default=10, help_text="L")
     T = models.FloatField(default=300, help_text="K")
     FA = models.FloatField(default=5, help_text="mol/min")
     FB = models.FloatField(default=10, help_text="mol/min")
     FC = models.FloatField(default=0, help_text="mol/min")
     FD = models.FloatField(default=0, help_text="mol/min")
     Ta0 =models.FloatField(default=325, help_text="K")
     def __str__(self):
            return "{self.T}"
     
class E131(models.Model):
    X0 = models.FloatField(default=0, help_text="")
    T0 = models.FloatField(default=286, help_text="K")
    t = models.FloatField(default=0)
    def __str__(self):
        return "{self.T}"
    
class E135(models.Model):
    t = models.FloatField(default=0)
    Ti = models.FloatField(default=290, help_text="K")
    CAi = models.FloatField(default=1, help_text="mol/L")
    CBi = models.FloatField(default=0, help_text="mol/L")
    CCi = models.FloatField(default=0, help_text="mol/L")
    
    def __str__(self):
        return "{self.t}"
    
class P1216(models.Model):
    T0 = models.FloatField(default=280, help_text="K")
    XBM = models.FloatField(default=0, help_text="")
    XBE = models.FloatField(default=0, help_text="")
    Xeq = models.FloatField(default=0, help_text="")
    GT = models.FloatField(default=0, help_text="cal/mol")
    RT = models.FloatField(default=0, help_text="cal/mol")

class P1223(models.Model):
    V = models.FloatField(default=0)
    T0 = models.FloatField(default=300, help_text="K")
    FA0 = models.FloatField(default=5, help_text="mol/min")
    FB0 = models.FloatField(default=0, help_text="mol/min")
    FC0 = models.FloatField(default=0, help_text="mol/min")
    Ta0 = models.FloatField(default=320, help_text="K")
