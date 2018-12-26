from django import forms
from django.forms import inlineformset_factory, ModelMultipleChoiceField, CheckboxSelectMultiple

from addresses.models import *


class AddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "first_name", "last_name", "description", "groups"

class AddEmailForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = "__all__"


class AddPhoneForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = "__all__"


class AddAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


PhoneFormSet = inlineformset_factory(Person, PhoneNumber, fields='__all__', extra=1)
EmailFormSet = inlineformset_factory(Person, EmailAddress, fields='__all__', extra=1)
