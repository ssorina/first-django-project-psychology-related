import datetime
import requests
from django.utils import timezone
from django.test import TestCase, Client
from manage_clients.models import PsychOpinion, Psychologist, Patient
from django.core.urlresolvers import reverse
from manage_clients import views
from django.contrib.auth.models import User

from manage_clients.forms import NameForm, ContactForm, RequestForm

# Create your tests here.


class HomeTest(TestCase):

    def setUp(self):
        PsychOpinion.objects.create(
            title='test title',
            body_text='text in the body of the Opinion',
            pub_date=timezone.now())
        Psychologist.objects.create(name='sorina', session_price=20, experience_level='E')

    def test_home_response_status(self):
#        opinion = PsychOpinion.objects.create(
#            title='test title',
#            body_text='text in the body of the Opinion',
#            pub_date=timezone.now())
        response = self.client.get(reverse('manage_clients:home'))
        self.assertEqual(response.status_code, 200)

    def test_opinion_title_display(self):
#        opinion = PsychOpinion.objects.create(
#            title='test title',
#            body_text='text in the body of the Opinion',
#            pub_date=timezone.now())
        response = self.client.get(reverse('manage_clients:home'))
        self.assertQuerysetEqual(
            response.context['latest_entries_list'],
            ['<PsychOpinion: test title>']
        )

    def test_psychologist_display(self):
#        psychologist = Psychologist.objects.create(name='sorina', session_price=20, experience_level='E')
        psychologist = Psychologist.objects.get(name='sorina')
        response = self.client.get(reverse('manage_clients:home'))
        self.assertContains(response, psychologist.name, 1)
        self.assertTemplateUsed(response, 'manage_clients/index.html')


class PsychologistTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse('manage_clients:psychologist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response,
                                   'manage_clients/single_entry.html')


class PsychologistSpecialTest(TestCase):

    def test_get(self):
        psychologist = Psychologist.objects.create(
            name='sorina',
            session_price=20,
            experience_level='E')
        response = self.client.get(reverse(
            'manage_clients:psychologist_special',
            args=(psychologist.id,)))
        self.assertEqual(response.status_code, 302)

    def test_patient_name_display(self):
        psychologist = Psychologist.objects.create(
            name='sorina',
            session_price=20,
            experience_level='E')
        patient = Patient.objects.create(name='testy',
                                         illness='MH',
                                         age=20,
                                         psychologist=psychologist,
                                         next_session=timezone.now())
        response = self.client.get(reverse(
            'manage_clients:psychologist_special',
            args=(patient.id,)))
        self.assertContains(response, patient.name)


class SingleEntryTest(TestCase):

    def test_get(self):
        opinion = PsychOpinion.objects.create(
            title='psychology is missed',
            body_text='text in the body of the Opinion',
            pub_date=timezone.now())
        response = self.client.get(reverse(
            'manage_clients:single_entry',
            args=(opinion.id,)))
        self.assertEqual(response.status_code, 200)

    def test_opinion_created(self):
        opinion = PsychOpinion.objects.create(
            title='psychology is missed',
            body_text='text in the body of the Opinion',
            pub_date=timezone.now())
        response = self.client.get(reverse(
            'manage_clients:single_entry',
            args=(opinion.id,)))
        self.assertTrue('Opinion' in response.content)
        self.assertTemplateUsed(response, 'manage_clients/single_entry.html')


class LoginTest(TestCase):

    def setUp(self):
        User.objects.create_user('sorina', 'sorina@test.com','pass')

    def test_admin_login(self):
        response = self.client.post('/admin/login/?next=/admin/', {'username': 'sorina','password': 'pass'})
        self.assertEqual(response.status_code, 200)



