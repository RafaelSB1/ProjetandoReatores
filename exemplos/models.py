from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


# Create your models here.
    
class E125(models.Model):
    FA = models.FloatField(default=100, help_text="mol/s", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(1000, message="O valor deve ser menor que 1000")])
    FB = models.FloatField(default=0, help_text="mol/s", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(1000, message="O valor deve ser menor que 1000")])
    FC = models.FloatField(default=0, help_text="mol/s", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(1000, message="O valor deve ser menor que 1000")])
    T = models.FloatField(default=423, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    V = models.FloatField(default=0)
    deltaH1 = models.FloatField(name="\u0394H1", default=-20000, help_text="J/molA")
    deltaH2 = models.FloatField(name="\u0394H2", default=-60000, help_text="J/molB")

    
    
class E102(models.Model):
    W = models.FloatField(default=0)
    X = models.FloatField(default=290, help_text="")
    p = models.FloatField(default=1, help_text="")
    PT0 = models.FloatField(default=12, help_text="atm", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    PH20 = models.FloatField(default=18, help_text="atm", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    PB0 = models.FloatField(default=0, help_text="atm",  validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    
    def __str__(self):
        return "{self.t}"

class E103(models.Model):
    W = models.FloatField(default=0)
    X = models.FloatField(default=290, help_text="")
    p = models.FloatField(default=1, help_text="")
    PT0 = models.FloatField(default=12, help_text="atm", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    PH20 = models.FloatField(default=18, help_text="atm", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    PB0 = models.FloatField(default=0, help_text="atm",  validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    
class E104(models.Model):
    x=0

class E122(models.Model):
    V = models.FloatField(default=0, help_text="")
    X = models.FloatField(default=0, help_text="")
    T0 = models.FloatField(default=1035, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    Ta0 = models.FloatField(default=1250, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    
class E124(models.Model):
    T0 = models.FloatField(default=550, help_text="R", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    XBM = models.FloatField(default=0, help_text="")
    XBE = models.FloatField(default=0, help_text="")
    
    def __str__(self):
        return "{self.T0}"

class E126(models.Model):
    deltaH1 = models.FloatField(name="\u0394H1", default=-55000, help_text="J/molA")
    deltaH2 = models.FloatField(name="\u0394H2", default=-71500, help_text="J/molB")
    cpA = models.FloatField(default=200, help_text="J/(mol ⋅ K)")
    cpB = models.FloatField(default=200, help_text="J/(mol ⋅ K)")
    cpC = models.FloatField(default=200, help_text="J/(mol ⋅ K)")
    UA = models.FloatField(default=40000, help_text="J/(min\u22C5K)",  validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100000, message="O valor deve ser menor que 100000")])
    Ta0 = models.FloatField(default=330, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
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
    T0 = models.FloatField(default=283, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    Tf = models.FloatField(default=740, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    CA0 = models.FloatField(default=0.3, help_text="mol/L", validators=[MinValueValidator(0.1, message="O valor deve ser maior que 0,1"), MaxValueValidator(100, message="O valor deve ser menor que 100")]) 
    v0 = models.FloatField(default=1000, help_text="L/min", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(10000, message="O valor deve ser menor que 10000")]) 
    V = models.FloatField(default=10, help_text="L/min", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(1000, message="O valor deve ser menor que 1000")]) 
    #FA0=CA0*v0
    FB0=0
    FC0=0
    def __str__(self):
            return "{self.T0}"
    
class E127(models.Model):
     V = models.FloatField(default=10, help_text="L")
     T = models.FloatField(default=300, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
     FA = models.FloatField(default=5, help_text="mol/min", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
     FB = models.FloatField(default=10, help_text="mol/min", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
     FC = models.FloatField(default=0, help_text="mol/min", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(2000, message="O valor deve ser menor que 100")])
     FD = models.FloatField(default=0, help_text="mol/min", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
     Ta0 =models.FloatField(default=325, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
     def __str__(self):
            return "{self.T}"
     
class E131(models.Model):
    X0 = models.FloatField(default=0, help_text="", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(1, message="O valor deve ser menor que 1")])
    T0 = models.FloatField(default=286, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    t = models.FloatField(default=0)
    def __str__(self):
        return "{self.T}"
    
class E135(models.Model):
    t = models.FloatField(default=0)
    Ti = models.FloatField(default=290, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    CAi = models.FloatField(default=1, help_text="mol/L", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    CBi = models.FloatField(default=0, help_text="mol/L", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    CCi = models.FloatField(default=0, help_text="mol/L", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    
    def __str__(self):
        return "{self.t}"
    
class P1216(models.Model):
    T0 = models.FloatField(default=280, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    XBM = models.FloatField(default=0, help_text="")
    XBE = models.FloatField(default=0, help_text="")
    Xeq = models.FloatField(default=0, help_text="")
    GT = models.FloatField(default=0, help_text="cal/mol")
    RT = models.FloatField(default=0, help_text="cal/mol")

class P1223(models.Model):
    V = models.FloatField(default=0)
    T0 = models.FloatField(default=300, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])
    FA0 = models.FloatField(default=5, help_text="mol/min", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    FB0 = models.FloatField(default=0, help_text="mol/min", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    FC0 = models.FloatField(default=0, help_text="mol/min", validators=[MinValueValidator(0, message="O valor deve ser maior que 0"), MaxValueValidator(100, message="O valor deve ser menor que 100")])
    Ta0 = models.FloatField(default=320, help_text="K", validators=[MinValueValidator(1, message="O valor deve ser maior que 1"), MaxValueValidator(2000, message="O valor deve ser menor que 2000")])

class DTR1(models.Model):
    t = models.CharField(default = "[0, 5, 10, 15, 20, 30, 40, 50, 70, 100, 150, 200]", help_text="min", max_length=1000)
    C = models.CharField(default = "[112, 95.8, 82.2, 70.6, 60.9, 45.6, 34.5, 26.3, 15.7, 7.67, 2.55, 0.90]", help_text="mg/dm³", max_length=1000, name="C(t)")

class DTR2(models.Model):
    t = models.CharField(default = "[4, 8, 10, 14, 16, 18]", help_text="min", max_length=1000)
    C = models.CharField(default = "[1000, 1333, 1500, 1666, 1750, 1800]", help_text="mg/dm³", max_length=1000, name="C(t)")

class DTR3(models.Model):
    t = models.CharField(default = "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]", help_text="min", max_length=1000)
    C = models.CharField(default = "[0, 1.4, 5, 8, 10, 8, 6, 4, 3, 2.2, 1.6, 0.6, 0]", help_text="mg/dm³", max_length=1000, name="C(t)")

class DTR4(models.Model):
    t = models.CharField(default = "[0, 20, 40, 60, 80, 120, 160, 200, 240, 280, 320]", help_text="min", max_length=1000)
    C = models.CharField(default = "[2000, 1050, 520, 280, 160, 61, 29, 16.4, 10, 6.4, 4]", help_text="mg/dm³", max_length=1000, name="C(t)")