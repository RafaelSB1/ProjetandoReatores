from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .forms import *
from .tests import Multiplas, StrToFloat, reacao
from .tests import *
from django.db import transaction

from scipy.integrate import odeint
import numpy as np

from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf


@csrf_protect

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')

def conversor_de_unidades(request):
    return render(request,'conversor_de_unidades.html')

def e102_pbr_desativacao(request):
    if request.method=="GET":
        form = E102Form()
        context = {'form':form}
        return render(request, "e102_pbr_desativacao.html", context=context)
    else:
        form = E102Form(request.POST)
        if form.is_valid():
            #form.save()
            resposta = e102(request) #função no teste.py

            W = []
            X = []
            p = []
            PT = []
            PH2 = []
            PB = []
            a = []
            t = []
            
            with transaction.atomic(): # Saving the new data
                #E102.objects.all().delete() 
                i=0
                for y in resposta['a']:
                    a.append(round(y,4))
                for y in resposta['t']:
                    t.append(y)
                for y in resposta['W']:
                    W.append(y)
                for y in resposta['X']:
                    X.append(round(y,4))
                for y in resposta['p']:
                    p.append(round(y,4))
                for y in resposta['PT']:
                    PT.append(round(y,4))
                for y in resposta['PH2']:
                    PH2.append(round(y,4))
                for y in resposta['PB']:
                    PB.append(round(y,4))
                    #dados = E102(pk=i, W=round(W[i],2) , X=round(X[i],4), p=round(p[i],4), PT0=round(PT[i],4), PH20=round(PH2[i],4), PB0=round(y,4))
                    #dados.save()
                    i+=1
    
            #qs = E102.objects.all()
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
        
    context = {
        'form':form,
        #'qs': qs,
        'W': W,
        'X': X,
        'p': p,
        'PT': PT,
        'PH2': PH2,
        'PB': PB,
        'a': a,
        't': t,
               }
    #return render(request, "e102_pbr_desativacao.html", context=context)
    return JsonResponse({'W':W, 'X':X, 'p':p, 'PT':PT,'PH2':PH2, 'PB':PB, 'a':a, 't':t, 'sucesso':True})

def e103_pbr_taxa(request):
    if request.method=="GET":
        form = E103Form()
        context = {'form':form}
        return render(request, "e103_pbr_taxa.html", context=context)
    else:
        form = E103Form(request.POST)
        if form.is_valid():
            resposta = e103(request) #função no teste.py
            parametros = (resposta['parametros'])
            erro = (resposta['erro'])
            R_quadrado = (resposta['R_quadrado'])

        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
        
    context = {
        'form':form,
        'parametros': parametros,
        'erro': erro,
        'R_quadrado': R_quadrado,
               }
    return JsonResponse({'parametros':parametros, 'erro':erro, 'R_quadrado':R_quadrado, 'sucesso':True})

def e104_pbr_desativacao(request):
    if request.method=="GET":
        form = E104Form()
        context = {'form':form}
        return render(request, "e104_pbr_desativacao.html", context=context)
    else:
        form = E104Form(request.POST)
        if form.is_valid():
            resposta = e104(request) #função no teste.py
            X=[]
            Xd=[]
            t=[]
            a=[]
            for n in range(len(resposta['t'])):
                X.append(resposta['X'][n])
                Xd.append(resposta['Xd'][n])
                t.append(resposta['t'][n])
                a.append(resposta['a'][n])
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
        
    context = {
        'form':form,
        'X': X,
        'Xd': Xd,
        't': t,
        'a':a,
               }
    return JsonResponse({'X':X, 'Xd':Xd, 't':t, 'a':a, 'sucesso':True})

def e122_pfr(request):
    if request.method=="GET":
        form = E122Form()
        context = {'form':form}
        return render(request, "e122_pfr.html", context=context)
    else:
        form = E122Form(request.POST)
        if form.is_valid():
            #form.save()

            resposta = e122(request) #função no teste.py

            V = []
            X = []
            T = []
            Ta = []
            
            with transaction.atomic():
                #E122.objects.all().delete() 
                for i,y in enumerate(resposta['V']):
                    V.append(round(y*1000,2)) #dm³/tubo
                    X.append(round(resposta['X'][i],4))
                    T.append(round(resposta['T'][i],2))
                    Ta.append(round(resposta['Ta'][i],2))

                    #dados = E122(pk=i,  V=round(y*1000,2) , X=round(resposta['X'][i],4), T0=round(resposta['T'][i],2), Ta0=round(resposta['Ta'][i],2))
                    #dados.save()
            #qs = E122.objects.all()
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
            
    context = {
        'form':form,
        #'qs': qs,
        'V': V,
        'X': X,
        'T': T,
        'Ta': Ta,
               }
    
    #return render(request, "e122_pfr.html", context=context)
    return JsonResponse({'V':V, 'X':X, 'T':T, 'Ta':Ta, 'sucesso':True})

