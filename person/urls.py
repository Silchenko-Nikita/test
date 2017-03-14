from django.conf.urls import url
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import RedirectView

from person.views import PersonList, PersonDetail, PersonUpdate, PersonCreate, PersonDelete

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('person_list'))),
    url(r'^list/$', PersonList.as_view(), name='person_list'),
    url(r'^(?P<pk>\d+)/$', PersonDetail.as_view(), name="person_detail"),
    url(r'^add/$', PersonCreate.as_view(), name="person_create"),
    url(r'^(?P<pk>\d+)/edit/$', PersonUpdate.as_view(), name="person_update"),
    url(r'^(?P<pk>\d+)/delete/$', PersonDelete.as_view(), name="person_delete"),
]