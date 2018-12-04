from django.shortcuts import render, redirect
from django.views import View

from .forms import *
from .models import *
# Create your views here.


class AddPersonView(View):
    def get(self, request):
        person_form = AddPersonForm(request.GET or None)
        email_formset = EmailFormset(request.GET or None)
        phone_formset = PhoneFormset(request.GET or None)
        return render(request, "addresses/add_person.html", locals())

    def post(self, request):
        person_form = AddPersonForm(request.POST)
        email_formset = EmailFormset(request.POST)
        phone_formset = PhoneFormset(request.POST)

        if person_form.is_valid() and email_formset.is_valid() and phone_formset.is_valid():
            first_name = person_form.cleaned_data.get("first_name")
            last_name = person_form.cleaned_data.get("last_name")
            description = person_form.cleaned_data.get("description")
            new_person = Person()
            new_person.first_name = first_name
            new_person.last_name = last_name
            new_person.description = description
            new_person.save()
            for m_form in email_formset:
                mail = m_form.cleaned_data.get("mail")
                m_type = m_form.cleaned_data.get("m_type")
                new_mail = EmailAddress()
                new_mail.mail = mail
                new_mail.m_type = m_type
                new_mail.person = new_person
                new_mail.save()
            for p_form in phone_formset:
                p_num = p_form.cleaned_data.get("p_num")
                p_type = p_form.cleaned_data.get("p_type")
                new_phone = PhoneNumber()
                new_phone.p_num = p_num
                new_phone.p_type = p_type
                new_phone.person = new_person
                new_phone.save()
            return redirect("all")
        return render(request, "addresses/add_person.html", locals())


class GetAllPersonsView(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request, "addresses/all.html", locals())