def e124_cstr(request):
    if request.method=="GET":
        form = E124Form()
        context = {'form':form}
        return render(request, "e124_cstr.html", context=context)
    else:
        form = E124Form(request.POST)
        if form.is_valid():
            ##form.save()

            resposta = e124(request) #função no teste.py

            T = []
            XBM = []
            XBE = []
            
            with transaction.atomic(): # Salvar os dados no banco de dados
                #E124.objects.all().delete() 
                for i in resposta['index']:
                    T.append(resposta['T'][i])
                    XBM.append(round(resposta['XBM'][i],4))
                    XBE.append(round(resposta['XBE'][i],4))
                    #dados = E124(pk=i,  T0=round(resposta['T'][i],2) , XBM=round(resposta['XBM'][i],4), XBE=round(resposta['XBE'][i],4))
                    #dados.save()
            #qs = E124.objects.all()
            qs=0
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
    context = {
        'form':form,
        'qs': qs,
        'T': T,
        'XBM': XBM,
        'XBE': XBE,

               }
    #return render(request, "e124_cstr.html", context=context)
    return JsonResponse({'T':T, 'XBM':XBM, 'XBE':XBE, 'EE':resposta['EE'], 'sucesso':True})

def e125_pfr_multiplas(request):
    if request.method=="GET":
        form = E125Form()
        context = {'form':form}
        return render(request, "e125_pfr_multiplas.html", context=context)
    else:
        form = E125Form(request.POST)
        if form.is_valid():
            #form.save()

            FA0 = float(request.POST.get("FA"))
            FB0 = float(request.POST.get("FB"))
            FC0 = float(request.POST.get("FC"))
            T0 = float(request.POST.get("T"))

            reacao(request) #função no teste.py

            CI = np.array([T0, FA0, FB0, FC0])
            CI = StrToFloat(CI)
            V = np.arange(0, 1.01, 0.01)  # faixa de variação do volume
            x = odeint(Multiplas, CI, V)

            labels = []
            T = []
            FA = []
            FB = []
            FC = []
            
            with transaction.atomic(): # Saving the new data
                #Dados.objects.all().delete() 
                for y in V:
                    labels.append(round(y,2))
                for i,y in enumerate(x):
                    T.append(round(y[0],2))
                    FA.append(round(y[1],2))
                    FB.append(round(y[2],2))
                    FC.append(round(y[3],2))
                    #dados = Dados(pk=i, T=round(y[0],2), FA=round(y[1],4), FB=round(y[2],4), FC=round(y[3],4), V=round(V[i],2))
                    #dados.save()
            #qs = Dados.objects.all()
            qs=0
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
        
    context = {
        'form':form,
        'FA':FA,
        'FB':FB,
        'FC':FC,
        'T':T,
        'V':labels,
        'qs':qs,
               }
    
    #return render(request, "e125_pfr_multiplas.html", context=context)
    return JsonResponse({'V':labels, 'FA':FA, 'FB':FB, 'FC':FC, 'T':T, 'sucesso':True})

def e126_cstr_multiplas(request):
    if request.method=="GET":
        form = E126Form()
        context = {'form':form}
        return render(request, "e126_cstr_multiplas.html", context=context)
    else:
        form = E126Form(request.POST)
        if form.is_valid():
            #form.save()

            resposta = e126(request) #função no teste.py

            T = resposta[0]
            GT = resposta[1]
            RT = resposta[2]
            EE = resposta[3]
            
            
            with transaction.atomic(): # Saving the new data
                #Dados.objects.all().delete() 
                T=[]
                for i in resposta[0]:
                    T.append(round(float(i),2))
            #qs = Dados.objects.all()
            #print(qs)
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})   
                
    context = {
        'form':form,
        #'qs': qs,
        'T': T,
        'GT': GT,
        'RT': RT,
        'EE': EE,
               }
    
    #return render(request, "e126_cstr_multiplas.html", context=context)
    return JsonResponse({'T':T, 'GT':GT, 'RT':RT, 'EE':EE, 'sucesso':True})

