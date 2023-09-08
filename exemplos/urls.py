from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('e102/', views.e102_pbr_desativacao, name='e102_pbr_desativacao'),
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
]