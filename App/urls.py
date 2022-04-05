from django import views
from . import views
from django.urls import path
from .views import AfficheP, Ajout, AjoutProject, DeleteGeneric, login_user,logout
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('index/',views.index),
    path('index_p/<int:name>',views.index_param),
    path('Affiche/',views.Affiche),
    path('AfficheLV/',AfficheP.as_view(),name='AfficheLV'),
    path('Ajout/',views.Ajout,name='Ajout'),
    path('AjoutP/',AjoutProject.as_view(),name='AjoutP'),
    path('Delete/<int:id>',views.Delete, name='D'),
    path('DeleteGeneric/<int:pk>', DeleteGeneric.as_view(), name='DD'),
    path('login/', views.login_user, name='login'),
    path('Register/', views.register , name='register'),
    path('logout/', views.logout, name='logout'),
    path('Acceuil/', views.Acceuil, name="acceuil"),
    path('LoginView/', LoginView.as_view(template_name='login.html'),name='loginView'),
    path('LogoutView/', LogoutView.as_view(),name='loginView'),

]
    