def e127_pfr_multiplas(request):
    if request.method=="GET":
        form = E127Form()
        context = {'form':form}
        return render(request, "e127_pfr_multiplas.html", context=context)
    else:
        form = E127Form(request.POST)
        if form.is_valid():
            #form.save()

            resposta = e127(request) #função no teste.py

            V = []
            T = []
            FA = []
            FB = []
            FC = []
            FD = []
            Ta = []
            
            with transaction.atomic(): # Saving the new data
                #E127.objects.all().delete() 
                i=0
                for y in resposta['V']:
                    V.append(round(y,2))
                for y in resposta['x']:
                    T.append(round(y[0],2))
                    FA.append(round(y[1],4))
                    FB.append(round(y[2],4))
                    FC.append(round(y[3],4))
                    FD.append(round(y[4],4))
                    Ta.append(round(y[5],2))
                    #dados = E127(pk=i, V=round(V[i],2) , T=round(y[0],2), FA=round(y[1],4), FB=round(y[2],4), FC=round(y[3],4), FD=round(y[4],4), Ta0=round(y[5],2))
                    i+=1
                    #dados.save()
            #qs = E127.objects.all()
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
                    
    context = {
        'form':form,
        #'qs': qs,
        'V': V,
        'T': T,
        'FA': FA,
        'FB': FB,
        'FC': FC,
        'FD': FD,
        'Ta': Ta,
               }
    
    #return render(request, "e127_pfr_multiplas.html", context=context)
    return JsonResponse({'V':V, 'FA':FA, 'FB':FB, 'FC':FC, 'FD':FD, 'T':T, 'Ta':Ta, 'sucesso':True})

def e131_batelada(request):
    if request.method=="GET":
        form = E131Form()
        context = {'form':form}
        return render(request, "e131_batelada.html", context=context)
    else:
        form = E131Form(request.POST)
        if form.is_valid():
            #form.save()

            resposta = e131(request) #função no teste.py

            t = []
            T = []
            X = []
            
            with transaction.atomic(): # Saving the new data
                #E131.objects.all().delete() 
                i=0
                for y in resposta['t']:
                    t.append(round(y,2))
                for y in resposta['x']:
                    T.append(round(y[0],2))
                    X.append(round(y[1],4))
                    #dados = E131(pk=i, t=round(t[i],2) , T0=round(y[0],2), X0=round(y[1],4))
                    i+=1
                    #dados.save()
            #qs = E131.objects.all()
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
                    
    context = {
        'form':form,
        #'qs': qs,
        'T': T,
        'X': X,
        't': t,
               }
    
    #return render(request, "e131_batelada.html", context=context)
    return JsonResponse({'t':t, 'X':X,'T':T, 'sucesso':True})



def e132_batelada(request):
    if request.method=="GET":
        form = E131Form(initial={'Ta0':298, 'NA0':9.044,'NB0':33.0,'NM':103.7,'T0':448,'X0':0})
        form.fields = {field: form.fields[field] for field in ['NA0','NB0','NM','T0','Ta0','X0']}
        context = {'form':form}
        return render(request, "e132_batelada.html", context=context)
    else:
        form = E131Form(request.POST, initial={'Ta0':298, 'NA0':9.044,'NB0':33.0,'NM':103.7,'T0':448,'X0':0})
        form.fields = {field: form.fields[field] for field in ['NA0','NB0','NM','T0','Ta0','X0']}
        if form.is_valid():
            #form.save()

            resposta = e132(request) #função no teste.py

            t = []
            T = []
            X = []
            
            with transaction.atomic(): # Saving the new data
                #E131.objects.all().delete() 
                i=0
                for y in resposta['t']:
                    t.append(round(float(y),2))
                for y in resposta['x']:
                    T.append(round(float(y[0]),2))
                    X.append(round(float(y[1]),4))
                    #dados = E131(pk=i, t=round(t[i],2) , T0=round(y[0],2), X0=round(y[1],4))
                    i+=1
                    #dados.save()
            #qs = E131.objects.all()
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
                   
    context = {
        'form':form,
        #'qs': qs,
        'T': T,
        'X': X,
        't': t,
               }
    
    #return render(request, "e132_batelada.html", context=context)
    return JsonResponse({'t':t, 'X':X,'T':T, 'sucesso':True})



