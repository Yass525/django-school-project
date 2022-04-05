from email import message
from django.contrib import admin,messages


from App.models import Coach, Etudiant, MemberShipInProject, Projet

class Membership(admin.StackedInline):
    model=MemberShipInProject
    extra=1


class ProjectAdmin(admin.ModelAdmin):
    list_display=('nom_projet','duree_projet','temps_alloue_createur','est_valide','createur')
# Register your models here.
    def set_to_valid(self,reuqest,queryset):
        queryset.update(est_valide=True)
    def set_to_no_valid(self,request,queryset):
        row=queryset.filter(est_valide=False)
        if row.count()>0:
            #message="%s projet invalide" % row.count()
            #self.message_user(request,message)
           
            messages.error(request,"%s projet invalide" % row.count())
        else:
            row_update =queryset.update(est_valide=False)
            if row_update==1:
                message = "1 project was updatet"
            else:
                message = "%s projects were updated" %row_update
            self.message_user(request,message)
    actions=['set_to_valid','set_to_no_valid']
    set_to_valid.short_description="Valider"
    fieldsets=(
        ('information génétales',{
            'fields':('nom_projet','description','besoins','createur','superviseur',)
            }),
        ('Etat',{
            'fields':('est_valide',)
        }),
        ('Durée',{
            'fields':('duree_projet','temps_alloue_createur',)
        }),
    )
    inlines=(Membership,)
    list_filter=('nom_projet','est_valide')
    list_per_page=2
    search_fields=['nom_projet']
    ordering=['-nom_projet']

admin.site.register(Etudiant)

admin.site.register(Projet,ProjectAdmin)# sinon fouk la classe lehne thot @admin.register(projet)

admin.site.register(Coach)