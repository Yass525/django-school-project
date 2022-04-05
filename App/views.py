from pyexpat.errors import messages
from django.views.generic import ListView,CreateView,DeleteView
from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from App.models import Projet
from .forms import AddProjetForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    return HttpResponse('Hi yassine')

def index_param(request,name):
    return HttpResponse('Hi %s'%name)


@login_required(login_url='login')
def Affiche(request):
    projet = Projet.objects.all()
    #resultat = "-".join([p.nom_projet for p in projet])
    #return HttpResponse(resultat)
    return render(request,"App/Affiche.html",{'p':projet})



class AfficheP(LoginRequiredMixin, ListView):
    model=Projet
    template_name='App/Affiche.html'
    context_object_name='p'
    list_dispplay=('nom_projet', 'besoin')

def Ajout(request):
    if request.method == "GET":
        form=AddProjetForm()
        return render(request,'App/Ajout.html',{'f':form})
    if request.method =="POST":
        form=AddProjetForm(request.POST)
        if form.is_valid():
            new_projet=form.save(commit=False)
            #commit false , recuperer les instance non sauvegardé
            new_projet.save()
            return HttpResponseRedirect(reverse('AfficheLV'))
        else:
            return render(request,'App/Ajout.html',{
                'f':form,
                'msg_erreur':"Erreur lors de l'ajout"
                })

class AjoutProject(CreateView):
    model = Projet
    fields = ['nom_projet','duree_projet','temps_alloue_createur','besoins','description','est_valide','createur']
    success_url = reverse_lazy('AfficheLV')

def Delete(request,id):
    projet = Projet.objects.get(pk=id)
    projet.delete()   
    return HttpResponseRedirect(reverse('AfficheLV'))

class DeleteGeneric(DeleteView):
    model = Projet
    uccess_url = reverse_lazy('AfficheLV')

def login_user(request):
    if request.method == "POST":
        u=request.POST['login']
        pwd=request.POST['password']
        user=authenticate(request, username=u, password=pwd)
        if user is not None:
            login(request,user)
            return redirect('AfficheLV')
        else:
            messages.info(request, 'username or password not valid')
            return redirect('login')
    else:  
        return render(request, 'login2.html')

def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form  = UserCreationForm()
    return render(request, 'register.html',{'f':form})

def logout(request):
    logout(request)
    return redirect('login')

def Acceuil(request):
    return render(request, 'base.html')