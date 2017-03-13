from django.contrib import admin

# Register your models here.
from person.models import Person



class PersonAdmin(admin.ModelAdmin):
    # list_per_page = 2
    ordering = ('first_name', 'last_name')
    list_display = ('full_name', 'first_name', 'last_name', "gender", 'colored_first_name')
    list_display_links = ('full_name',)
    raw_id_fields = ("relatives",)
    search_fields = ['first_name', 'last_name']
    # radio_fields = {"gender": admin.HORIZONTAL}
    list_editable = ("gender",)
    # list_filter = ('first_name',)
    preserve_filters = False

    change_list_template = "admin_person_list.html"

    # def changelist_view(self, request, extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['osm_data'] = self.get_osm_info()
    #     return super(MyModelAdmin, self).change_view(request, object_id,
    #                                                  form_url, extra_context=extra_context)

admin.site.register(Person, PersonAdmin)