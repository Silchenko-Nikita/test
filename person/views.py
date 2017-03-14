from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import UpdateView

from person.forms import PersonForm
from person.models import Person

# def persons(request):
#     person_list = Person.objects.all()
#     paginator = Paginator(person_list, 2)
#
#     page = request.GET.get('page')
#     try:
#         persons = paginator.page(page)
#     except PageNotAnInteger:
#         persons = paginator.page(1)
#     except EmptyPage:
#         persons = paginator.page(paginator.num_pages)
#
#     return render_to_response('person_list.html', {"persons": persons})


class PersonList(ListView):
    model = Person
    paginate_by = 4
    context_object_name = 'persons'
    template_name = 'person_list.html'


class PersonDetail(DetailView):
    model = Person
    context_object_name = 'person'
    template_name = 'person_detail.html'


class PersonCreate(CreateView):
    form_class = PersonForm
    # model = Person
    template_name = 'person_create.html'
    success_url = reverse_lazy('person_list')

    # def post(self, request, *args, **kwargs):
    #     form = PersonForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #     return redirect(reverse('person_list'), *args, **kwargs)

    # def form_valid(self, form):
    #     form.save()
    #
    #     return redirect(reverse('person_list'))


class PersonUpdate(UpdateView):
    form_class = PersonForm
    model = Person
    template_name = 'person_update.html'

    def get_success_url(self):
        return reverse('person_detail', kwargs={ "pk": self.get_object().pk })

    # def form_valid(self, form):
    #     form.save()
    #
    #     return redirect(reverse('person_list'))


class PersonDelete(DeleteView):
    model = Person
    template_name = 'person_delete.html'
    success_url = reverse_lazy('person_list')

    # def post(self, request, *args, **kwargs):
    #     Person.objects.get(pk=self.get_object().pk).delete()
    #     return redirect(PersonDelete.success_url)

#
# def person_detail(request, id):
#     try:
#         person = Person.objects.get(id=id)
#     except ObjectDoesNotExist:
#         raise Http404("Person does not exist")
#
#     return render_to_response('person_detail.html', {"person": person})