def e135_semibatelada(request):
    if request.method=="GET":
        form = E135Form()
        context = {'form':form}
        return render(request, "e135_semibatelada.html", context=context)
    else:
        form = E135Form(request.POST,)
        if form.is_valid():
            #form.save()

            resposta = e135(request) #função no teste.py

            t = []
            T = []
            CA = []
            CB = []
            CC = []
            
            with transaction.atomic(): # Saving the new data
                #E135.objects.all().delete() 
                i=0
                for y in resposta['t']:
                    t.append(round(y,2))
                for y in resposta['x']:
                    T.append(round(y[0],2))
                    CA.append(round(y[1],4))
                    CB.append(round(y[2],4))
                    CC.append(round(y[3],4))
                    #dados = E135(pk=i, t=round(t[i],2) , Ti=round(y[0],2), CAi=round(y[1],4), CBi=round(y[2],4), CCi=round(y[3],4))
                    i+=1
                    #dados.save()
            #qs = E135.objects.all()
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
                    
    context = {
        'form':form,
        #'qs': qs,
        'T': T,
        'CA': CA,
        'CB': CB,
        'CC': CC,
        't': t,
               }
    
    #return render(request, "e135_semibatelada.html", context=context)
    return JsonResponse({'t':t, 'CA':CA, 'CB':CB, 'CC':CC,'T':T, 'sucesso':True})

def p1216_cstr_reversivel(request):
    if request.method=="GET":
        form = P1216Form()
        context = {'form':form}
        return render(request, "p1216_cstr_reversivel.html", context=context)
    else:
        form = P1216Form(request.POST,)
        if form.is_valid():
            #form.save()

            resposta = p1216(request) #função no teste.py

            T = []
            XBM = []
            XBE = []
            Xeq = []
            GT = []
            RT = []
            EE = resposta['EE']
            
            with transaction.atomic(): # Saving the new data
                #P1216.objects.all().delete() 
                for i in resposta['index']:
                    T.append(round(resposta['T'][i],2))
                    XBM.append(round(resposta['XBM'][i],4))
                    XBE.append(round(resposta['XBE'][i],4))
                    Xeq.append(round(resposta['Xeq'][i],4))
                    GT.append(round(resposta['GT'][i],2))
                    RT.append(round(resposta['RT'][i],2))
                    #dados = P1216(pk=i, T0=round(resposta['T'][i],2), XBM=round(resposta['XBM'][i],4), XBE=round(resposta['XBE'][i],4), Xeq=round(resposta['Xeq'][i],4), GT=round(resposta['GT'][i],2), RT=round(resposta['RT'][i],2))
                    #dados.save()
            #qs = P1216.objects.all()
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
                    
    context = {
        'form':form,
        #'qs': qs,
        'T': T,
        'XBM': XBM,
        'XBE': XBE,
        'Xeq': Xeq,
        'GT': GT,
        'RT': RT,
               }
    
    #return render(request, "p1216_cstr_reversivel.html", context=context)
    return JsonResponse({'T':T, 'Xeq':Xeq, 'XBM':XBM, 'XBE':XBE,'GT':GT,'RT':RT, 'EE':EE, 'sucesso':True})


def p1223_pfr_multiplas_reversivel(request):
    if request.method=="GET":
        form = P1223Form()
        context = {'form':form}
        return render(request, "p1223_pfr_multiplas_reversivel.html", context=context)
    else:
        form = P1223Form(request.POST,)
        if form.is_valid():
            #form.save()

            resposta = p1223(request) #função no teste.py

            V = []
            T = []
            FA = []
            FB = []
            FC = []
            Ta = []
            
            with transaction.atomic(): # Saving the new data
                #P1223.objects.all().delete() 
                for i in resposta['index']:
                    V.append(round(resposta['V'][i],1))
                    T.append(round(resposta['T'][i],2))
                    FA.append(round(resposta['FA'][i],4))
                    FB.append(round(resposta['FB'][i],4))
                    FC.append(round(resposta['FC'][i],4))
                    Ta.append(round(resposta['Ta'][i],2))
                    #dados = P1223(pk=i, V=round(resposta['V'][i],2), T0=round(resposta['T'][i],2), FA0=round(resposta['FA'][i],4), FB0=round(resposta['FB'][i],4), FC0=round(resposta['FC'][i],4), Ta0=round(resposta['Ta'][i],2))
                    #dados.save()
            #qs = P1223.objects.all()
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})
        
    context = {
        'form':form,
        #'qs': qs,
        'V': V,
        'T': T,
        'FA': FA,
        'FB': FB,
        'FC': FC,
        'Ta': Ta,
               }
    
    #return render(request, "p1223_pfr_multiplas_reversivel.html", context=context)
    return JsonResponse({'V':V, 'FA':FA, 'FB':FB, 'FC':FC,'T':T,'Ta':Ta, 'sucesso':True})


