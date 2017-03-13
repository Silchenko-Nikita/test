from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, render_to_response

# Create your views here.
from person.models import Person

def persons(request):
    person_list = Person.objects.all()
    paginator = Paginator(person_list, 2)

    page = request.GET.get('page')
    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        persons = paginator.page(1)
    except EmptyPage:
        persons = paginator.page(paginator.num_pages)

    return render_to_response('person_list.html', {"persons": persons})


def person_detail(request, id):
    try:
        person = Person.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404("Person does not exist")

    return render_to_response('person_detail.html', {"person": person})