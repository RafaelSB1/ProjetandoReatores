from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML

class E125Form(forms.ModelForm):

    delta = '\u0394' #delta unicode
    #\u22C5 unicode para o ponto de multiplicação: ⋅initial
    cpA = forms.FloatField(initial=90, help_text="J/(mol\u22C5°C)")
    cpB = forms.FloatField(initial=90, help_text="J/(mol\u22C5°C)")
    cpC = forms.FloatField(initial=180, help_text="J/(mol\u22C5°C)")
    Ua = forms.FloatField(initial=4000, help_text="J/(m³\u22C5s\u22C5°C)", min_value=0, max_value=100000)
    Ta0 = forms.FloatField(initial=373, help_text="K", min_value=1, max_value=2000)
    CT0 = forms.FloatField(initial=0.1, help_text="mol/L", min_value=0.01, max_value=100)
    
    class Meta:
        model = E125
        fields = ['FA','FB','FC','T','\u0394H1','\u0394H2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]


class E102Form(forms.ModelForm):
    tf = forms.FloatField(initial=0, help_text="período de desativação do catalisador em dias", min_value=0, max_value=1000)
    class Meta:
        model = E102
        fields = ['PT0','PH20','PB0']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class E103Form(forms.ModelForm):
    PE = forms.CharField(initial="1,1,1,3,5,0.5,0.5,0.5,0.5", help_text="atm")
    PH = forms.CharField(initial="1,3,5,3,3,3,5,3,1", help_text="atm")
    PEA = forms.CharField(initial="1,1,1,1,1,1,0.5,3,5", help_text="atm")
    taxa = forms.CharField(initial="1.04,3.13,5.21,3.82,4.19,2.391,3.867,2.199,0.75", label="taxa", help_text="mol/(kgcat \u2022 s)")
    class Meta:
        model = E103
        fields = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class E104Form(forms.ModelForm):
    E = forms.FloatField(initial=20000, help_text="cal/mol", min_value=0)
    Ed = forms.FloatField(initial=75000, help_text="cal/mol", min_value=0)
    T = forms.FloatField(initial=300, help_text="K", min_value=0, max_value= 2000)
    k0 = forms.FloatField(initial=0.01, help_text="1/s", min_value=0)
    Tk0 = forms.FloatField(initial=300, help_text="K", min_value=0, max_value= 2000)
    k0d = forms.FloatField(initial=0.1, help_text="1/s", min_value=0)
    Tk0d = forms.FloatField(initial=300, help_text="K", min_value=0, max_value= 2000)
    class Meta:
        model = E103
        fields = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class E122Form(forms.ModelForm):
    opcoes = [
        ('a','1. Processo adiabático'),
        ('b','2. Transferência de calor, com Ta constante'),
        ('c','3. Transferência de calor em cocorrente, com Ta variável'),
        ('d','4. Transferência de calor em contracorrente, com Ta variável'),
]

    FI0 = forms.FloatField(initial=0.376, help_text="mol/s", min_value=0, max_value= 10)
    FA0 = forms.FloatField(initial=0.0376, help_text="mol/s", min_value=0, max_value= 10)
    FB0 = forms.FloatField(initial=0, help_text="mol/s", min_value=0, max_value= 10)
    FC0 = forms.FloatField(initial=0, help_text="mol/s", min_value=0, max_value= 10)
    FD0 = forms.FloatField(initial=0, help_text="mol/s", min_value=0, max_value= 10)

    x=forms.ChoiceField(label='Selecione a alternativa a ser resolvida:', choices=opcoes, required=False, widget=forms.RadioSelect, initial='a')

    class Meta:
        model = E122
        fields = ['T0','Ta0']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            if i == 'x':
                self.fields[i].widget.attrs.update({'class':""})
            else:
                self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
                self.fields[i].label = listaDeSimbolos[i]

class E124Form(forms.ModelForm):
    Ta0 = forms.FloatField(initial=545, help_text="R", min_value=1, max_value=2000)
    V = forms.FloatField(initial=40.1, help_text="ft³", min_value=0, max_value=500)
    v0 = forms.FloatField(initial=326.3, help_text="ft³/h", min_value=0, max_value=1000)
    FA0 = forms.FloatField(initial=43.04, help_text="lb-mol/h", min_value=0, max_value=1000)
    FB0 = forms.FloatField(initial=802.8, help_text="lb-mol/h", min_value=0, max_value=5000)
    FC0 = forms.FloatField(initial=0, help_text="lb-mol/h", min_value=0, max_value=1000)
    FM0 = forms.FloatField(initial=71.87, help_text="lb-mol/h", min_value=0, max_value=1000)
    class Meta:
        model = E124
        fields = ['T0']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class E126Form(forms.ModelForm):
    class Meta:
        model = E126
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class E127Form(forms.ModelForm):
    opcoes = [
        ('a','(a) Transferência de calor cocorrente'),
        ('b','(b) Transferência de calor em contracorrente'),
        ('c','(c) Ta constante'),
        ('d','(d) Operação adiabática'),
    ]
    x=forms.ChoiceField(label='Selecione a alternativa a ser resolvida:', choices=opcoes, required=False, widget=forms.RadioSelect, initial='a')
    class Meta:
        model = E127
        fields = ['T','FA','FB','FC','FD','Ta0']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            if i == 'x':
                self.fields[i].widget.attrs.update({'class':""})
            else:
                self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
                self.fields[i].label = listaDeSimbolos[i]

class E131Form(forms.ModelForm):
    opcoes = [
        ('a','(a) Operação Adiabática'),
        ('b','(b) Troca de Calor'),
    ]
    Ta0 = forms.FloatField(initial=290, help_text="K", min_value=1, max_value=400)
    V = forms.FloatField(initial=18, help_text="L", min_value=0, max_value=1000)
    tf = forms.FloatField(initial=4000, help_text="s", min_value=0, max_value=8000)
    NM = forms.FloatField(initial=98.8, help_text="mol", min_value=0, max_value=500)
    NA0 = forms.FloatField(initial=54.8, help_text="mol", min_value=0, max_value=500)
    NB0 = forms.FloatField(initial=555, help_text="mol", min_value=0, max_value=5000)
    x=forms.ChoiceField(label='Selecione a alternativa a ser resolvida:', choices=opcoes, required=False, widget=forms.RadioSelect, initial='a')
    class Meta:
        model = E131
        fields = ['X0','T0']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields_order = ['NA0','NB0','NM','X0','T0','Ta0','V','tf','x']
        self.fields = {field: self.fields[field] for field in self.fields_order}
        for i in self.fields:
            if i == 'x':
                self.fields[i].widget.attrs.update({'class':""})
            else:
                self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
                self.fields[i].label = listaDeSimbolos[i]

class E135Form(forms.ModelForm):
    T0 = forms.FloatField(initial=305, help_text="K", min_value=1, max_value=2000)
    CA0 = forms.FloatField(initial=4, help_text="mol/L", min_value=0, max_value=100)
    CB0 = forms.FloatField(initial=0, help_text="mol/L", min_value=0, max_value=100)
    CC0 = forms.FloatField(initial=0, help_text="mol/L", min_value=0, max_value=100)

    class Meta:
        model = E135
        fields = ['Ti','CAi','CBi','CCi']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class P1216Form(forms.ModelForm):
    Ta0 = forms.FloatField(initial=310, help_text="K", min_value=1, max_value=2000)
    FA0 = forms.FloatField(initial=10, help_text="mol/min", min_value=0, max_value=100)
    FB0 = forms.FloatField(initial=0, help_text="mol/min", min_value=0, max_value=100)
    UA = forms.FloatField(initial=3600, help_text="cal/min K", min_value=0, max_value=100000)
    k = forms.FloatField(initial=1, help_text="1/min (na temperatura Tk)", min_value=0)
    Tk = forms.FloatField(initial=400, help_text="K", min_value=1, max_value=2000)
    Kc = forms.FloatField(initial=100, help_text="(na temperatura TKc)", min_value=0,)
    TKc = forms.FloatField(initial=400, help_text="K", min_value=1, max_value=2000)

    class Meta:
        model = P1216
        fields = ['T0']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class P1223Form(forms.ModelForm):
    opcoes = [
        ('c','Ta constante'),
        ('d','Operação adiabática'),
        ('a','Transferência de calor cocorrente'),
        ('b','Transferência de calor em contracorrente'),
    ]
    x=forms.ChoiceField(label='Selecione a alternativa a ser resolvida:', choices=opcoes, required=False, widget=forms.RadioSelect, initial='a')
 
    k1 = forms.FloatField(initial=50, help_text="1/min (na temperatura Tk1)", min_value=0,)
    Tk1 = forms.FloatField(initial=305, help_text="K", min_value=1, max_value=2000)
    k2 = forms.FloatField(initial=4000, help_text="1/min (na temperatura Tk2)", min_value=0,)
    Tk2 = forms.FloatField(initial=310, help_text="K", min_value=1, max_value=2000)
    Kc = forms.FloatField(initial=10, help_text="(na temperatura TKc)", min_value=0,)
    TKc = forms.FloatField(initial=315, help_text="K", min_value=1, max_value=2000)

    class Meta:
        model = P1223
        fields = ['T0','FA0','FB0','FC0','Ta0']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            if i == 'x':
                self.fields[i].widget.attrs.update({'class':""})
            else:
                self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
                self.fields[i].label = listaDeSimbolos[i]

class DTR1Form(forms.ModelForm):
    k = forms.FloatField(initial=0.01, help_text="dm³/(mol min)", min_value=0,)
    CA0 = forms.FloatField(initial=8, help_text="mol/dm³", min_value=0, max_value=100)
    V = forms.FloatField(initial=1000, help_text="dm³", min_value=0, max_value=10000)
    v0 = forms.FloatField(initial=25, help_text="dm³/min", min_value=1, max_value=1000)
    N0 = forms.FloatField(initial=100, help_text="g", min_value=0, max_value=1000)
    npolinomio = forms.FloatField(initial=7, help_text="", min_value=0, max_value=10)

    class Meta:
        model = DTR1
        fields = ['t','C(t)']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class DTR2Form(forms.ModelForm):
    k = forms.FloatField(initial=0.28, help_text="m³/(kmol min)", min_value=0,)
    CA0 = forms.FloatField(initial=2, help_text="kmol/m³", min_value=0, max_value=100)
    tau = forms.FloatField(initial=10, help_text="min", min_value=0, max_value=1000,)
    CT0 = forms.FloatField(initial=2000, help_text="mg/dm³", min_value=0, max_value=10000)
    npolinomio = forms.FloatField(initial=3, help_text="", min_value=0, max_value=10)

    class Meta:
        model = DTR2
        fields = ['t','C(t)']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class DTR3Form(forms.ModelForm):
    k = forms.FloatField(initial=0.01, help_text="dm³/(mol min)", min_value=0,)
    CA0 = forms.FloatField(initial=8, help_text="mol/dm³", min_value=0, max_value=100)
    V = forms.FloatField(initial=1000, help_text="dm³", min_value=0, max_value=10000)
    v0 = forms.FloatField(initial=25, help_text="dm³/min", min_value=1, max_value=1000)
    N0 = forms.FloatField(initial=100, help_text="g", min_value=0, max_value=1000)

    class Meta:
        model = DTR3
        fields = ['t','C(t)']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

class DTR4Form(forms.ModelForm):
    k = forms.FloatField(initial=0.03, help_text="1/min", min_value=0,)
    V = forms.FloatField(initial=1000, help_text="dm³", min_value=0, max_value=10000)
    v0 = forms.FloatField(initial=25, help_text="dm³/min", min_value=1, max_value=1000)

    class Meta:
        model = DTR4
        fields = ['t','C(t)']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})
            self.fields[i].label = listaDeSimbolos[i]

