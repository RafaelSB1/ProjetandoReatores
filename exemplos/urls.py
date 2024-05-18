from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('e102/', views.e102_pbr_desativacao, name='e102_pbr_desativacao'),
    path('e103/', views.e103_pbr_taxa, name='e103_pbr_taxa'),
    path('e104/', views.e104_pbr_desativacao, name='e104_pbr_desativacao'),
    path('e122/', views.e122_pfr, name='e122_pfr'),
    path('e124/', views.e124_cstr, name='e124_cstr'),
    path('e125/', views.e125_pfr_multiplas, name='e125_pfr_multiplas'),
    path('e126/', views.e126_cstr_multiplas, name='e126_cstr_multiplas'),
    path('e127/', views.e127_pfr_multiplas, name='e127_pfr_multiplas'),
    path('e131/', views.e131_batelada, name='e131_batelada'),
    path('e132/', views.e132_batelada, name='e132_batelada'),
    path('e135/', views.e135_semibatelada, name='e135_semibatelada'),
    path('p1216/', views.p1216_cstr_reversivel, name='p1216_cstr_reversivel'),
    path('p1223/', views.p1223_pfr_multiplas_reversivel, name='p1223_pfr_multiplas_reversivel'),
    path('dtr1/', views.DTR1, name='DTR1'),
    path('dtr2/', views.DTR2, name='DTR2'),
    path('dtr3/', views.DTR3, name='DTR3'),
    path('dtr4/', views.DTR4, name='DTR4'),
    path('conversor_de_unidades', views.conversor_de_unidades , name="conversor_de_unidades"),
]