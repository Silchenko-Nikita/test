# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-13 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import person.models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='second_name',
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default=2, max_length=50, validators=[person.models.validate_capitalized, person.models.validate_without_spaces]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=50, validators=[person.models.validate_capitalized, person.models.validate_without_spaces]),
        ),
    ]