listaDeSimbolos = {
    'T0': "Temperatura inicial do reator",
    'T': "Temperatura inicial do reator",
    'Ta0': "Temperatura inicial do fluido de troca térmica",
    'FA': "Vazão molar inicial da espécie A",
    'FB': "Vazão molar inicial da espécie B",
    'FC': "Vazão molar inicial da espécie C",
    'FD': "Vazão molar inicial da espécie D",
    'FA0': "Vazão molar inicial da espécie A",
    'FB0': "Vazão molar inicial da espécie B",
    'FC0': "Vazão molar inicial da espécie C",
    'FD0': "Vazão molar inicial da espécie D",
    'FI0': "Vazão molar inicial da espécie I (inerte)",
    'FM0': "Vazão molar inicial da espécie inerte",
    'ΔH1': "Variação de entalpia da reação 1",
    'ΔH2': "Variação de entalpia da reação 2",
    'deltaH1': "Variação de entalpia da reação 1",
    'deltaH2': "Variação de entalpia da reação 2",
    'cpA': "Calor específico da espécia A",
    'cpB': "Calor específico da espécia B",
    'cpC': "Calor específico da espécia C",
    'Ua': "Coeficiente Global de Perda de Calor",
    'UA': "Coeficiente Global de Transferência de Calor",
    'CT0': "Concentração inicial total (somando todas as espécies)",
    'k1': "Velocidade específica da reação 1",
    'k2': "Velocidade específica da reação 2",
    'k': "Velocidade específica da reação",
    'Tk1': "Temperatura associada a k1",
    'Tk2': "Temperatura associada a k2",
    'Tk': "Temperatura associada a k",
    'Kc': "Constante de equilíbrio",
    'TKc': "Temperatura associada a Kc",
    'V': "Volume do reator",
    'v0': "Vazão volumétrica inicial",
    'E1': "Energia de ativação da reação 1",
    'E2': "Energia de ativação da reação 2",
    'Tf': "Temperatura final do gráfico",
    'CA0': "Concentração inicial da espécie A",
    'CB0': "Concentração inicial da espécie B",
    'CC0': "Concentração inicial da espécie C",
    'NA0': "Número de mols da espécie A",
    'NB0': "Número de mols da espécie B",
    'NM': "Número de mols da espécie inerte",
    'X0': "Conversão inicial",
    'tf': "Tempo final do gráfico",
    'Ti': "Temperatura inicial do reator",
    'CAi': "Concentração inicial da espécie A no reator",
    'CBi': "Concentração inicial da espécie B no reator",
    'CCi': "Concentração inicial da espécie C no reator",
    'PT0': "Pressão parcial de tolueno",
    'PH20': "Pressão parcial de hidrogênio",
    'PB0': "Pressão parcial de benzeno",
    'PE': 'Dados experimentais da pressão parcial do etileno',
    'PH': 'Dados experimentais da pressão parcial do hidrogênio',
    'PEA': 'Dados experimentais da pressão parcial do etano',
    'taxa': '',
    'E':'Energia de ativação',
    'Ed':'Energia de ativação do decaimento',
    'k0':'Lei de velocidade',
    'k0d':'Constante de decaimento',
    'Tk0':'Temperatura associada a k0',
    'Tk0d':'Temperatura associada a k0d',
    't': 'Tempo de experimento de DTR',
    'C(t)': 'Concentração de traçador ao longo do tempo',
    'N0': 'Quantidade inicial de traçador',
    'npolinomio': 'Grau da regressão polinomial',
    'tau': 'Tempo de residência médio',
    'CT0': 'Concentração de entrada do traçador',
}