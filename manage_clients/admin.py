from django.contrib import admin
from manage_clients.models import Psychologist, Patient, PsychOpinion


class PatientInline(admin.StackedInline):
    model = Patient
    extra = 1


class PsychologistAdmin(admin.ModelAdmin):
    # adds the fields when you go to a particular psychologist object page
    fields = ['name', 'experience_level', 'session_price']
    inlines = [PatientInline]
    # adds the fields as columns on the general psych objects page
    list_display = ('name', 'experience_level', 'session_price')
    list_filter = ['experience_level']
    search_fields = ['name']


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal data', {'fields': ['name']}),
        (None, {'fields': ['age']}),
        ('Problems', {'fields': ['illness']}),
        ('Treating psychologist', {'fields': ['psychologist']}),
        (None, {'fields': ['next_session']}),
        ('Personal experience', {'fields': ['experience']}),
    ]
    list_display = ('name', 'illness', 'psychologist')
    list_filter = ['illness']


class PsychOpinionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'title', 'body_text']
    list_display = ('title', 'pub_date')


admin.site.register(Psychologist, PsychologistAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PsychOpinion, PsychOpinionAdmin)


