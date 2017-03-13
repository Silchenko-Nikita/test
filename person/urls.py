from django.conf.urls import url

from person.views import persons, person_detail

urlpatterns = [
    url(r'^list/$', persons),
    url(r'^(?P<id>\d+)/$', person_detail, name="person_details"),
]