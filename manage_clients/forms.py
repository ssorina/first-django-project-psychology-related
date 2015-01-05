from django import forms
from manage_clients.models import Psychologist, Patient, PsychOpinion


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class RequestForm(forms.Form):
    your_request = forms.CharField(label='Ask whatever crosses your mind', max_length=200, widget=forms.Textarea)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()


#class PsychForm(ModelForm):
#    class Meta:
#        model = PsychOpinion
#        fields = ['title', 'body_text']
