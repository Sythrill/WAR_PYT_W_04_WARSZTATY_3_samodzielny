from django import forms
from django.forms import formset_factory

from addresses.models import *


class AddPersonForm(forms.Form):
    first_name = forms.CharField(label="Imię", max_length=64)
    last_name = forms.CharField(label="Nazwisko", max_length=64)
    description = forms.CharField(label="Opis", widget=forms.Textarea)


class AddEmailForm(forms.Form):
    mail = forms.EmailField(label="Email")
    m_type = forms.ChoiceField(label="Rodzaj maila", choices=TYPES)


class AddPhoneForm(forms.Form):
    p_num = forms.CharField(label="Telefon", max_length=64)
    p_type = forms.ChoiceField(label="Rodzaj telefonu", choices=TYPES)


EmailFormset = formset_factory(AddEmailForm, extra=1)
PhoneFormset = formset_factory(AddPhoneForm, extra=1)
