from django.forms import ModelForm
from .models import Athlete, Eventsignup, Groups, Event, ClassTime, Attendance
from django.forms.models import inlineformset_factory
from django.forms.formsets import BaseFormSet
from django.forms import modelformset_factory
from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction




class AthleteForm(ModelForm):
    class Meta:
        model = Athlete
        fields = ['first_name', 'last_name', 'group', 'dob', 'year', 'phonenumber', 'weight', 'email', 'gender', 'address', 'school', 'contact', 'contactnumber', 'gpa', 'goals', 'transcript', 'usaw']

class GroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['name']

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'description', 'date_start', 'date_end']

class AthleteEventForm(ModelForm):
    class Meta:
        model = Eventsignup
        fields = ['athlete', 'event', 'transportation']

class ClassTimeForm(ModelForm):
    class Meta:
        model = ClassTime
        fields = ['date']

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['classtime','athlete_id']

class AttendanceForm2(ModelForm):
    class Meta:
        model = Attendance
        fields = ['mark_attendance'] #'classtime','athlete_id', 