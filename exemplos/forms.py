from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML

class DadosForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['FA','FB','FC','T']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})


class ConstForm(forms.ModelForm):
    class Meta:
        model = Const
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})

class E102Form(forms.ModelForm):
    tf = forms.FloatField(initial=0, help_text="período de desativação do catalisador em dias")
    class Meta:
        model = E102
        fields = ['PT0','PH20','PB0']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})

class E122Form(forms.ModelForm):
    opcoes = [
        ('a','1. Processo adiabático'),
        ('b','2. Transferência de calor, com Ta constante'),
        ('c','3. Transferência de calor em cocorrente, com Ta variável'),
        ('d','4. Transferência de calor em contracorrente, com Ta variável'),
    ]

    FI0 = forms.FloatField(initial=0.376, help_text="mol/s")
    FA0 = forms.FloatField(initial=0.0376, help_text="mol/s")
    FB0 = forms.FloatField(initial=0, help_text="mol/s")
    FC0 = forms.FloatField(initial=0, help_text="mol/s")
    FD0 = forms.FloatField(initial=0, help_text="mol/s")
    FA0_descricao = "descrevendoFA0"

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

class E124Form(forms.ModelForm):
    Ta0 = forms.FloatField(initial=545, help_text="R")
    V = forms.FloatField(initial=40.1, help_text="ft³")
    v0 = forms.FloatField(initial=326.3, help_text="ft³/h")
    FA0 = forms.FloatField(initial=43.04, help_text="lb-mol/h")
    FB0 = forms.FloatField(initial=802.8, help_text="lb-mol/h")
    FC0 = forms.FloatField(initial=0, help_text="lb-mol/h")
    FM0 = forms.FloatField(initial=71.87, help_text="lb-mol/h")
    class Meta:
        model = E124
        fields = ['T0']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})

class E126Form(forms.ModelForm):
    class Meta:
        model = E126
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})

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


class E131Form(forms.ModelForm):
    opcoes = [
        ('a','(a) Operação Adiabática'),
        ('b','(b) Troca de Calor'),
    ]
    Ta0 = forms.FloatField(initial=290, help_text="K")
    V = forms.FloatField(initial=18, help_text="L")
    tf = forms.FloatField(initial=4000, help_text="s")
    NM = forms.FloatField(initial=98.8, help_text="mol")
    NA0 = forms.FloatField(initial=54.8, help_text="mol")
    NB0 = forms.FloatField(initial=555, help_text="mol")
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

class E135Form(forms.ModelForm):
    T0 = forms.FloatField(initial=305, help_text="K")
    CA0 = forms.FloatField(initial=4, help_text="mol/L")
    CB0 = forms.FloatField(initial=0, help_text="mol/L")
    CC0 = forms.FloatField(initial=0, help_text="mol/L")

    class Meta:
        model = E135
        fields = ['Ti','CAi','CBi','CCi']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})

class P1216Form(forms.ModelForm):
    Ta0 = forms.FloatField(initial=310, help_text="K")
    FA0 = forms.FloatField(initial=10, help_text="mol/min")
    FB0 = forms.FloatField(initial=0, help_text="mol/min")
    UA = forms.FloatField(initial=3600, help_text="cal/min K")
    k = forms.FloatField(initial=1, help_text="1/min (na temperatura Tk)")
    Tk = forms.FloatField(initial=400, help_text="K")
    Kc = forms.FloatField(initial=100, help_text="(na temperatura TKc)")
    TKc = forms.FloatField(initial=400, help_text="K")

    class Meta:
        model = P1216
        fields = ['T0']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':"form-control form-control-sm"})

class P1223Form(forms.ModelForm):
    opcoes = [
        ('c','Ta constante'),
        ('d','Operação adiabática'),
        ('a','Transferência de calor cocorrente'),
        ('b','Transferência de calor em contracorrente'),
    ]
    x=forms.ChoiceField(label='Selecione a alternativa a ser resolvida:', choices=opcoes, required=False, widget=forms.RadioSelect, initial='a')
 
    k1 = forms.FloatField(initial=50, help_text="1/min (na temperatura Tk1)")
    Tk1 = forms.FloatField(initial=305, help_text="K")
    k2 = forms.FloatField(initial=4000, help_text="1/min (na temperatura Tk2)")
    Tk2 = forms.FloatField(initial=310, help_text="K")
    Kc = forms.FloatField(initial=10, help_text="(na temperatura TKc)")
    TKc = forms.FloatField(initial=315, help_text="K")

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