from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, ListView, DetailView

from .forms import *
from .models import *
# Create your views here.


class AddPersonView(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'description', 'groups']
    template_name = "addresses/add_person.html"
    success_url = reverse_lazy("all")

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_formset = PhoneFormSet()
        email_formset = EmailFormSet()
        address_form = AddAddressForm()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                phone_formset=phone_formset,
                email_formset=email_formset,
                address_form=address_form
            ))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_formset = PhoneFormSet(self.request.POST)
        email_formset = EmailFormSet(self.request.POST)
        address_form = AddAddressForm(self.request.POST)
        if form.is_valid() and phone_formset.is_valid() and email_formset.is_valid() and address_form.is_valid():
            return self.form_valid(form, phone_formset, email_formset, address_form)
        else:
            return self.form_invalid(form, phone_formset, email_formset, address_form)

    def form_valid(self, form, phone_formset, email_formset, address_form):
        self.object = form.save(commit=False)
        self.object = form.save()
        phone_formset.instance = self.object
        phone_formset.save()
        email_formset.instance = self.object
        email_formset.save()
        self.object.address = address_form.save(commit=False)
        self.object.address = address_form.save()
        self.object = form.save()
        return HttpResponseRedirect(reverse_lazy("all"))


class ContactEditView(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'description', 'groups']
    template_name = "addresses/edit_person.html"
    success_url = reverse_lazy("all")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_formset = PhoneFormSet(instance=self.object)
        email_formset = EmailFormSet(instance=self.object)
        address_form = AddAddressForm(instance=self.object.address)
        return self.render_to_response(
            self.get_context_data(
                form=form,
                phone_formset=phone_formset,
                email_formset=email_formset,
                address_form=address_form
            ))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        phone_formset = PhoneFormSet(self.request.POST, instance=self.object)
        email_formset = EmailFormSet(self.request.POST, instance=self.object)
        address_form = AddAddressForm(self.request.POST, instance=self.object.address)
        if form.is_valid() and phone_formset.is_valid() and email_formset.is_valid() and address_form.is_valid():
            return self.form_valid(form, phone_formset, email_formset, address_form)
        else:
            return self.form_invalid(form, phone_formset, email_formset, address_form)

    def form_valid(self, form, phone_formset, email_formset, address_form):
        self.object = form.save(commit=False)
        self.object = form.save()
        phone_formset.instance = self.object
        phone_formset.save()
        email_formset.instance = self.object
        email_formset.save()
        address_form.instance = self.object
        address_form.save()
        return HttpResponseRedirect(reverse_lazy("all"))

    def form_invalid(self, form, phone_formset, email_formset, address_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  phone_formset=phone_formset,
                                  email_formset=email_formset,
                                  address_form=address_form))


class GetAllPersonsView(View):
    def get(self, request):
        persons = Person.objects.all().order_by("last_name")
        return render(request, "addresses/all.html", locals())


class ContactInfoView(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        phone_numbers = PhoneNumber.objects.filter(person=id)
        emails = EmailAddress.objects.filter(person=id)
        return render(request, "addresses/info.html", locals())


class ContactDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy("all")


class CreateGroupView(CreateView):
    model = Group
    fields = "__all__"
    success_url = reverse_lazy("all_groups")
    template_name = "addresses/add_group.html"


class GroupListView(ListView):
    model = Group
    template_name = "addresses/all_groups.html"

    def get_queryset(self):
        return Group.objects.annotate(
            members=Count('person', distinct=True)
        )


class GroupInfoView(View):
    def get(self, request, id):
        group = Group.objects.get(pk=id)
        members = Person.objects.filter(groups=group)
        return render(request, "addresses/group_info.html", locals())


class EditGroupView(UpdateView):
    model = Group
    fields = ['group_name', 'group_desc']
    template_name = "addresses/edit_group.html"
    success_url = reverse_lazy("all_groups")


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy("all_groups")
