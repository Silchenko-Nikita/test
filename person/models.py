from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import ManyToManyField
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

# Create your models here.

def validate_capitalized(value):
    if not value[0].isupper():
        raise ValidationError(
            _('Must be capitalized'),
        )

def validate_without_spaces(value):
    if ' ' in value:
        raise ValidationError(
            _('Must not have spaces'),
        )

class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    YEAR_IN_SCHOOL_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    first_name = models.CharField(max_length=50, validators=[validate_capitalized, validate_without_spaces])
    last_name = models.CharField(max_length=50, validators=[validate_capitalized, validate_without_spaces])
    gender = models.CharField(max_length=1, choices=YEAR_IN_SCHOOL_CHOICES, default=MALE)
    color_code = models.CharField(max_length=6)
    relatives = ManyToManyField('Person', blank=True)

    def colored_first_name(self):
        return format_html('<span style="color: #{};">{}</span>',
                           self.color_code,
                           self.first_name)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()

    def get_absolute_url(self):
        return reverse('person_details', args=[str(self.id)])

    full_name.short_description = "Full name"

    colored_first_name.admin_order_field = '-first_name'