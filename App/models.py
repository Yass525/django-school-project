from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
def is_esprit_email(value):
    if(str(value).endswith('@esprit.tn'))==False:
        raise ValidationError('Email doit contenir @ esprit.tn',params={'value':value})
class User(models.Model):
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    email=models.EmailField('Email',validators=[is_esprit_email])
    def __str__(self):
        return f'nom = f{self.nom},prenom = {self.prenom}'


class Etudiant(User):
    groupe = models.CharField(max_length=30)

class Coach(User):
        pass

class Projet(models.Model):
        nom_projet=models.CharField('Titre projet',max_length=30)
        duree_projet=models.IntegerField('Duree estimee',default=0)
        temps_alloue_createur=models.IntegerField('Temps alloue',validators=[MinValueValidator(1),MaxValueValidator(10)])
        besoins=models.TextField(max_length=100)
        description=models.TextField(max_length=100)
        est_valide=models.BooleanField(default=False)
        createur=models.OneToOneField(
            Etudiant,
            related_name='project_owner',
            on_delete=models.CASCADE
        )
        superviseur=models.ForeignKey(
            Coach,
            on_delete=models.SET_NULL,
            null=True,
            related_name='project_coach'
        )
        members=models.ManyToManyField(
            Etudiant,
            through='MemberShipInProject',
            related_name='Les_membres'
        )
class MemberShipInProject(models.Model):
    projet=models.ForeignKey(Projet,on_delete=models.CASCADE)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    time_allocated_By_Members=models.IntegerField()