def DTR1(request):
    if request.method=="GET":
        form = DTR1Form()
        context = {'form':form}
        return render(request, "DTR1.html", context=context)
    else:
        form = DTR1Form(request.POST,)
        if form.is_valid():
            resposta = dtr1(request) #função no teste.py
            #Erro de regressão:
            if "erro" in resposta:
                return JsonResponse({'sucesso': False, 'erro_regressao': resposta["erro"]})

            t = list(resposta["t"])
            C = list(resposta["C"])
            E = list(resposta["E"])
            F = list(resposta["F"])
            dadosC = list(resposta["DadosExperimentaisC"])
            dadost = list(resposta["DadosExperimentaist"])
            dadosDTR = {'tm':resposta["tm"], '\u03C3²':resposta["variancia"], 'S³':resposta["inclinacao"], 'X':resposta["X"], 'Xseg':resposta["Xseg"], 'XMM':resposta["XMM"]}
            
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})

    return JsonResponse({"t":t, "C":C,"E":E,"F":F,"dadosC":dadosC,"dadost":dadost,"dadosDTR": dadosDTR, 'sucesso':True})

def DTR2(request):
    if request.method=="GET":
        form = DTR2Form()
        context = {'form':form}
        return render(request, "DTR2.html", context=context)
    else:
        form = DTR2Form(request.POST,)
        if form.is_valid():
            resposta = dtr2(request) #função no teste.py
            #Erro de regressão:
            if "erro" in resposta:
                return JsonResponse({'sucesso': False, 'erro_regressao': resposta["erro"]})

            t = list(resposta["t"])
            C = list(resposta["C"])
            E = list(resposta["E"])
            F = list(resposta["F"])
            dadosDTR = {'tm':resposta["tm"], '\u03C3²':resposta["variancia"], 'S³':resposta["inclinacao"], 'Xideal':resposta["Xideal"], 'Xmodelo':resposta["Xmodelo"], 'alfa':resposta["alfa"], 'beta':resposta["beta"], 'tauS':resposta["tauS"]}
            
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})

    return JsonResponse({"t":t, "C":C,"E":E,"F":F,"dadosDTR": dadosDTR, 'sucesso':True})

def DTR3(request):
    if request.method=="GET":
        form = DTR3Form()
        context = {'form':form}
        return render(request, "DTR3.html", context=context)
    else:
        form = DTR3Form(request.POST,)
        if form.is_valid():
            resposta = dtr3(request) #função no teste.py

            t = list(resposta["t"])
            C = list(resposta["C"])
            E = list(resposta["E"])
            F = list(resposta["F"])
            dadosDTR = {'tm':resposta["tm"], '\u03C3²':resposta["variancia"], 'S³':resposta["inclinacao"], 'XTES':resposta["XTES"], 'n':resposta["n"]}
            
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})

    return JsonResponse({"t":t, "C":C,"E":E,"F":F,"dadosDTR": dadosDTR, 'sucesso':True})

def DTR4(request):
    if request.method=="GET":
        form = DTR4Form()
        context = {'form':form}
        return render(request, "DTR4.html", context=context)
    else:
        form = DTR4Form(request.POST,)
        if form.is_valid():
            resposta = dtr4(request) #função no teste.py

            t = list(resposta["t"])
            C = list(resposta["C"])
            E = list(resposta["E"])
            F = list(resposta["F"])
            dadosDTR = {'tm':resposta["tm"], '\u03C3²':resposta["variancia"], 'S³':resposta["inclinacao"], 'X':resposta["X"], "X(CSTR)": resposta["X(CSTR)"], "X(PFR)": resposta["X(PFR)"], "m1": resposta['m1'], "m2": resposta['m2'], "Intersecao": resposta['Intersecao']}
            
        else:
            errors = {field: [error for error in field_errors] for field, field_errors in form.errors.items()}
            return JsonResponse({'sucesso': False, 'erros': errors})

    return JsonResponse({"t":t, "C":C,"E":E,"F":F,"dadosDTR": dadosDTR, 'sucesso':True})