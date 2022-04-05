from tkinter import Widget
from django import forms
from App.models import Projet
from django.forms import Textarea

class AddProjetForm(forms.ModelForm):
    class Meta:
        model = Projet 
        fields=('nom_projet','duree_projet','temps_alloue_createur','besoins','description','est_valide','createur')
        widgets={'besoin':Textarea(attrs={'cols':20,'rows':10})}