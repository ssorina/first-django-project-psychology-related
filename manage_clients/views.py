import datetime
from django.shortcuts import render, get_object_or_404
#from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from manage_clients.forms import NameForm, ContactForm, RequestForm
from manage_clients.models import PsychOpinion, Psychologist, Patient


def homepage(request):
    latest_entries_list = PsychOpinion.objects.order_by('-pub_date')[:7]
    psychologists = Psychologist.objects.order_by('name')
    form = ContactForm(request.POST)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        return HttpResponseRedirect('/home/')

    context = {
        'latest_entries_list': latest_entries_list,
        'psychologists': psychologists,
        'form': form,
        }
    return render(request, 'manage_clients/index.html', context)


def single_entry(request, title_id):
    entry = get_object_or_404(PsychOpinion, pk=title_id)
    return render(request, 'manage_clients/single_entry.html',
                  {'entry': entry})


def psychologist_page(request):
    psychologist = Psychologist.objects.order_by('-experience_level')
    context = {'psychologist': psychologist}
    return render(request, 'manage_clients/psychologist.html', context)


@login_required
def psychologist_special(request, name_id):
    psychologist = get_object_or_404(Psychologist, pk=name_id)
    patients = Patient.objects.filter(psychologist__pk=name_id).order_by(
        'name')
    context = {
        'psychologist': psychologist,
        'patients': patients,
        }
    return render(request, 'manage_clients/psychologist_special.html', context)


def patient(request):
    patient = Patient.objects.order_by('illness')
    context = {
        'patient': patient,
        }
    return render(request, 'manage_clients/patient.html', context)


def patient_experience(request, name_id):
    patient = get_object_or_404(Patient, pk=name_id)
    experience = Patient.objects.filter(pk=name_id)
    form = RequestForm(request.POST)
    context = {
        'experience': experience,
        'patient': patient,
        'form': form,
    }
    return render(request, 'manage_clients/patient_experience.html', context)



def get_name(request):
#    ''' processing form data for the NameForm'''
    if request.method == 'POST':
        #create form instance and populate it with data from request
        form = NameForm(request.POST)
        #check for validity
        if form.is_valid():
            return HttpResponseRedirect('/home/thanks/')
    #if request is GET or other method, create a blank form:
    else:
        form = NameForm()

    return render(request, 'manage_clients/name.html', {'form': form})


def thanks(request):
    return HttpResponse("""Thanks for submitting your name
           and question! We'll soon post the psychologist's response
           on our PsychOpinion pages as an article.""")


def opinion_upload(request):
    if request.method == "GET":
        return render(request, 'manage_clients/single_entry_test.html', {})
    elif request.method == "POST":
        psychopinion = PsychOpinion.objects.create(
            title=request.POST['title'],
            body_text=request.POST['body_text'],
            pub_date=datetime.datetime.now())
        return HttpResponseRedirect(reverse(
            'manage_clients:single_entry',
            kwargs={'title_id': psychopinion.id}))
